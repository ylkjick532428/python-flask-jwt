import jwt, datetime, time
import flask, functools
from flask import jsonify, request
from app.users.model import UserAuths, Role
from .. import config
from .. import common

class Auth():
    @staticmethod
    #===========================================================================
    # encode_auth_token: 生成认证Token
    # :param user_id: int
    # :param login_time: int(timestamp)
    # :return: string
    #===========================================================================
    def encode_auth_token(user_id, login_time):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            tmp = jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
            return tmp
        except Exception as e:
            return e

    @staticmethod
    #===========================================================================
    # decode_auth_token : 验证Token
    # :param auth_token:
    # :return: integer|string
    #===========================================================================
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, config.SECRET_KEY, leeway=datetime.timedelta(seconds=3600))
            # 取消过期时间验证
#             payload = jwt.decode(auth_token, config.SECRET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    #===========================================================================
    # authenticate :  用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
    #===========================================================================
    def authenticate(self, username, password):
        user_id = UserAuths.get_id(username)
        userInfo = UserAuths.getInfo(user_id["user_id"])
        if (userInfo is None):
            return jsonify(common.falseReturn('', '找不到用户', 109))
        else:
            if (UserAuths.check_password(UserAuths, userInfo.password, password)):
                login_time = datetime.datetime.now()
                userInfo.login_time =  login_time
                userInfo.update_login_time(userInfo.login_time)
                print(userInfo.id, int(time.mktime(login_time.timetuple())))
                token = self.encode_auth_token(userInfo.id, int(time.mktime(login_time.timetuple())))
                if type(token) == bytes:
                    print (token)
                    token = str(token)[2:-1]
                return jsonify(common.trueReturn(token, '登录成功'))
            else:
                return jsonify(common.falseReturn('', '密码不正确', 108))

    #===========================================================================
    # identify : 用户鉴权
    #===========================================================================
    def identify(self, request):
        if request.method == "GET":
            _token = request.args.get("token", False)
        elif request.method == "POST":
            _token = request.form.get("token", False)
        else:
            return jsonify(common.falseReturn("", "方法错误"))
        
        if not _token:
            _token = request.cookies.get('token', False)
            
        if _token:
            return self.auth_www_token(self, _token)
        else:
            auth_header = request.headers.get('Authorization')
            if (auth_header):
                auth_tokenArr = auth_header.split(" ")
                if (not auth_tokenArr):
                    result = common.falseReturn('', '请传递正确的验证头信息', 106)
                else:
                    auth_token = auth_tokenArr[0]
                    print (auth_token)
                    return self.auth_www_token(auth_token)
            else:
                result = common.falseReturn('', '没有提供认证token', 104)
            
            return result
    
    #===========================================================================
    # auth_www_token : 认证token
    #===========================================================================
    def auth_www_token(self, auth_token):
        payload = self.decode_auth_token(auth_token)
        if not isinstance(payload, str):
            user = UserAuths.getInfo(payload['data']['id'])
            if (user is None):
                result = common.falseReturn('', '找不到该用户信息', 110)
            else:
                login_time = int((time.mktime(user.login_time.timetuple()) + user.login_time.microsecond/1000000.0))
                print (login_time, payload['data']['login_time'], payload['data']['login_time']==login_time)
                if (login_time == payload['data']['login_time']):
                    result = common.trueReturn(user.id, '请求成功')
                else:
                    result = common.falseReturn('', 'Token已更改，请重新登录获取', 105)
        else:
            result = common.falseReturn('', payload, 107)
        
        return result
    
#===============================================================================
# require_before : 判定参数
#===============================================================================
def require_before(*required_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            
            if request.method == "GET":
                for arg in required_args:
                    tmp_val = request.args.get(arg, False)
                    if not tmp_val:
                        return jsonify(common.falseReturn("", "参数不正确", 106))
            elif request.method == "POST":
                for arg in required_args:
                    tmp_val = request.form.get(arg, False)
                    if not tmp_val:
                        return jsonify(common.falseReturn("", "参数不正确", 106))
            
            return func(*args, **kw) 
        return wrapper
    return decorator

#===============================================================================
# require_login : 验证token/登陆
# request.user
# request.user_id
#===============================================================================
def require_login():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            result = Auth.identify(Auth, request)
            if (result and result['status'] and result['data']):
                request.user = UserAuths.query.filter_by(id=result['data']).first()
                request.user_id = result['data']
                return func(*args, **kw)
            else:
                return jsonify(result)
            
        return wrapper
    return decorator

#===============================================================================
# require_permission
#===============================================================================
def require_permission(*roles):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for role in roles:
                tmp_role = Role.query.filter_by(id=request.user.role_id).first()
#                 print (tmp_role , role, tmp_role == role)
                if tmp_role.name == role.name:
                    request.role = tmp_role
                    return func(*args, **kw)
            return jsonify(common.falseReturn("", "你的权限不足"))
            
        return wrapper
    return decorator

    
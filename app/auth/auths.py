import jwt, datetime, time
import flask, functools
from flask import jsonify, request
from app.users.model import UserAuths
from .. import config
from .. import common

class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
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
            print (tmp)
            return tmp
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
#             payload = jwt.decode(auth_token, config.SECRET_KEY, leeway=datetime.timedelta(seconds=3600))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, config.SECRET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        print (username)
        user_id = UserAuths.get_id(UserAuths, username)
        print (user_id)
        userInfo = UserAuths.getInfo(user_id)
        print (userInfo)
        if (userInfo is None):
            return jsonify(common.falseReturn('', '找不到用户', 109))
        else:
            if (UserAuths.check_password(UserAuths, userInfo.password, password)):
                login_time = datetime.datetime.now()
                userInfo.login_time =  login_time
                UserAuths.update_login_time(user_id, userInfo.login_time)
                token = self.encode_auth_token(user_id, int(time.mktime(login_time.timetuple())))
                return jsonify(common.trueReturn(token, '登录成功'))
            else:
                return jsonify(common.falseReturn('', '密码不正确', 108))

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if request.method == "GET":
            _token = request.args.get("token", False)
        elif request.method == "POST":
            _token = request.form.get("token", False)
        else:
            return jsonify(common.falseReturn("", "方法错误"))
        
        #检查cookie中是否有token
        if not _token:
            weixin_token = request.cookies.get('token', False)
            return self.auth_www_token(self, _token)
        else:
            if (auth_header):
                auth_tokenArr = auth_header.split(" ")
                if (not auth_tokenArr):
                    result = common.falseReturn('', '请传递正确的验证头信息', 106)
                else:
                    auth_token = auth_tokenArr[0]
                    return self.auth_www_token(auth_token)
            else:
                result = common.falseReturn('', '没有提供认证token', 104)
        return result
    
    def identify_cookies(self, request):
        """
        用户鉴权(微信授权后回调)
        :return: list
        """
        tmp_token = request.cookies.get('token', False)
        return self.auth_www_token(self, tmp_token)
    
    def auth_www_token(self, auth_token):
        payload = self.decode_auth_token(auth_token)
        if not isinstance(payload, str):
            print (payload['data'])
            user = UserAuths.getInfo(payload['data']['id'])
            print (user)
            if (user is None):
                result = common.falseReturn('', '找不到该用户信息', 110)
            else:
                login_time = int((time.mktime(user["login_time"].timetuple()) + user["login_time"].microsecond/1000000.0))
                print (login_time, payload['data']['login_time'], payload['data']['login_time']==login_time)
                if (login_time == payload['data']['login_time']):
                    result = common.trueReturn(user["id"], '请求成功')
                else:
                    result = common.falseReturn('', 'Token已更改，请重新登录获取', 105)
        else:
            result = common.falseReturn('', payload, 107)
        
        return result
    
#判定参数
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

def require_permission(*required_args):
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

    
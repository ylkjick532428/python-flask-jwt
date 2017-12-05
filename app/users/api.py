from flask import jsonify, request, session
from app.users.model import UserAuths
from app.auth.auths import Auth, require_before
from .. import common
import uuid
import time

def init_api(app):
    
    @app.route('/api/login/check', methods=['POST', 'GET'])
    #===========================================================================
    # check_login: 检查用户是否已经登陆
    #===========================================================================
    def check_login():
        result = Auth.identify(Auth, request)
        if (result and result['status'] and result['data']):
            user_info = UserAuths.getInfo(result['data'])
            returnUser = {
                'id': result['data'],
                'username': user_info.name,
                'login_time': user_info.login_time
            }
            return jsonify(common.trueReturn(returnUser, "请求成功"))
        else:
            return jsonify(common.falseReturn("", "请求失败"))
    
    @app.route('/api/user/check', methods=["GET", "POST"])
    #===========================================================================
    # user_check: 检查用户名是否已经注册
    #===========================================================================
    def user_check():
        if request.method == "GET":
            username = request.args.get("username", False)
        elif request.method == "POST":
            username = request.form.get("username", False)
        if not username:
            return jsonify(common.falseReturn('', '用户检查失败，参数错误', 110))
        user_info = UserAuths.get_id(username)
        if user_info["is_have"]:
            return jsonify(common.falseReturn('', '用户已经注册请登陆', 101))
        return jsonify(common.trueReturn('', '用户未注册'))
        
    @app.route('/api/register', methods=['GET', 'POST'])
    #===========================================================================
    # register: 用户注册
    #===========================================================================
    def register():
        if request.method == 'POST':
            username = request.form.get('username', False)
            password = request.form.get('password', False)
            
        elif request.method == 'GET':
            username = request.args.get('username', False)
            password = request.args.get('password', False)
        
        if not (username and password):
            return jsonify(common.falseReturn('', '用户注册失败, 缺少参数 username=%s, password=%s' % (username, password)))
        # 最后一条记录及其ID
        user = UserAuths(username)
        user_id = UserAuths.get_id(UserAuths, username)
        userInfo = UserAuths.getInfo(user_id)
        if userInfo:
            return jsonify(common.falseReturn('', '用户注册失败,已经存在', 101))
        add_result = user.add(user_id, username, password)
        
        
        if add_result:
            print (user_id)
            userInfo = user.getInfo(user_id)
            print (userInfo)
            if userInfo:
                login_time = int(time.time())
                userInfo["login_time"] = login_time
                UserAuths.update_login_time(user_id, userInfo["login_time"])
                token = Auth.encode_auth_token(user_id, login_time)
                
                returnUser = {
                    'id': user_id,
                    'username': username,
                    'login_time': userInfo['login_time'],
                    'token': token
                }
                return jsonify(common.trueReturn(returnUser, "用户注册成功"))
        return jsonify(common.falseReturn('', '用户注册失败', 100))

    @app.route('/api/login', methods=['GET', 'POST'])
    #===========================================================================
    # login: 用户登录
    #===========================================================================
    def login():
        if request.method == 'POST':
            username = request.form.get('username', False)
            password = request.form.get('password', False)
        elif request.method == 'GET':
            username = request.args.get('username', False)
            password = request.args.get('password', False)
        else:
            return jsonify(common.falseReturn('', '请使用POST提交', 103))
        if (not username or not password):
            return jsonify(common.falseReturn('', '用户名和密码不能为空', 102))
        else:
            return Auth.authenticate(Auth, username, password)


    @app.route('/api/user', methods=['GET', "POST"])
    #===========================================================================
    # get: 获取用户信息
    #===========================================================================
    def get():
        result = Auth.identify(Auth, request)
        if (result and result['status'] and result['data']):
            user_info = UserAuths.getInfo(result['data'])
            returnUser = {
                'id': user_info.id,
                'username': user_info.name,
                'login_time': user_info.login_time,
            }
            result = common.trueReturn(returnUser, "请求成功")
            return jsonify(result)
        return jsonify(common.falseReturn("", "请求失败"))
    
    @app.route('/api/user/update', methods=['GET', 'POST'])
    @require_before("token", "user_id", "type_name", "value")
    #===========================================================================
    # update_info : 更新用户信息
    #===========================================================================
    def update_info():
        if request.method == 'POST':
            token = request.form.get('token', False)
            user_id = request.form.get('user_id', False)
            filed_type = request.form.get('type_name', False)
            filed_value = request.form.get('value', False)
        elif request.method == 'GET':
            token = request.args.get('token', False)
            user_id = request.args.get('user_id', False)
            filed_type = request.args.get('type_name', False)
            filed_value = request.args.get('value', False)
        else:
            pass
        
        if not token or not user_id or not filed_type or not filed_value:
            return jsonify(common.falseReturn("", "字段参数错误,不能为空", 112))
        
        result = Auth.identify(Auth, request)
        if (result and result['status'] and result['data']):
            user_info = UserAuths.getInfo(result['data'])
            if result['data'] != user_id:
                return jsonify(common.falseReturn("", "认证错误,检查到你伪造用户", 113))
            
            if filed_type not in ["sfz", "nickname", "phone"]:
                return jsonify(common.falseReturn("", "更新失败,不支持的字段", 114))
            
            if filed_type in ["phone"]:
                return jsonify(common.falseReturn("", "暂时不支持修改手机号", 115))
            
            tmp_user = UsersBasic()
            tmp_user.update(user_id, filed_type, filed_value)
            user_info = UserAuths.getInfo(result['data'])
            returnUser = {
                'id': result['data'],
                'username': user_info["username"],
                'login_time': user_info["login_time"],
                'nickname': user_info["nickname"],
                'sfz': user_info["sfz"][:6],
                "open_id": user_info["open_id"]
            }
            return jsonify(common.trueReturn(returnUser, "请求成功"))
        else:
            return jsonify(common.falseReturn("", "跟新用户信息失败, 认证不通过", 111))
        
        
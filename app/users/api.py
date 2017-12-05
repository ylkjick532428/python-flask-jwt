'''
Created on 2017年12月4日

@author: honey
'''
import uuid
import datetime
import time, functools

from flask import jsonify, request, session
from app.users.model import UserAuths
from app.auth.auths import Auth, require_before, require_login,\
    require_permission
from app.users.model import init_roles
from .. import common


USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE = init_roles()

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
        # 查询用户名是否存在
        user_id = UserAuths.get_id(username)
        if user_id["is_have"]:
            return jsonify(common.falseReturn('', '用户注册失败,已经存在', 101))
        
        add_result = UserAuths.add(user_id["user_id"], username, password, DEFAULT_ROLE)
        if add_result:
            userInfo = UserAuths.getInfo(user_id["user_id"])
            if userInfo:
                login_time = datetime.datetime.now()
                userInfo.login_time =  login_time
                userInfo.update_login_time(userInfo.login_time)
                token = Auth.encode_auth_token(userInfo.id, int(time.mktime(login_time.timetuple())))
                if type(token) == bytes:
                    token = str(token)[2:-1]
            
                returnUser = {
                    'id': userInfo.id,
                    'username': username,
                    'login_time': userInfo.login_time,
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
    @require_login()
    @require_permission(DEFAULT_ROLE)
    #===========================================================================
    # get: 获取用户信息
    #===========================================================================
    def get():
        user_info = UserAuths.getInfo(request.user_id)
        returnUser = {
            'id': user_info.id,
            'username': user_info.name,
            'login_time': user_info.login_time,
        }
        result = common.trueReturn(returnUser, "请求成功")
        return jsonify(result)
    
    @app.route('/api/user/update', methods=['GET', 'POST'])
    @require_before("token", "user_id", "type_name", "value")
    @require_login()
    #===========================================================================
    # update_info : 更新用户信息
    #===========================================================================
    def update_info():
        if request.method == 'POST':
            user_id = request.form.get('user_id', False)
            filed_type = request.form.get('type_name', False)
            filed_value = request.form.get('value', False)
        else:
            user_id = request.args.get('user_id', False)
            filed_type = request.args.get('type_name', False)
            filed_value = request.args.get('value', False)
        
        user = request.user
        if user_id != user.id:
            return jsonify(common.falseReturn("", "操作失败, 伪造用户"))
        
        return jsonify(common.trueReturn("", "请求成功"))
        
        
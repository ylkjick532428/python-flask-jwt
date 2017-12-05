'''
Created on 2017年12月4日

@author: honey
'''

import uuid
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, ForeignKey, func
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from app.util.mysql_utility import MySqlUtil
from app import app
from flask.globals import session
db = SQLAlchemy(app)
        
class TEST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def update(self):
        admin = TEST.query.filter_by(id='1').first()
        admin.username = 'my_new_email@example.com'
        db.session.commit()
    
class Permission:
    USER = 1
    ADMIN = 2
    DEFAULT = USER

DEFAULT_ROLE = Permission.DEFAULT

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    permission = db.Column(db.Integer)

class UserAuths(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    role_id = db.Column(db.Integer)
    register_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    login_time = db.Column(db.TIMESTAMP) #onupdate=datetime.datetime.now
    access_token = db.Column(db.String(255))

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def update(self, update_filed, update_value):
        db.session.update(UserAuths.__tablename__).where(UserAuths.id==self.id).values(update_filed=update_value)
        return session_commit()
    
    def update_login_time(self, new_login_time):
        self.login_time = new_login_time #datetime.datetime.now()
        return db.session.commit()
    
    @staticmethod
    #===========================================================================
    # get_id : 更加用户名获得用户id
    #===========================================================================
    def get_id(username):
        """get user id from profile file, if not exist, it will
        generate a uuid for the user.
        """
        if username is not None:
            tmp_user = UserAuths.query.filter_by(name=username).first()
            if tmp_user:
                print (tmp_user)
                return {"user_id": tmp_user.id, "is_have": True}
            else:
                return {"user_id": str(uuid.uuid4()), "is_have": False}
        else:
            return {"user_id": str(uuid.uuid4()), "is_have": False}
            
    
    #===========================================================================
    # is_exist : 判断用户是否已经存在
    #===========================================================================
    @staticmethod
    def is_exist(username):
        user_count = UserAuths.query.filter_by(name=username).count()
        if user_count:
            return True
        else:
            return False
        
    @staticmethod    
    #===========================================================================
    # add: 创建用户
    #===========================================================================
    def add(user_id, username, password, role, email=""):
        password_hash = generate_password_hash(password)
        if UserAuths.is_exist(username):
            return False
        else:
            new_user = UserAuths(id=user_id, name=username, password=password_hash, email=email, role_id=role.id)
            db.session.add(new_user)
            db.session.commit()
            return True
    
    @staticmethod
    def getInfo(user_id):
        try:
            if not user_id:
                return None
            else:
                tmp_user = UserAuths.query.filter_by(id=user_id).first()
                if tmp_user:
                    print(tmp_user)
                    return tmp_user
        except:
            return None
        return None
        
    @staticmethod
    def get(user_id):
        """try to return user_id corresponding User object.
        This method is used by load_user callback function
        """
        try:
            if not user_id:
                return None
            else:
                tmp_user = UserAuths.query.filter_by(id=user_id).first()
                if tmp_user:
                    return tmp_user.id
        except:
            return None
        return None

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason

#===============================================================================
# init_roles : 用户权限
#===============================================================================
def init_roles():
    global USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE
    tmp_count = db.session.query(func.count(Role.id)).scalar()
    if tmp_count <= 0:
        USER_ROLE = Role(name='USER', permission=Permission.USER)
        ADMIN_ROLE = Role(name='ADMIN', permission=Permission.ADMIN)
        DEFAULT_ROLE = Role(name='DEFAULT', permission=Permission.DEFAULT)
        db.session.add(USER_ROLE)
        db.session.add(ADMIN_ROLE)
        db.session.add(DEFAULT_ROLE)
        db.session.commit()
    else:            
        USER_ROLE = Role.query.filter_by(permission=Permission.USER).first()
        ADMIN_ROLE = Role.query.filter_by(permission=Permission.ADMIN).first()
        DEFAULT_ROLE = Role.query.filter_by(permission=Permission.DEFAULT).first()
    return USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE
    
if __name__ == '__main__':
    USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE = init_roles()
    print (USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE.name)
    user_id = str(uuid.uuid4())
    UserAuths.add(user_id, "jick", "jick", DEFAULT_ROLE, "jick@jick.com")
    print (UserAuths.getInfo(user_id))
#     db.session.update(UserAuths.__tablename__).where(UserAuths.id==user_id).values(login_time=new_login_time)
    
#     db.session.update(TEST.__tablename__).where(TEST.id=="1").values(username="df")
    tmp = TEST.query.filter_by(id="1").first()
    tmp.name = "dddddd"
    print(tmp.id)
    user_id="3c3e057c-8c03-43dc-b297-79a488218a94"
    jj = UserAuths.query.filter_by(id=user_id).first()
    kk = UserAuths.query.filter_by(id=user_id).first()
    print (jj, kk)
#     TEST.update().where(id="1").values(username="df")


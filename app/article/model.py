'''
Created on 2017年12月5日

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
from app.users.model import Permission
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.TEXT)
    user_id = db.Column(db.String(36))
    stat = db.Column(db.Integer, default=1)
    create_time = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    modify_time = db.Column(db.TIMESTAMP, onupdate=datetime.datetime.now)
    
    def __str__(self):
        
        return {"id": self.id, "content": self.content, "modify_time": self.modify_time}
    
    @staticmethod
    #===========================================================================
    # add : 创建博文
    #===========================================================================
    def add(content, user_id):
        new_article = Article(content=content, user_id=user_id)
        db.session.add(new_article)
        db.session.commit()
        return new_article
    
    @staticmethod
    #===========================================================================
    # delete: 删除博文
    #===========================================================================
    def delete(article_id, user_role, user_id):
        tmp_article = Article.query.filter_by(id=article_id, stat=1).first()
        if not tmp_article:
            return {"stat": False, "msg": "文章不存在"}
        
#         print (user_role.permission, Permission.ADMIN)
        if tmp_article and tmp_article.user_id != user_id:
            if user_role.permission == Permission.ADMIN:
                tmp_article.stat = 0
                db.session.commit()
                return {"stat": True, "msg": "文章删除成功"}
            else:
                return {"stat": False, "msg": "你权限不足"}
        else:
            tmp_article.stat = 0
            db.session.commit()
            return {"stat": True, "msg": "文章删除成功"}
        
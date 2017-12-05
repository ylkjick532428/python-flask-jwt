'''
Created on 2017年12月5日

@author: honey
'''
import uuid
import datetime
import time, functools

from flask import jsonify, request, session
from app.article.model import Article
from app.auth.auths import Auth, require_before, require_login,\
    require_permission
from app.users.model import init_roles
from .. import common


USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE = init_roles()

def init_article(app):
    @app.route('/api/article/post', methods=['POST'])
    @require_before("content")
    @require_login()
    @require_permission(DEFAULT_ROLE)
    #===========================================================================
    # post: 发布文章
    #===========================================================================
    def post():
        content = request.form.get("content", "").strip()
        new_article = Article.add(content, request.user_id)
        return jsonify(common.trueReturn({"article_id": new_article.id}, "发布文章成功"))
    
    @app.route('/api/article/delete', methods=['POST'])
    @require_before("article_id")
    @require_login()
    @require_permission(DEFAULT_ROLE, ADMIN_ROLE)
    #===========================================================================
    # delete: 删除文章
    #===========================================================================
    def delete():
        article_id = request.form.get("article_id", False)
        user_role = request.role
        print (user_role)
        result = Article.delete(article_id, user_role, request.user_id)
        if result["stat"]:
            return jsonify(common.trueReturn(result, "删除文章成功"))
        else:
            return jsonify(common.falseReturn(result, "删除文章失败"))
    
    
    @app.route('/api/article/list', methods=['POST'])
    @require_login()
    @require_permission(DEFAULT_ROLE, ADMIN_ROLE)
    #===========================================================================
    # delete: 删除文章
    #===========================================================================
    def list():
        articles = Article.query.filter_by(stat=1)
        result = []
        for article in articles:
            article_time = article.modify_time if article.modify_time else article.create_time
            result.append({"id": article.id, "content": article.content, "modify_time": article_time})
        return jsonify(common.trueReturn(result, ""))
    

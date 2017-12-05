from flask import Flask, request
from flask import session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templates')
app.config.from_object("app.config")
Session(app)

db = SQLAlchemy(app)

global USER_ROLE, ADMIN_ROLE, DEFAULT_ROLE

@app.after_request
# send CORS headers
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response

def init_app(app):
#     db.init_app(app)
    from app.users.model import init_roles
    init_roles()
    
    from app.users.api import init_api
    from app.article.api import init_article
    init_api(app)
    init_article(app)
    return app

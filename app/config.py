"""
create database if not exists eigen default character set utf8;
GRANT ALL PRIVILEGES ON `eigen`.* TO 'eigen'@'%' IDENTIFIED BY '3c38f92dfd6dc09023fe49c8917';
SET old_passwords = 0;
UPDATE mysql.user SET Password = PASSWORD('3c38f92dfd6dc09023fe49c8917') WHERE User = 'eigen' limit 1;
SELECT LENGTH(Password) FROM mysql.user WHERE User = 'eigen';
FLUSH PRIVILEGES;
"""

db_config_local={'NAME': 'eigen',
            'USER': 'eigen',
            'PASSWORD': '3c38f92dfd6dc09023fe49c8917',
            'HOST': 'localhost',
            'PORT': 3306}

DB_USER = db_config_local["USER"]
DB_PASSWORD = db_config_local["PASSWORD"]
DB_HOST = db_config_local["HOST"]
DB_DB = db_config_local["NAME"]

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SECRET_KEY = "eigen"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
SESSION_TYPE = 'filesystem'
print (SQLALCHEMY_DATABASE_URI)

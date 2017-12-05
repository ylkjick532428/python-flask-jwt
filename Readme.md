## 
### 依赖

windows需要 cpp编译工具

http://landinghub.visualstudio.com/visual-cpp-build-tools

mac 需要安装Xcode开发者工具

### 安装依赖python3.5.3依赖包
pip install -r requirements.txt

### eigen.postman_collection.json
* postman 接口调试数据
* request 测试工具 [postman chrome扩展](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-ntp-icon)
* [使用介绍](http://blog.csdn.net/u013613428/article/details/51557804)


### 创建数据库账号

```sql
create database if not exists eigen default character set utf8;
GRANT ALL PRIVILEGES ON `eigen`.* TO 'eigen'@'%' IDENTIFIED BY '3c38f92dfd6dc09023fe49c8917';
SET old_passwords = 0;
UPDATE mysql.user SET Password = PASSWORD('3c38f92dfd6dc09023fe49c8917') WHERE User = 'eigen' limit 1;
SELECT LENGTH(Password) FROM mysql.user WHERE User = 'eigen';
FLUSH PRIVILEGES;
```

### 数据库设置(mysql)
* navcate 初始化数据表 eigen.sql
* app.config.py 数据库配置文件

### python3 run.py 运行网站


### 用户注册

```
POST /api/register HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: f757dfc2-167c-4308-f7ca-5cca48b7a761
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

test
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="password"

test
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
#### 请求参数：
* username
* password

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": {
        "id": "ed2726c0-8d0c-4d40-8047-f8994dd437f2",
        "login_time": "Tue, 05 Dec 2017 20:48:13 GMT",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJrZW4iLCJkYXRhIjp7ImlkIjoiZWQyNzI2YzAtOGQwYy00ZDQwLTgwNDctZjg5OTRkZDQzN2YyIiwibG9naW5fdGltZSI6MTUxMjQ3ODA5Mn0sImV4cCI6MTUxMjQ3ODEwMiwiaWF0IjoxNTEyNDc4MDkyfQ.VR-V7IrBiGy83QHUb9Ep8nI4Q4_CnoFEvotDrFYLQkU",
        "username": "test"
    },
    "msg": "用户注册成功",
    "status": true
}
```

#### Fail Response

**Content examples**

```json
{
    "code": 101,
    "data": "",
    "msg": "用户注册失败,已经存在",
    "status": false
}
```

### 登陆

```
POST /api/login HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 3e5bbcdc-2212-2640-9c13-2ccdcc360e7d
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

test
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="password"

test
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
#### 请求参数：
* username
* password

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJrZW4iLCJkYXRhIjp7ImlkIjoiZWQyNzI2YzAtOGQwYy00ZDQwLTgwNDctZjg5OTRkZDQzN2YyIiwibG9naW5fdGltZSI6MTUxMjQ3ODE5MX0sImV4cCI6MTUxMjQ3ODIwMSwiaWF0IjoxNTEyNDc4MTkxfQ.AnuTdlJ7ZN4a9YCIFzXRXNGxLwsXTc5WfQu6UHw3fHA",
    "msg": "登录成功",
    "status": true
}
```

#### Fail Response

**Content examples**

```json
{
    "code": 108,
    "data": "",
    "msg": "密码不正确",
    "status": false
}
```

### 获得用户信息

```
POST /api/user HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: f64db4e5-e8fd-1d22-8b22-1bb32cef20fb
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="token"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJrZW4iLCJkYXRhIjp7ImlkIjoiZWQyNzI2YzAtOGQwYy00ZDQwLTgwNDctZjg5OTRkZDQzN2YyIiwibG9naW5fdGltZSI6MTUxMjQ3ODI3MX0sImV4cCI6MTUxMjQ3ODI4MSwiaWF0IjoxNTEyNDc4MjcxfQ.GKSgFKIIogBuCs8RRALjXKkvgIWtsGtKJ67FvCwVlxU
------WebKitFormBoundary7MA4YWxkTrZu0gW--

```
#### 请求参数：
* token

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": {
        "id": "ed2726c0-8d0c-4d40-8047-f8994dd437f2",
        "login_time": "Tue, 05 Dec 2017 20:51:11 GMT",
        "username": "test"
    },
    "msg": "请求成功",
    "status": true
}
```

#### Fail Response

**Content examples**

```json
{
    "code": 107,
    "data": "",
    "msg": "无效Token",
    "status": false
}
```

### 发布文章

```
POST /api/article/post HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: be0e2890-536e-8d30-c355-d8de35074b49
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="token"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJrZW4iLCJkYXRhIjp7ImlkIjoiZWQyNzI2YzAtOGQwYy00ZDQwLTgwNDctZjg5OTRkZDQzN2YyIiwibG9naW5fdGltZSI6MTUxMjQ3ODI3MX0sImV4cCI6MTUxMjQ3ODI4MSwiaWF0IjoxNTEyNDc4MjcxfQ.GKSgFKIIogBuCs8RRALjXKkvgIWtsGtKJ67FvCwVlxU
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="content"

dfhdfdfiads地方还是短发的覅撒地方还是发
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
#### 请求参数：
* content 文章内容
* token

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": {
        "article_id": 25
    },
    "msg": "发布文章成功",
    "status": true
}
```

#### Fail Response

**Content examples**

```json

```

### 文章列表

```
POST /api/article/list HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 338943b5-01a9-62a9-edd5-c61b3ca8c69f
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

jick
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="password"

jick
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="token"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTI0NzU2NzQsImRhdGEiOnsibG9naW5fdGltZSI6MTUxMjQ3NTY3NCwiaWQiOiIxMzdmY2E2YS03MDUyLTQ2MzUtYjQ3Yi0yMzNmYTEwMjlmZWEifSwiZXhwIjoxNTEyNDc1Njg0LCJpc3MiOiJrZW4ifQ.P1EMqW3s563ULeIuC3hhqoytMXoqx0IhR4imUa8hZNg
------WebKitFormBoundary7MA4YWxkTrZu0gW--

```
#### 请求参数：
* token

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": [
        {
            "content": "dfhdfdfiads地方还是短发的覅撒地方还是发",
            "id": 1,
            "modify_time": "Tue, 05 Dec 2017 19:54:02 GMT"
        }
    ],
    "msg": "",
    "status": true
}
```

#### Fail Response

**Content examples**

```json
{
    "code": 107,
    "data": "",
    "msg": "无效Token",
    "status": false
}
```

### 删除文章

```
POST /api/article/delete HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 3747ae6c-b3ac-58b2-a8ac-2431311f0c57
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="token"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MTI0NzU2NzQsImRhdGEiOnsibG9naW5fdGltZSI6MTUxMjQ3NTY3NCwiaWQiOiIxMzdmY2E2YS03MDUyLTQ2MzUtYjQ3Yi0yMzNmYTEwMjlmZWEifSwiZXhwIjoxNTEyNDc1Njg0LCJpc3MiOiJrZW4ifQ.P1EMqW3s563ULeIuC3hhqoytMXoqx0IhR4imUa8hZNg
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="article_id"

1
------WebKitFormBoundary7MA4YWxkTrZu0gW--

```
#### 请求参数：
* article_id 文章id
* token

#### Success Response

**Content examples**

```json
{
    "code": 200,
    "data": {
        "msg": "文章删除成功",
        "stat": true
    },
    "msg": "删除文章成功",
    "status": true
}
```

#### Fail Response

**Content examples**

```json
{
    "code": 200,
    "data": {
        "msg": "文章不存在",
        "stat": false
    },
    "msg": "删除文章失败",
    "status": false
}
```

**Content examples 用户删除他人文章, 权限不足**

```json
{
    "code": 200,
    "data": {
        "msg": "你权限不足",
        "stat": false
    },
    "msg": "删除文章失败",
    "status": false
}
```






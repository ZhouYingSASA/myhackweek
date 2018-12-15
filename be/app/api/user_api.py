# coding: utf-8
from flask_restful import Resource
from app.util.rest_util import add_args
from app.resources.user import User
from app import auth
from flask import g


class Token(Resource):

    def post(self):
        args = add_args([
            ["username", str, True, "缺少用户名"],
            ["password", str, True, "缺少密码"]
        ]).parse_args()
        username = args.get("username")
        password = args.get("password")
        token = User.user_verify_password(username, password)
        if not token:
            return {
                "message": "用户名或密码错误",
                "code": 1
            }
        return {
            "message": "ok",
            "code": 0,
            "token": token
        }

    @auth.login_required
    def get(self):
        homeUser = g.user
        return {
            "status": 1,
            "message": "验证成功",
            "user": {
                "id": homeUser.id,
                "xh": homeUser.username,
                "name": homeUser.name,
                "head_pic_url": homeUser.head_pic_url
            }
        }

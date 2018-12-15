from app.util.qiniu import get_pic_url
from flask import g
from flask_restful import Resource
from app import auth
from app.util.rest_util import add_args
from app.model.models import user


class Mine(Resource):
    @auth.login_required
    def get(self):
        user = g.user
        if user is None:
            return {
                "status": 0,
                "message": u"未登录"
            }
        dict = {}
        dict['name'] = user.name
        dict['head_pic_url'] = get_pic_url(user.username + '.jpg')
        dict["app_avatar_url"] = get_pic_url(user.app_avatar_name)

        dict['status'] = 1
        dict['message'] = u'请求成功'
        return dict

    def post(self):
        args = add_args([
            ["username", str, True, "缺少用户名"],
        ]).parse_args()
        username = args.get("username")
        grade = user.query.filter(user.username == username)
        if not username:
            return {
                "message": "用户名错误",
                "code": 1
            }
        return {
            "message": "ok",
            "code": 0,
            "grade": grade,
        }
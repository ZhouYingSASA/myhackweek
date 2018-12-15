# coding: utf-8
from flask_restful import Resource
from app.resources.apply import Apply
from app.util.rest_util import add_args
from flask import g
from app import auth


class Join(Resource):

    def __init__(self):
        self.success_message = {
            "message": "ok",
            "code": 0
        }
        self.failed_message = {
            "message": "error",
            "code": 1
        }

    def success(self, data=None):
        message = self.success_message.copy()
        if data:
            message["data"] = data
        return message

    def failed(self):
        return self.failed_message

    @auth.login_required
    def post(self):
        homeUser = g.user
        args = add_args([
            ["activity_id", int, True, "缺少activity_id"],
        ]).parse_args()
        activity_id = args.get("activity_id")
        a = Apply()
        data = a.join_activity(homeUser, activity_id)
        if not data:
            return self.failed()
        return data

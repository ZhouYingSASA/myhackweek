# coding: utf-8
from app.model.models import homeUser


class User(object):

    @staticmethod
    def user_verify_password(username, password):
        homeuser = homeUser.query.filter_by(
            username=username
        ).first()
        if not homeuser:
            return None
        if not homeuser.verify_password(password):
            return None
        return homeuser.generate_auth_token()

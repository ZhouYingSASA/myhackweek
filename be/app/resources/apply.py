# coding: utf-8
from app.model.models import actUser, user
from app import db


class Apply(object):

    def first_login(self, homeUser):
        username = homeUser.username
        if not homeUser:
            return u"没有权限"
        r = user(username=username,
                 grade=1,
                 )
        try:
            db.session.add(r)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return u"数据库错误"
        return {
            "status": 1,
            "message": "存入用户数据成功",
        }

    def join_activity(self, homeUser, activity_id):
        username = homeUser.username
        if not homeUser:
            return u"没有权限"
        r = actUser(username=username,
                    activity_id=activity_id,
                    )
        try:
            db.session.add(r)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return u"数据库错误"
        return {
            "status": 1,
            "message": "用户加入活动成功",
        }

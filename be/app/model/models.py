# config=utf-8
from app import db
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash


SECRET_KEY = "8e127c14-9ae0-4726-9a0d-137f64de3e47"


class homeUser(db.Model, UserMixin):
    __bind_key__ = 'passport_user'
    __tablename__ = 'users'
    id = db.Column(db.String(10), primary_key=True)

    username = db.Column(db.String(64),
                         unique=True,
                         index=True)  # student id or teacher id

    name = db.Column(db.String(64),
                     unique=False)  # true name

    password_hash = db.Column(db.String(128))

    head_pic_url = db.Column(db.String(120))  # head pic url

    app_avatar_name = db.Column(db.String(120), default=False)

    def __init__(
            self,
            username=None,
            password='123456',
            name=''):
        self.id = self.generate_id()
        self.username = username
        self.password = password
        self.name = name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<homeUser %r>' % (self.username)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# 获取token的方法，默认时间是60分钟(60*60秒)
    def generate_auth_token(self, expiration=3000):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        t = s.dumps({'id': self.id})
        try:
            return t.decode()
        except Exception:
            return None

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except Exception:
            return None
        user = homeUser.query.filter_by(id=data.get("id")).first()
        return user


class actUser(db.Model):
    __tablename__ = 'act_user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('user.username'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

    def __repr__(self):
        return '<actUser %r>' % (self.username)


class activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    pic_url = db.Column(db.String(150), nullable=False)
    bg_pic_url = db.Column(db.String(150), nullable=False)
    content = db.Column(db.String(160), nullable=False)
    organizer = db.Column(db.String(20), nullable=False)
    time = db.Column(db.Text(20), nullable=False)
    users = db.relationship(
        'user',
        secondary='act_user',
        backref='activity',
        lazy="select")

    def __repr__(self):
        return '<activity %r>' % (self.title)


class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    activities = db.relationship(
        'activity',
        secondary='act_user',
        backref='user',
        lazy="select")

    def __repr__(self):
        return '<user %r>' % (self.username)

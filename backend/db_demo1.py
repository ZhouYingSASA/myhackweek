import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                      'mysql+pymysql://passport_user:+WIscsL5' + \
                      'ncuhomev5.mysql.rds.aliyuncs.com/passport?charset=utf8'
SECRET_KEY = 'hard to guess'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(10), primary_key=True)
    username = db.Column(db.String(64),
                         unique=True,
                         index=True)  # student id or teacher id
    password_hash = db.Column(db.String(128))

    def __init__(
            self,
            username=None,
            password='123456',
            name=''):

        self.username = username
        self.password = password
# 似乎只能创建表，创建不了database！！

# db.create_all()

# insert 操作

# record=User('tuitui','tongdunkeji')
# record1=User('tuitui1','tongdunkeji1')
# db.session.add(record)
# db.session.add(record1)
# db.session.commit()


# query操作
# qres=User.query.filter_by(username='tuitui1',password='tongdunkeji1').first()
# delete 操作
# db.session.delete(qres)
# db.session.commit()


@app.route('/')
def index():
    username = request.args.get('username')
    password = request.args.get('password')
    qres = User.query.filter_by(username=username, password=password).first()
    if qres is None:
        return "用户名或密码不对"
    else:
        return "成功登陆"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5002)

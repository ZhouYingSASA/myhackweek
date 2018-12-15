import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://user:ye123456@' + \
        'zhouyingsasa.xyz/test?charset=utf8'
    SQLALCHEMY_BINDS = {
        "passport_user": 'mysql+pymysql://passport_user:+WIscsL5@' +
        'ncuhomev5.mysql.rds.aliyuncs.com/passport?charset=utf8',
        }
    SECRET_KEY = 'hard to guess'
    QINIU_HEADPIC_ACCESS_KEY = 'L3KFIE40u9sfW8zIb3Ssa2Wa5ICNbFAZp1NllMO0'
    QINIU_HEADPIC_SECRET_KEY = 'Pdb1jQCIXJB-Cj86bWrGbPpJfkBTPYHfHrmFJiSB'
    QINIU_HEADPIC_EXPIRES = 3600
    QINIU_HANDPIC_BASE_URL = 'https://photocdn.ncuos.com'

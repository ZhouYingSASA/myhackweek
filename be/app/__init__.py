# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.model.models import homeUser
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from flask import g
auth = HTTPTokenAuth(scheme='passport')
basic_auth = HTTPBasicAuth()


@auth.verify_token
def verify_token(token):
    if token == '':
        return False
    user = homeUser.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True

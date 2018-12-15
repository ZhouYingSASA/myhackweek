from flask import current_app
from qiniu import Auth


def get_pic_url(filename):

    access_key = current_app.config['QINIU_HEADPIC_ACCESS_KEY']
    secret_key = current_app.config['QINIU_HEADPIC_SECRET_KEY']

    q = Auth(access_key, secret_key)

    base_url = current_app.config['QINIU_HANDPIC_BASE_URL'] + '/' + filename

    expires = current_app.config['QINIU_HEADPIC_EXPIRES']

    private_url = q.private_download_url(base_url, expires)

    return private_url

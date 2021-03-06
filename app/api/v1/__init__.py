"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from flask import Blueprint
from app.api.v1 import user, client, token


def create_blueprint_v1():
    """
    红图向蓝图(v1)注册
    """
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1

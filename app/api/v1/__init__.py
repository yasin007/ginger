"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from flask import Blueprint
from app.api.v1 import user
from app.api.v1 import client

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1

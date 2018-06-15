# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午10:02
# @Author  : 维尼的小熊
# @FileName: __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from app.api.v1 import user


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    return bp_v1

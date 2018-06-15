# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午10:03
# @Author  : 维尼的小熊
# @FileName: user.py
# @Software: PyCharm

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_use():
    return "im a pig"

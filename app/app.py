"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import date


class JSONEncoder(_JSONEncoder):
    """
    序列化从model里找相应的序列化key
    处理时间类型
    """

    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

"""
create by 维尼的小熊 on 2018/6/19

"""
__autor__ = 'yasin'

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    # 400参数错误 401 403 404
    # 500 未知错误
    # 200 成功 201更新成功 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid'
    error_code = 1000
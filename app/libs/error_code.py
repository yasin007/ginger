"""
create by 维尼的小熊 on 2018/6/19

"""
__autor__ = 'yasin'

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    """
    删除成功
    """
    code = 202
    error_code = 1


class ServerError(APIException):
    """
    服务器未知错误
    """
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ParameterException(APIException):
    """
    参数错误
    """
    code = 400
    msg = 'invalid'
    error_code = 1000


class NotFound(APIException):
    """
    没有找到资源和界面
    """
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    """
    没有授权
    """
    code = 401
    error_code = 1005
    msg = '没有授权'


class Forbidden(APIException):
    """
    禁止访问权限不够
    """
    code = 403
    error_code = 1004
    msg = '禁止访问权限不够'


class HttpFailed(APIException):
    """
    http请求错误
    """
    code = 405
    error_code = 1007
    msg = 'http错误'

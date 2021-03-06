"""
create by 维尼的小熊 on 2018/6/19

"""
__autor__ = 'yasin'

from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    """
    自定义异常 重写HTTPException
    """
    code = 500
    msg = 'sorry -- error'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        """
        去掉问号后面内容保留主路径
        :return: 主路径
        """
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

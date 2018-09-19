"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException
from app.libs.error_code import ServerError, HttpFailed

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    """
    捕捉全局异常
    :param e: Exception，APIException，HTTPException
    :return:异常类型
    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        return HttpFailed(msg=e.description, code=e.code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


# 入口
if __name__ == '__main__':
    app.run(debug=True)

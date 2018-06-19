"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from app.app import create_app
from app.libs.error import APIException
from werkzeug.exceptions import HTTPException
from app.libs.error_code import ServerError

app = create_app()


# 全局异常
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


# 入口
if __name__ == '__main__':
    app.run(debug=False)

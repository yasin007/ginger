"""
create by 维尼的小熊 on 2018/6/19

"""
__autor__ = 'yasin'

from wtforms import Form
from app.libs.error_code import ParameterException
from flask import request

class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self

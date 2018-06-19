"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms import ValidationError
from app.libs.enums import ClinetTypeEnum

from app.models.user import User
from app.validators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    # 承接类型转换直接使用枚举类型
    def validate_type(self, value):
        try:
            client = ClinetTypeEnum(value.data)
        except ValueError as e:
            raise e

        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='请填写正确的邮箱')])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')

    ])

    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    # 验证用户是否注册过
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()

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
    # 用户账号
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    # 用户密码
    secret = StringField()
    # 客户端类型
    type = IntegerField(validators=[DataRequired()])

    # 承接类型转换直接使用枚举类型

    def validate_type(self, value):
        try:
            client = ClinetTypeEnum(value.data)
        except ValueError as e:
            raise e

        self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[DataRequired(message='邮箱不允许为空'), Email(message='请填写正确的邮箱')])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='请输入6位至22位格式密码')

    ])
    nickname = StringField(validators=[DataRequired(message='昵称不允许为空'),
                                       length(min=2, max=22)])

    # 验证用户是否注册过
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message='邮箱已经注册过')

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError(message='昵称已经存在')

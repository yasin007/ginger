"""
create by 维尼的小熊 on 2018/6/19

"""
__autor__ = 'yasin'
from flask import current_app, jsonify
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClinetTypeEnum
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    """登录"""

    form = ClientForm().validate_for_api()

    promis = {
        ClinetTypeEnum.USER_EMAIL: User.verify,
    }

    identity = promis[ClinetTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )

    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """
    生成令牌
    有效期2小时
    """

    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })

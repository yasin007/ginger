"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClinetTypeEnum
from app.models.user import User
from app.libs.error_code import Success

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promis = {

        ClinetTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promis[form.type.data]()
    # 可预知的异常
    # 完全没有意识到的异常 未知异常
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)

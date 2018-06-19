"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return "im a pig"


@api.route('/create')
def create_user():
    # name
    # passworld
    # api 数据
    # 客户端
    return "im a pig"

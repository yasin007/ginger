"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base, db
from app.libs.error_code import NotFound, AuthFailed


class User(Base):
    # parmark 建表
    id = Column(Integer, primary_key=True)  # 主键
    email = Column(String(24), unique=True, nullable=False)  # 邮箱
    nickname = Column(String(24), unique=True)  # 昵称
    auth = Column(SmallInteger, default=1)  # 权限标识
    _password = Column('password', String(100))  # 密码

    # 序列化对象
    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    def __getitem__(self, item):
        return getattr(self, item)

    # parmark 设置密码
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # parmark 注册入库-邮箱
    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404('您还没有注册，请先去注册')
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

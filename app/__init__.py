"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'

from .app import Flask


def register_blueprints(app):
    """
    v1蓝图对象向flask对象注册
    添加url前缀v1
    """
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    """
    注册数据库
    """
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app

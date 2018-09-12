"""
create by 维尼的小熊 on 2018/6/15

"""
__autor__ = 'yasin'


class Redprint:
    """
    创建红图Redprint重写路由装饰器和注册
    """

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
        重写装饰器函数 利用mound列表存储起来后注册
        """

        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):

        """
        重写蓝图注册函数

        :param bp: 函数
        :param url_prefix: 如果红图url_prefix不存在则添加红图名字
        :return: 添加到add_url_rule
        """

        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            endpoint = self.name + '+' + \
                       options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

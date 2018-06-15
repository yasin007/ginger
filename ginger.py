# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 上午8:53
# @Author  : 维尼的小熊
# @FileName: ginger.py
# @Software: PyCharm

from app.app import create_app

app = create_app()

# 入口
if __name__ == '__main__':
    app.run(debug=True)

'''
    decorators 全局 装饰器
'''
from flask import g
from flask import redirect
from flask import url_for
from  functools import wraps


# 限制只有登录了才能访问的装饰器
def login_required(func):
    # @wraps 这个函数必须添加
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,"user"):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('the_users.login'))
    return wrapper
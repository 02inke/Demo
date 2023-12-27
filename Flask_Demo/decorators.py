from functools import wraps
from flask import g,redirect,url_for

def login_required(func):
    #保留func的信息
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user:
            print("真的有g.user,",g.user)
            return func(*args,**kwargs)
        else:
            return redirect(url_for('author.login'))
    return inner

#装饰器

'''

def func2(f):

    def wrapper(*args,**kwargs):
        f(*args,**kwargs)
        print('email:123@qq.com')
    return wrapper
@func2
def func1(name):
    print(f'{name}')
    print('name:inke','age:21')


func1('hello world')

'''

"""
question.py
    问答平台的首页蓝图文件
"""
from flask import render_template
from flask import Blueprint
from flask import g
from flask import redirect
from decorators import  login_required

question = Blueprint('question',__name__,url_prefix='/')



# 首页
@question.route('/')
def home():
    return render_template('index.html')


@question.route('/question/public')
@login_required
def public_question():
    # 判断是否登录 如果未登录则返回登录界面
    return render_template('question_public.html')

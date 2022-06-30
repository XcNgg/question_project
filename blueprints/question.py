
"""
question.py
    问答平台的首页蓝图文件
"""
import flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from decorators import login_required
from flask import request
from .project_forms import QuestionForm

question = Blueprint('question',__name__,url_prefix='/')



# 首页
@question.route('/')
def home():
    return render_template('index.html')


@question.route('/question/public',methods=["GET","POST"])
@login_required
def public_question():
    if request.method=='GET':
        # 判断是否登录 如果未登录则返回登录界面
        return render_template('question_public.html')
    else:
        pass
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data


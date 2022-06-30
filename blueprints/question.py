"""
question.py
    问答平台的首页蓝图文件
"""
import flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import g
from flask import flash
from decorators import login_required
from flask import request
from flask import url_for
from blueprints.project_forms import QuestionForm
from models import question_models
from project_extension import db

question = Blueprint('question', __name__, url_prefix='/')


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
            question = question_models()
            question.title = title
            question.content = content
            question.author_id = g.user.id
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash("标题或内容格式错误!")
            return redirect(url_for("question.public_question"))

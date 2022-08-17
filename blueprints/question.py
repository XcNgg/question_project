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
    # 读取全部数据并且排序 如果在字段前面加个负号- 则从大到小进行排序
    questions = question_models.query.order_by('create_time').all()
    questions = question_models.query.order_by(db.text('-create_time')).all()
    return render_template('index.html',questions=questions)


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


#
@question.route('/question/<int:question_id>')
def question_detail(question_id):
    question = question_models.query.get(question_id)
    return render_template('detail.html',question=question)

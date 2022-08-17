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
from blueprints.project_forms import AnswerForm
from models import answer_models
#
from sqlalchemy import or_

question = Blueprint('question', __name__, url_prefix='/')


# 首页
@question.route('/')
def home():
    # 读取全部数据并且排序 如果在字段前面加个负号- 则从大到小进行排序
    # questions = question_models.query.order_by('create_time').all()
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


# 指定详情页
@question.route('/question/<int:question_id>')
def question_detail(question_id):
    question = question_models.query.get(question_id)
    return render_template('detail.html', question=question)


@question.route('/answer/<int:question_id>', methods=["post"])
@login_required
def answer(question_id):
    form = AnswerForm(request.form)
    # 如果验证成功
    if form.validate():
        content = form.content.data
        answer_model = answer_models(
            content=content,
            question_id=question_id,
            author=g.user
        )
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for('question.question_detail', question_id=question_id))
    else:
        flash("评论验证失败！最短评论为1个字符")
        return redirect(url_for('question.question_detail', question_id=question_id))


@question.route('/search')
def search():
    # 搜索框的name为 keywords /search?keywords=
    keywords = request.args.get('keywords')
    print(keywords)
    # 对其进行搜索 filter_by 直接使用字段名称
    # filter 使用模型字段名称
    # 导入了一个 or_ 如果问题数据模型的标题或文本内容中包含关键词
    search_question = question_models.query.filter(
        or_(
            question_models.title.contains(keywords),  # 标题内包含keywords
            question_models.content.contains(keywords)  # 问题内包含keywords
        )
    ).order_by(db.text("-create_time"))  # 根据创建的时间进行降序

    return render_template('index.html', questions=search_question)

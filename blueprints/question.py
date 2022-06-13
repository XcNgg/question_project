
"""
question.py
    问答平台的首页蓝图文件
"""
from flask import render_template
from flask import Blueprint


question = Blueprint('question',__name__,url_prefix='/')



# 首页
@question.route('/')
def home():
    return render_template('index.html')

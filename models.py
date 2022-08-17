"""
models.py
    数据库模型文件
"""
from datetime import datetime
# from datetime import timedelta
from project_extension import db
import time
from sqlalchemy.dialects.mysql import FLOAT


# emial验证码存储模型
class email_captcha(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # 邮箱不为空，且唯一
    email = db.Column(db.String(100),nullable=False,unique=True)
    # 验证码不为空，且唯一
    captcha = db.Column(db.String(10),nullable=False,unique=True)
    # 验证码发送时间
    send_time = db.Column(db.Integer,nullable=False)
    # # 验证码有效时间
    valid_time = db.Column(db.Integer,nullable=False)

# 用户存储模型
class users_information(db.Model):
    __tablename__ = 'users_information'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # 用户名不为空，且唯一
    username = db.Column(db.String(20),nullable=False,unique=True)
    # 密码不为空
    password = db.Column(db.String(220),nullable=False)
    # 邮箱不为空
    email = db.Column(db.String(100),nullable=False,unique=True)
    # 注册时间不为空
    regits_time = db.Column(db.DateTime,nullable=False,default=datetime.now)



# 发布问答的模型
class question_models(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('users_information.id'))

    # author 就是 users_information
    author = db.relationship(users_information, backref="question")


# 发布问答数据库模型
class answer_models(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users_information.id'))
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # 两个外键 反向引用2个模型
    # 指定排序方式 order_by=create_time.desc() 从大到小
    question = db.relationship(question_models, backref=db.backref('answers', order_by=create_time.desc()))

    author = db.relationship(users_information, backref='answers')

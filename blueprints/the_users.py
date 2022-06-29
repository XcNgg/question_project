"""
the_users.py
    用户管理的蓝图文件
"""
import time

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import session
from flask import flash


from project_extension import mail
from flask_mail import Message
from models import email_captcha
import string
import random
from flask import request
from datetime import datetime
from project_extension import db
from blueprints.project_forms import RegistForm
from blueprints.project_forms import LoginForm
from models import users_information
# flask 底层的生成加密函数
from werkzeug.security import generate_password_hash
# flask 底层的解密函数
from werkzeug.security import check_password_hash


users = Blueprint('the_users',__name__,url_prefix='/users')

from flask import g
# 登录界面
@users.route('/login',methods=['GET','POST'])
def login():
    # 点击GET请求
    if request.method == 'GET':
        return render_template('login.html')
    # POST 请求
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            # 获取email
            email = form.email.data
            # 获取密码
            password = form.password.data
            user = users_information.query.filter_by(email=email).first()
            # 使用check_password_hash函数来验证密码 函数(hashpassowrd,password)
            if user and check_password_hash(user.password,password):
                session['user_id']=user.id
                return redirect('/')
            else:
                flash('邮箱或密码不匹配!')
                return render_template('login.html')
        else:
            flash("密码格式错误!")
            return render_template('login.html')
            #  jsonify({"error":"邮箱或密码格式错误!"})



# 注册界面
@users.route('/regist',methods=['GET','POST'])
def regist():
    if request.method =='GET':
        return render_template('regist.html')
    elif request.method=='POST':
        # 得到form表单
        form = RegistForm(request.form)
        # 如果验证通过
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user_info = users_information(
                username=username,
                # 密码哈希存储
                password=generate_password_hash(password),
                email=email,
            )
            db.session.add(user_info)
            db.session.commit()
            print("NICE")
            return redirect(url_for("the_users.login"))
        # 如果验证不通过1
        else:
            return redirect(url_for('the_users.regist'))


# 注销清除session
@users.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("the_users.login"))


# 发送验证码
@users.route('/email',methods=['POST'])
def send_email():
    # 验证码随机6位
    captcha = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    #
    # 读取表单内的email值
    recipients = request.form.get('email')

    if not recipients:
        return jsonify({
            "code":400,
            "message":"Miss Email"
        })
    else:
        try:
            message_dict={
                "title":"感谢您的注册", # 邮件标题
                "username":recipients, # 接收者
                "service":"注册用户", # 发送的服务
                "code":captcha, # 验证码
            }
            message= Message(
                recipients=[recipients],# 收件人
                subject='【小草平台】验证码',# 邮件主题
                html=render_template('emialbase.html', **message_dict),  # 邮件内容
                # message.body='邮件内容'# 邮件内容
            )
            # 打印验证码
            # print(captcha)
            # 发送邮件
            mail.send(message)
        except Exception as e:
            print(e)
            return jsonify({
                "code":"400",
                "message":"ERROR"
            })

        # 导入模型
        email_captcha_model = email_captcha.query.filter_by(email=recipients).first()

        # 如果邮箱存在
        if email_captcha_model:
            # 将验证码赋值模型
            email_captcha_model.captcha = captcha
            # 将验证码发送时间赋值模型
            email_captcha_model.send_time = int(time.time())
            # 设置超时时间
            email_captcha_model.valid_time = int(time.time()+300)
            # 提交模型到数据库
            db.session.commit()
        else:
            # 创建模型 赋值
            email_captcha_model = email_captcha()
            email_captcha_model.email = recipients
            email_captcha_model.captcha = captcha
            # 设置发送时间
            email_captcha_model.send_time = int(time.time())
            # 设置超时时间
            email_captcha_model.valid_time = int(time.time()+300)
            # 添加模型
            db.session.add(email_captcha_model)
            # 提交模型到数据库
            db.session.commit()
        return jsonify({
            "code":200,
            "status":"Send captcha Scuccess"
        })


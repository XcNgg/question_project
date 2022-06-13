"""
project_forms.py
    表单文件
"""
import wtforms
from models import  email_captcha
from models import users_information
from wtforms.validators import Length,email,regexp,EqualTo


# 用户注册表单
"""
    以下属性均来自于前端 form 的name 值
"""
class RegistForm(wtforms.Form):

    # 用户名验证
    username = wtforms.StringField(validators=[Length(min=3,max=20,message='用户名长度必须在3-10之间')])
    # 邮箱验证
    email =wtforms.StringField(validators=[email()])
    # 密码验证
    password = wtforms.StringField(validators=[Length(min=8,max=20,message='密码长度必须在8-20之间')])
    # # 确认密码验证
    password_confirm =wtforms.StringField(validators=[EqualTo('password',message='两次密码不一致')])
    # # 验证码
    captcha = wtforms.StringField(validators=[Length(min=6,max=6,message='验证码输入有误！请检查！')])



    # 定一个验证方法
    def validate_captcha(self,filed):
        captcha = filed.data
        email = self.email.data
        captcha_model = email_captcha.query.filter_by(email = email).first()
        if not captcha_model or  captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("邮箱验证码错误！")

    # 定义一个邮箱验证码方法
    def validate_email(self,filed):
        email = filed.data
        user_model = users_information.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError('当前邮箱已经存在！')


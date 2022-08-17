"""
project_forms.py
    表单文件
"""
import wtforms
from models import email_captcha
from models import users_information
from wtforms.validators import Length, email, regexp, EqualTo, InputRequired
import time

# 用户注册表单
class RegistForm(wtforms.Form):
    """
        以下属性均来自于前端 form 的name 值
    """
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
        # 获取当前时间戳
        now_time = int(time.time())
        if now_time < captcha_model.valid_time:
            if not captcha_model or  captcha_model.captcha.lower() != captcha.lower():
                # print("邮箱验证码错误！")
                raise wtforms.ValidationError("邮箱验证码错误！")
        else:
            # print("邮箱验证码超时!")
            raise wtforms.ValidationError("邮箱验证码超时!")
    # 定义一个邮箱验证码方法
    def validate_email(self,filed):
        email = filed.data
        user_model = users_information.query.filter_by(email=email).first()
        if user_model:
            # print('当前邮箱已经存在！')
            raise wtforms.ValidationError('当前邮箱已经存在！')



# 登录表单
class LoginForm(wtforms.Form):
    # 邮箱验证
    email = wtforms.StringField(validators=[email()])
    # 密码验证
    password = wtforms.StringField(validators=[Length(min=8, max=20, message='密码长度必须在8-20之间')])


# 发布问题的表单
class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=200)])
    content = wtforms.StringField(validators=[Length(min=5)])


# 发布评论表单

class AnswerForm(wtforms.Form):
    # # 是否存在输入 InputRequired 问题ＩＤ
    # question_id  =wtforms.IntegerField(validators=[InputRequired()])
    # 评论内容
    content = wtforms.StringField(validators=[Length(min=1)])

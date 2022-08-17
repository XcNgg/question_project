"""
app.py
    app文件
"""
from flask import Flask
from flask import session
from models import  users_information
# 蓝图
from blueprints import users_bp
from blueprints import question_bp
# 扩展绑定
from project_extension import db
from project_extension import mail
# db
from flask_migrate import Migrate
from  flask import  g





app = Flask(__name__)
app.config.from_object('config')
# 将db绑定在app上
db.init_app(app)
# 将mail绑定在app上
mail.init_app(app)

app.register_blueprint(users_bp)
app.register_blueprint(question_bp)

# ORM映射
migrate = Migrate(app, db)


#每次请求前
@app.before_request
def before_requests():
    user_id = session.get('user_id')
    if user_id:
        try:
            user = users_information.query.get(user_id)
            # setattr给什么属性绑定什么变量
            # 给g绑定一个叫做user的变量，他的值是user这个变量
            # 此时的g是全局变量
            setattr(g,'user',user) # 等于  g.user= user
        except:
            g.user = None # 等于 setattr(g,'user',None)



# 请求来了 -> beforr_request -> 视图函数 -> 视图函数中返回模板 -> context_processor
# 上下文处理器
@app.context_processor
# 当渲染的所有网站都会执行以下的代码
def context_processor():
    if hasattr(g,"user"):
        return  {"user":g.user}
    else:
        return {}
    #



if __name__ == '__main__':
    app.run(host='0.0.0.0')

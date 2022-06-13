"""
app.py
    app文件
"""
from flask import Flask
# 蓝图
from blueprints import users_bp
from blueprints import question_bp
# 扩展绑定
from project_extension import db
from project_extension import mail
# db
from flask_migrate import Migrate




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



if __name__ == '__main__':
    app.run()

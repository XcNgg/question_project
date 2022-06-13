"""
blueprints.__init__.py
    导入蓝图文件夹内的文件
    方便在app.py中直接导入蓝图
"""
from .question import question as question_bp
from .the_users import users as users_bp
from .project_forms import RegistForm
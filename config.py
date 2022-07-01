"""
config.py
    配置文件,配置app信息
"""

"""
FLASK问答平台，知了传课学习仿写：https://www.bilibili.com/video/BV17r4y1y7jJ?p=31&vd_source=5fce51f437b997bc2572736f7abf0efc
"""

"""
    MySQL配置
    HOSTNAME="192.168.200.140"
    PORT=3306
    DATABASE="question_project"
    PASSWORD="zYjWbRHzD7RGYh7y"
    DB_URI="mysql+pymysql://root:{}@{}:{}/{}?charset=utf8".format(PASSWORD,HOSTNAME,PORT,DATABASE)
    SQLALCHEMY_DATABASE_URI=DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY="XcNgg_question_project_@2022"
"""

# todo FLASK MYSQL
MYSQLCONFIG = {
    "HOSTNAME": "203.25.208.205",
    "PORT": 3306,
    "USERNAME": "question_project",
    "PASSWORD": "zD6sj5dGfJwDHEDX",
    "DATABASE": "question_project"
}

# 设置DB_URI
DB_URI = "mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8".format(**MYSQLCONFIG)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "XcNgg_question_project_@2022"
# print(DB_URI)


""" 邮箱验证配置
MAIL_SERVER : 默认为 ‘localhost’
MAIL_PORT : 默认为 25
MAIL_USE_TLS : 默认为 False
MAIL_USE_SSL : 默认为 False
MAIL_DEBUG : 默认为 app.debug
MAIL_USERNAME : 默认为 None
MAIL_PASSWORD : 默认为 None
MAIL_DEFAULT_SENDER : 默认为 None
MAIL_MAX_EMAILS : 默认为 None
MAIL_SUPPRESS_SEND : 默认为 app.testing
MAIL_ASCII_ATTACHMENTS : 默认为 False
"""
# 服务器地址
MAIL_SERVER = "smtp.qq.com"
# 端口
MAIL_PORT = 465
#
MAIL_USE_TLS = False
#
MAIL_USE_SSL = True
# 如果后续部署,需要更改为False
MAIL_DEBUG = True
#邮箱账号 STMP密钥
MAIL_USERNAME = "1355523280@qq.com"
MAIL_PASSWORD = "ojavkiizqurlibgj"
#默认发件人
MAIL_DEFAULT_SENDER ="1355523280@qq.com"
#
# MAIL_MAX_EMAILS =
#
# MAIL_SUPPRESS_SEND
#
# MAIL_ASCII_ATTACHMENTS
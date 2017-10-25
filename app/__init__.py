from flask import Flask
from configs import DevConfig
from app.api_1_0 import api as api_blueprint
from app.api_1_0.auth import auth as auth_blueprint
from exts import db, mail
from app.uploads import uploads as uploads_blueprint


def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(DevConfig)
    # 初始化插件
    # 数据库
    db.init_app(app)
    mail.init_app(app)
    # 注册蓝图
    # 基础api 蓝图
    app.register_blueprint(api_blueprint)
    # 登陆 注册相关的蓝图
    app.register_blueprint(auth_blueprint)
    # 访问上传文件的蓝图
    app.register_blueprint(uploads_blueprint)
    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(config_overrides=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"  # 默认使用SQLite数据库
    
    # 如果提供了 config_overrides，则更新配置
    if config_overrides:
        app.config.update(config_overrides)

    # 加载模型
    from todo.models import db
    from todo.models.todo import Todo
    db.init_app(app)

    # 创建数据库表
    with app.app_context():
        db.create_all()
        db.session.commit()

    # 注册蓝图
    from todo.views.routes import api
    app.register_blueprint(api)

    return app


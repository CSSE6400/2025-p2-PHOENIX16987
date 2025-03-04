from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    
    # 配置 SQLite 数据库的 URI
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    
    # 导入数据库对象
    from todo.models import db
    from todo.models.todo import Todo
    
    # 初始化数据库
    db.init_app(app)

    # 创建数据库表
    with app.app_context():
        db.create_all()
        db.session.commit()

    # 注册 API 路由
    from todo.views.routes import api
    app.register_blueprint(api)

    return app

import datetime
from . import db

class Todo(db.Model):
    __tablename__ = 'todos'

    # 定义数据库列
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(80), nullable=False)  # 必填字段，最长 80 个字符
    description = db.Column(db.String(120), nullable=True)  # 可选字段，最长 120 个字符
    completed = db.Column(db.Boolean, nullable=False, default=False)  # 默认未完成
    deadline_at = db.Column(db.DateTime, nullable=True)  # 任务截止日期
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)  # 默认当前时间
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )  # 每次更新都会自动更新时间戳

    # 将模型转换为字典的方法
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'deadline_at': self.deadline_at.isoformat() if self.deadline_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    def __repr__(self):
        return f'<Todo {self.id} {self.title}>'

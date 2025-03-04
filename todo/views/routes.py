from flask import Blueprint, jsonify, request
from todo.models import db
from todo.models.todo import Todo
from datetime import datetime

 
api = Blueprint('api', __name__, url_prefix='/api/v1') 

TEST_ITEM = {
    "id": 1,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2023-02-27T00:00:00",
    "created_at": "2023-02-20T00:00:00",
    "updated_at": "2023-02-20T00:00:00"
}
 
@api.route('/health') 
def health():
    """Return a status of 'ok' if the server is running and listening to request"""
    return jsonify({"status": "ok"})


@api.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()  # 从数据库中获取所有 Todo 记录
    result = []  # 创建一个空列表，用于存储每个 Todo 对象的字典格式

    for todo in todos:
        result.append(todo.to_dict())  # 将每个 Todo 对象转换为字典，并添加到 result 列表中
    
    return jsonify(result)  # 将 result 列表作为 JSON 响应返回


@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)  # 根据传入的 todo_id 从数据库中获取指定的 Todo 记录
    if todo is None:  # 如果没有找到对应的 Todo 记录
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo.to_dict())  


@api.route('/todos', methods=['POST'])
def create_todo():
    todo = Todo(
        title=request.json.get('title'),
        description=request.json.get('description'),
        completed=request.json.get('completed', False),
    )
    if 'deadline_at' in request.json:
        todo.deadline_at = datetime.fromisoformat(request.json.get('deadline_at'))
    
    # 添加新记录到数据库或更新现有记录
    db.session.add(todo)
    # 提交数据库更改
    db.session.commit()
    
    return jsonify(todo.to_dict()), 201


@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    
    todo.title = request.json.get('title', todo.title)
    todo.description = request.json.get('description', todo.description)
    todo.completed = request.json.get('completed', todo.completed)
    todo.deadline_at = request.json.get('deadline_at', todo.deadline_at)
    
    db.session.commit()
    return jsonify(todo.to_dict())


@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo item and return the deleted item"""
    return jsonify(TEST_ITEM)
 

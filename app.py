# app.py
from flask import Flask, request, jsonify
from pony.orm import db_session, select
import jwt
import datetime
from models import db, User, Checklist, Item
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Decorator untuk memeriksa token JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.get(username=data['username'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)
    return decorated

# API untuk login
@app.route('/login', methods=['POST'])
@db_session
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get(username=username)
    if user and user.password == password:
        token = jwt.encode({
            'username': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials!'}), 401

# API untuk mendaftar user baru
@app.route('/register', methods=['POST'])
@db_session
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.get(username=username):
        return jsonify({'message': 'User already exists!'}), 400

    User(username=username, password=password)
    return jsonify({'message': 'User registered successfully!'}), 201

# API untuk membuat checklist
@app.route('/checklist', methods=['POST'])
@token_required
@db_session
def create_checklist(current_user):
    data = request.get_json()
    title = data.get('title')

    Checklist(title=title, user=current_user)
    return jsonify({'message': 'Checklist created successfully!'}), 201

# API untuk menampilkan semua checklist
@app.route('/checklists', methods=['GET'])
@token_required
@db_session
def get_checklists(current_user):
    checklists = select(c for c in Checklist if c.user == current_user)[:]
    return jsonify([{'id': c.id, 'title': c.title} for c in checklists])

# API untuk membuat item di dalam checklist
@app.route('/checklist/<int:checklist_id>/item', methods=['POST'])
@token_required
@db_session
def create_item(current_user, checklist_id):
    data = request.get_json()
    description = data.get('description')

    checklist = Checklist.get(id=checklist_id, user=current_user)
    if not checklist:
        return jsonify({'message': 'Checklist not found!'}), 404

    Item(description=description, checklist=checklist)
    return jsonify({'message': 'Item created successfully!'}), 201

# API untuk mengubah status item
@app.route('/item/<int:item_id>/complete', methods=['PUT'])
@token_required
@db_session
def complete_item(current_user, item_id):
    item = Item.get(id=item_id, checklist__user=current_user)
    if not item:
        return jsonify({'message': 'Item not found!'}), 404

    item.completed = True
    return jsonify({'message': 'Item marked as completed!'})

# API untuk menghapus item
@app.route('/item/<int:item_id>', methods=['DELETE'])
@token_required
@db_session
def delete_item(current_user, item_id):
    item = Item.get(id=item_id, checklist__user=current_user)
    if not item:
        return jsonify({'message': 'Item not found!'}), 404

    item.delete()
    return jsonify({'message': 'Item deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
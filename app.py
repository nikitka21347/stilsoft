import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


USERS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'root',
        'author': 'admin',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'admin',
        'author': 'nimda',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': '1234',
        'author': '4321',
        'read': True
    }
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in USERS:
        if book['id'] == book_id:
            USERS.remove(book)
            return True
    return False


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        USERS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Пользователь добавлен!'
    else:
        response_object['books'] = USERS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        USERS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Пользователь обновлен!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Пользователь удален!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
from flask import Flask
from services import get_github_user

app = Flask(__name__)


@app.route('/users/', methods=['GET'], defaults={'username': None})
@app.route('/users/<username>', methods=['GET'])
def user_info(username):
    if not username:
        return {'error': 'Usuario nao informado'}, 400
    return get_github_user(username)
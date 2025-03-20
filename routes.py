from flask import Flask, jsonify
from services import get_github_user

app = Flask(__name__)

@app.route('/user/<username>', methods = ['GET'])
def user_info(username):
    data, status = get_github_user(username)
    return jsonify(data), status
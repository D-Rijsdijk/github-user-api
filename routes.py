from flask import Flask, jsonify
from services import get_github_user, get_user_repos

app = Flask(__name__)

@app.route('/user/<username>', methods = ['GET'])
def user_info(username):
    data, status = get_github_user(username)
    return jsonify(data), status

@app.route('/user/<username>/repos', methods = ['GET'])
def user_repos(username):
    data, status = get_user_repos(username)
    return jsonify(data), status
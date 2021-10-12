import random
from random import randrange
from flask import Flask, app
from flask.json import jsonify
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Here</h1>', 404

@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>Something is Broke</h1>', 500


@app.route('/pong', methods=['GET'])
@auth.login_required
def pong():
    number = random.randrange(1000000)
    return jsonify({"random_int" : number}), 201

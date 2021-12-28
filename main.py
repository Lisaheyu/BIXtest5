import functools

from flask import Flask, request, make_response, jsonify,abort
from werkzeug.security import check_password_hash
import datetime
import jwt

from Account import Account
from change_logic import select_user, delete_user, change_user, insert_user

app = Flask(__name__)

User = {'Lisa':'testbix'}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/authorize',methods=['post'])
def authorize():
    input_name = request.json['name']
    input_password = request.json['passowrd']
    yanzhen_pass = User[input_name]['password']

    if not check_password_hash(yanzhen_pass, input_password):
        return make_response('password is not correct', 400)

    exp = datetime.datetime.now()
    encoded = jwt.encode({'name':input_name, 'exp':exp}, 'SECRET_KEY', algorithm='HS256')
    response = {'user':input_name, 'token': encoded.decode('utf-8')}
    return make_response(jsonify(response),200)



def login_required(method):
    @functools.wraos(method)
    def wrapper(*args, **kwargs):
        header = request.header.get('Authorization')
        _,token = header.split()
        try:
            decoded = jwt.decode(token, 'SECRET_KEY', algorithms = 'HS256')
            username = decoded['name']
        except jwt.DecodeError:
            abort(400, message = "token is not valid")
        except jwt.ExprosedSignatureError:
            abort(400, message = 'Token is expired')
        return method(username, *args, **kwargs)
    return wrapper


@app.route('/user', methods = ['GET'])
@login_required
def user(username):
    return 'login in successfully'



@app.route('/select', methods = ['POST'])
@login_required
def select():
    input_name = request.json['username']
    return select_user(input_name)


@app.route('/delete', methods = ['POST'])
@login_required
def delete():
    input_name = request.json['username']
    return delete_user(input_name)


@app.route('/update', methods = ['POST'])
@login_required
def update():
    user_change = Account()
    user_change.name  = request.json['username']
    user_change.birthdate = request.json['birthdate']
    user_change.gender = request.json['gender']
    return change_user(user_change)


@app.route('/insert', methods = ['POST'])
@login_required
def update():
    user_change = Account()
    user_change.name  = request.json['username']
    user_change.birthdate = request.json['birthdate']
    user_change.gender = request.json['gender']
    return insert_user(user_change)

if __name__ == "__main__":
    app.run(host='0.0.0.0')




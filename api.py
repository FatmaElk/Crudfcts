from crypt import methods
from distutils.log import debug
from unicodedata import name
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer)

def __init__(self, id, firstname, lastname, age):
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.age = age

@app.route('/users', methods=['GET'])
def get_all_users():
    # GET http://localhost:5000/user
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname
        user_data['age'] = user.age
        output.append(user_data)
    return jsonify({'users' : output})

@app.route('/user/<id>', methods=['GET'])
def get_single_user(id):
    #GET http://localhost:5000/user/1
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})
    else:
        user_data = {}
        user_data['id'] = user.id
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname
        user_data['age'] = user.age
        return jsonify({'user': user_data})

@app.route('/user', methods=['POST'])
def create_user():
    # POST http://localhost:5000/user
    # {"id": 1, "firstname" : "Charelotte", "lastname" : "Linlin" , "age" : 70 }
    new_user = User(id=request.json['id'], firstname=request.json['firstname'], lastname=request.json['lastname'], age=request.json['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@app.route('/user/<id>', methods=['PUT'])
def update_user_age(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})
    else:
        #update_user = User(user.id, user.firstname, user.lastname, age=request.json['age'])
        #db.session.add(update_user)
        user.age = 100
        db.session.commit()
        return jsonify({'message': 'User age updated!'})

@app.route('/user/<id>', methods=['DELETE'])
def remove_user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message' : 'No user found!'})
    else:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message' : 'User deleted!'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create database
db = SQLAlchemy(app)

# initialize marshmallow
ma = Marshmallow(app)

@app.route('/', methods=['GET'])
def get():
    return jsonify({
        'msg': 'intial message'
    })

# start server
if __name__ == '__main__':
    app.run(debug=True)
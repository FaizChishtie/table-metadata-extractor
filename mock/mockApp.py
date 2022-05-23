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

# mock data model
class MockData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    number = db.Column(db.Float)

    def __init__(self, id, name, description, number):
        self.id = id
        self.name = name
        self.description = description
        self.number = number

# mock data schema
class MockDataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'number')

# intialize mock data schema
mockdata_schema = MockDataSchema()

@app.route('/', methods=['POST'])
def post_mockdata():
    id = request.json['id']
    name = request.json['name']
    description = request.json['description']
    number = request.json['number']

    new_mockdata = MockData(id, name, description, number)

    db.session.add(new_mockdata)
    db.session.commit()

    return mockdata_schema.jsonify(new_mockdata)

# start server
if __name__ == '__main__':
    app.run(debug=True)
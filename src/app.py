from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# initialize app
app = Flask(__name__)

# start server
if __name__ == '__main__':
    app.run(debug=True)
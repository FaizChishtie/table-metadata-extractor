from flask import Flask, request, jsonify
from sqlalchemy import MetaData, create_engine
import json

import os

# initialize app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['POST'])
def findTableMetadata():
    uri = request.json['uri']

    tmp_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

    connection = create_engine(tmp_uri)

    print(connection.table_names())

    metadata = MetaData(bind=connection)

    metadata.reflect()

    return jsonify({
        'metadata': list(metadata.tables.keys())
    })

# start server
if __name__ == '__main__':
    app.run(debug=True)
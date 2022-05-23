from flask import Flask, request, jsonify
from sqlalchemy import MetaData, create_engine, inspect
from src.models.TableMetadata import TableMetadata
import json

# initialize app
app = Flask(__name__)

@app.route('/', methods=['POST'])
def retrieve_table_metadata():
    uri = request.json['uri']

    # todo validate URI
    connection = create_engine(uri)

    metadata = create_metadata_object(connection)

    inspector = inspect(connection)

    # for table in inspector.get_table_names():
    #     print(inspector.get_columns(table))

    tables = get_table_metadata(metadata)

    return jsonify(tables)

def create_metadata_object(connection):
    metadata = MetaData(bind=connection)
    metadata.reflect()
    return metadata

def get_table_metadata(metadata):
    tables = []
    for key in metadata.tables.keys():
        tablemetadata_obj = TableMetadata.create_table_from_metadata(metadata.tables[key])
        tables.append(tablemetadata_obj.to_dict())
    
    return tables


# start server
if __name__ == '__main__':
    app.run(debug=True)
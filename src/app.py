from flask import Flask, request, jsonify
from sqlalchemy import MetaData, create_engine, inspect, func, text
from sqlalchemy.orm import sessionmaker
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

    session = sessionmaker(bind=connection)
    session = session()

    tables = get_table_metadata(metadata, uri, session)

    session.close()

    return jsonify(tables)

def create_metadata_object(connection):
    metadata = MetaData(bind=connection)
    metadata.reflect()
    return metadata

def get_table_metadata(metadata, uri, session):
    tables = []
    for key in metadata.tables.keys():
        num_rows = get_number_of_rows(metadata.tables[key], session)
        # last_modified = get_last_modified(metadata.tables[key].name, engine)
        tablemetadata_obj = TableMetadata.create_table_from_metadata(metadata.tables[key], uri, num_rows)
        tables.append(tablemetadata_obj.to_dict())
    
    return tables

def get_number_of_rows(table, session):
    return session.query(func.count(table.c.id)).scalar()

def get_last_modified(table, engine):
    sql = text(f'SELECT {table}, [modify_date] FROM sys.tables')
    return engine.execute(sql)

# start server
if __name__ == '__main__':
    app.run(debug=True)
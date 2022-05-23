import json
from src.models.ColumnMetadata import ColumnMetadata

Columns = list[ColumnMetadata]

class TableMetadata():
    # todo make serializable

    def __init__(self, columns: Columns, num_rows: int, last_updated: str, schema: str, database: str, name: str):
        self.columns = columns
        self.num_rows = num_rows
        self.last_updated = last_updated
        self.schema = schema
        self.database = database
        self.name = name
    
    @staticmethod
    def create_table_from_metadata(table_metadata):
        name = table_metadata.name
        schema = table_metadata.schema
        num_rows = 0
        database = "database"
        last_updated = "lu"
        columns = []

        for c in table_metadata.c:
            column_metadata = ColumnMetadata.create_column_from_metadata(c)
            columns.append(column_metadata)

        return TableMetadata(columns, num_rows, last_updated, schema, database, name)

    def __repr__(self):
        col_string = ''
        for c in self.columns:
            col_string += ', ' + str(c)

        return f'<TableMetadata {self.name}, {self.schema}, {self.num_rows}, {self.database}, {self.last_updated}{col_string}>'
    
    def to_dict(self):
        to_return = {"name": self.name, "schema": self.schema, "num_rows": str(self.num_rows), "database": self.database, "last_updated": self.last_updated}
        cols = []
        for col in self.columns:
            cols.append(col.to_dict())

        to_return["columns"] = cols
        return to_return
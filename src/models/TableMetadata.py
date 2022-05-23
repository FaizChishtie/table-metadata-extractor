from ColumnMetadata import ColumnMetadata

Columns = list[ColumnMetadata]

class TableMetadata():
    # todo make serializable

    def __init__(self, columns: Columns, num_rows: int, last_updated: str, schema: str, database: str):
        self.columns = columns
        self.num_rows = num_rows
        self.last_updated = last_updated
        self.schema = schema
        self.database = database
    
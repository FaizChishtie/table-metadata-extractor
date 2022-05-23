import json

class ColumnMetadata():
    def __init__(self, col_name: str, col_type: str):
        self.col_name = col_name
        self.col_type = col_type

    def __iter__(self):
        yield from {
            "col_name": self.col_name,
            "col_type": self.col_type,
        }.items()

    @staticmethod
    def create_column_from_metadata(column_metadata):
        col_name = column_metadata.name
        col_type = column_metadata.type

        return ColumnMetadata(col_name, col_type)

    def __repr__(self):
        return f'<ColumnMetadata {self.col_name}, {self.col_type}>'
    
    def to_dict(self):
        return {"col_name" : str(self.col_name), "col_type": str(self.col_type)}

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
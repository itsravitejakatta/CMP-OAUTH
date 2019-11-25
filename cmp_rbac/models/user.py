import flask_restplus
import sqlalchemy

from cmp_rbac import DB


# For SQLAlchemy
class UserDB(DB.Model):
    """
    user table
    """

    __tablename__ = 'user'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    # made user name as unique
    name = DB.Column(DB.String(100), unique=True)
    age = DB.Column(DB.Integer)
    gender = DB.Column(DB.String(10))

    def __repr__(self):
        return '<User: {}>'.format(self.name)


# For flask_restplus
api_model = {
    'id': flask_restplus.fields.Integer(required=False, description='user id'),
    'name': flask_restplus.fields.String(required=True, description='user Name'),
    'age': flask_restplus.fields.Integer(required=True, description='user age'),
    'gender': flask_restplus.fields.String(required=True, description='user gender'),

}

# For validation
json_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "required": [
        "name",
        "age",
        "gender"
    ],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string",
            "pattern": "^[A-Za-z0-9-_.@]+$"
        },
        "age": {
            "type": "integer"
        },
        "gender": {
            "type": "string",
            #gender accepts only two strings
            "enum": ["male", "female"]

        }
    },
    "type": "object"
}

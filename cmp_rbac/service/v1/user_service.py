import jsonschema
from cmp_rbac.models.user import UserDB
from cmp_rbac import DB
import cmp_rbac.models.user

user_json_schema = cmp_rbac.models.user.json_schema


def get_all_users():
    return UserDB.query.all()


def add_user(data):
    if 'id' in data:
        del(data['id'])

    if data["name"]:
        data["name"] = (data["name"]).lower()

    jsonschema.validate(data, user_json_schema)

    new_user = UserDB(**data)

    DB.session.add(new_user)
    DB.session.commit()

    return "Thank you for your submission. You are a age {} old gender {} named {}".format(
        new_user.age,
        new_user.gender,
        new_user.name
    )


def update_user(id, data):
    if not isinstance(id, int):
        raise ValueError("User ID must be an int.")

    jsonschema.validate(data, user_json_schema)

    user = UserDB.query.filter_by(id=id).first()

    if not user:
        raise ValueError("No user with id: {}".format(id))

    user.name = (data['name']).lower()
    user.age = data['age']
    user.gender = data['gender']

    DB.session.add(user)
    DB.session.commit()
    return "{} is {} year old {} and updated as new user successfully.".format(
        user.name,
        user.age,
        user.gender
    )


def delete_user(id):
    if not isinstance(id, int):
        raise ValueError("User ID must be an int.")

    user = UserDB.query.filter_by(id=id).first()

    if not user:
        raise ValueError("No user with id: {}".format(id))

    DB.session.delete(user)
    DB.session.commit()
    return "User having id:{} deleted successfully.".format(
        id
    )

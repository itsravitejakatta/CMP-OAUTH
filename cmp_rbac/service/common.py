import datetime
import logging

import flask

LOGGER = logging.getLogger()


def get_return_envelope(success="true", message="", data={}):
    envelope = {
        "success": success,
        "message": message,
        "data": data
    }
    return envelope


def get_post_data(required_fields, non_required_fields=[]):
    data = flask.request.get_json()
    if not data:
        raise ValueError(
            "This requires a 'Content-Type: application/json header."
        )

    missing_fields = []
    fields = {}
    for field in required_fields:
        field = field.lower()
        if field not in data:
            missing_fields.append(field)
            continue

        fields[field] = data[field]

    for field in non_required_fields:
        field = field.lower()
        if field in data:
            fields[field] = data[field]

    if len(missing_fields):
        raise ValueError(
            "Missing required fields '%s' in POST JSON data." %
            str(missing_fields)
        )

    return fields

def get_current_datetime():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

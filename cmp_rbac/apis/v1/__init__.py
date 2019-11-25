import logging
import flask
import flask_restplus
from cmp_rbac.service import common
from cmp_rbac.apis.v1.users import api as user_ns
blueprint = flask.Blueprint('v1_api', __name__, url_prefix='/api/v1')
api = flask_restplus.Api(blueprint,
                         version='1.0',
                         title='CMP',
                         description='Handles the APIs for CMP'
)


api.add_namespace(user_ns)

LOGGER = logging.getLogger()

@api.errorhandler(ValueError)
def handle_valueerror_exception(error):
    """
    Flask error handler for ValueError.
    :param error: error message
    :return: tuple (return envelope string. http status code int)
    :rtype: tuple(str, int)
    """
    envelope = common.get_return_envelope(
        success="false",
        message=str(error)
    )
    LOGGER.exception(str(error))

    return envelope, 400


@api.errorhandler(Exception)
def handle_general_exception(error):
    """
    Flask error handler for exception
    :param error: error message
    :return: tuple(return envelope string, http status code int)
    :rtype: tuple(str, int)
    """
    envelope = common.get_return_envelope(
        success="false",
        message=str(error)
    )
    LOGGER.exception(str(error))

    return envelope, 500



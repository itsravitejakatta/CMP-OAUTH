import logging
import flask
import flask_restplus

from cmp_rbac import app
from .v1 import blueprint as v1_blueprint

blueprint = flask.Blueprint('api', __name__, url_prefix='/api')
api = flask_restplus.Api(
    blueprint,
    title='Magic Manager',
    version='1.0',
    description='Magic Manager'
)

app.register_blueprint(v1_blueprint, url_prefix='/api/v1')
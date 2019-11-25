import flask
import flask_cors
import flask_sqlalchemy
import flask_migrate
import werkzeug.contrib.fixers
from cmp_rbac import log
import os
from collections import ChainMap
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, UserMixin, RoleMixin, utils
import requests
import json
from cmp_rbac.models.rbac import Userrole, Role
from cmp_rbac.models import DB
# configure logging before flask app is initialized so it uses that format.
# Otherwise, it creates a default handler.
log.log_init()

app = flask.Flask(__name__, instance_relative_config=True)
flask_cors.CORS(app)
app.wsgi_app = werkzeug.contrib.fixers.ProxyFix(app.wsgi_app)

#TODO: This needs to get moved somewhere else.

defaults = {'dbuser': 'magic_master',
            'dbpassword': '3e532292-75a3-459c-854a-edd2fad90f80',
            'dbhost': 'dev-png-magic-db.cluster-c9s6igb3qixu.us-west-2.rds.amazonaws.com',
            'dbport': '3306',
            'dbschema': 'rbac'
            }

envconfig = ChainMap(os.environ, defaults)

mysql_uri = "mysql://{}:{}@{}:{}/{}".format(
    envconfig.get('dbuser'),
    envconfig.get('dbpassword'),
    envconfig.get('dbhost'),
    envconfig.get('dbport'),
    envconfig.get('dbschema')
)

app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60
# DB = flask_sqlalchemy.SQLAlchemy(app)
# migrate = flask_migrate.Migrate(app, DB)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_TOKEN_MAX_AGE'] = 600


#DB = flask_sqlalchemy.SQLAlchemy(app)
DB.init_app(app)
migrate = flask_migrate.Migrate(app, DB)


# roles_users = DB.Table('roles_users',
#                        DB.Column('user_id', DB.Integer(), DB.ForeignKey('userrole.id')),
#                        DB.Column('role_id', DB.Integer(), DB.ForeignKey('role.id')))
#
#
# class Role(DB.Model, RoleMixin):
#     id = DB.Column(DB.Integer(), primary_key=True)
#     name = DB.Column(DB.String(80), unique=True)
#     description = DB.Column(DB.String(255))
#
#
# class Userrole(DB.Model, UserMixin):
#     id = DB.Column(DB.Integer, primary_key=True)
#     email = DB.Column(DB.String(255), unique=True)
#     password = DB.Column(DB.String(255))
#     active = DB.Column(DB.Boolean())
#     confirmed_at = DB.Column(DB.DateTime())
#     roles = DB.relationship('Role', secondary=roles_users,
#                             backref=DB.backref('users', lazy='dynamic'))
#
#
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(DB, Userrole, Role)
security = Security(app, user_datastore)
#

# Create a user to test with
@app.before_first_request
def create_user():
    DB.create_all()

    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')

    encrypted_password = utils.encrypt_password('password')
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(email='someone@example.com', password=encrypted_password)
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(email='admin@example.com', password=encrypted_password)

    DB.session.commit()

    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'admin')
    DB.session.commit()


# #Views
# import pdb; pdb.set_trace()
@app.route('/')
@login_required
def home():
    return render_template('index.html')



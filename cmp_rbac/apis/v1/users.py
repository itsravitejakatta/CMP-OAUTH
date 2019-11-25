import flask
import flask_restplus

from cmp_rbac.service import common
from flask import render_template
from cmp_rbac.service.v1 import user_service
from cmp_rbac import app
import cmp_rbac.models.user
from flask_security import roles_required, auth_token_required, login_required

api = flask_restplus.Namespace('user', description='User Details')

user_api_model = api.model('user', cmp_rbac.models.user.api_model)

# @app.route('/')
# @login_required
# def home():
#     return render_template('index.html')

@api.route('/user_details')
@api.response(500, 'Something went wrong.')
class UserView(flask_restplus.Resource):
    @api.doc('Lists all users')
    @api.response(200, 'User Data')
    # @auth_token_required
    # @roles_required('admin')
    # @roles_required('end-user')
    def get(self):
        return common.get_return_envelope(
            data=api.marshal(user_service.get_all_users(), user_api_model)
        ), 200

    @api.doc('Creates new user.')
    @api.response(200, 'User data')
    @api.response(400, 'Failed to add User')
    @api.expect(user_api_model, validate=True)
    @roles_required('admin')
    def post(self):
        data = flask.request.json
        return common.get_return_envelope(
            message=user_service.add_user(data=data)
        ), 201


@api.route('/<int:id>')
@api.response(404, 'User not found.')
@api.response(500, 'Something went wrong.')
class UserUpdate(flask_restplus.Resource):
    @api.doc('Deletes user by ID')
    @api.response(202, 'User Deleted Successfully')
    @api.response(400, 'Failed to delete User')
    @roles_required('admin')
    def delete(self, id):
        return common.get_return_envelope(
            message=user_service.delete_user(id)
        ), 200

    @api.doc('Update user by ID')
    @api.response(201, 'User Updated Successfully')
    @api.response(400, 'Failed to update User')
    @api.expect(user_api_model, validate=True)
    @roles_required('admin')
    def put(self, id):
        data = flask.request.json
        return common.get_return_envelope(
            message=user_service.update_user(id, data)
        ), 201

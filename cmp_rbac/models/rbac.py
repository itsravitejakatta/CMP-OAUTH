from flask_security import UserMixin, RoleMixin
from cmp_rbac.models import DB

roles_users = DB.Table('roles_users',
                       DB.Column('user_id', DB.Integer(), DB.ForeignKey('userrole.id')),
                       DB.Column('role_id', DB.Integer(), DB.ForeignKey('role.id')))


class Role(DB.Model, RoleMixin):
    id = DB.Column(DB.Integer(), primary_key=True)
    name = DB.Column(DB.String(80), unique=True)
    description = DB.Column(DB.String(255))


class Userrole(DB.Model, UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(255), unique=True)
    password = DB.Column(DB.String(255))
    active = DB.Column(DB.Boolean())
    confirmed_at = DB.Column(DB.DateTime())
    roles = DB.relationship('Role', secondary=roles_users,
                            backref=DB.backref('users', lazy='dynamic'))



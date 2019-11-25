"""empty message

Revision ID: 19de42497f0d
Revises: 
Create Date: 2019-01-16 20:52:31.003079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19de42497f0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('userrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['userrole.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('userrole')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
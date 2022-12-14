"""empty message

Revision ID: 502ab9f7ffae
Revises: 
Create Date: 2022-12-10 14:45:06.741417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '502ab9f7ffae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.Column('rotation', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planets_id', sa.Integer(), nullable=False),
    sa.Column('charancteres_id', sa.Integer(), nullable=False),
    sa.Column('vehicles_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charancteres_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicles_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('vehicles')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###

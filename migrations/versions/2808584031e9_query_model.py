"""query model

Revision ID: 2808584031e9
Revises: 232613356081
Create Date: 2014-11-14 14:21:41.902869

"""

# revision identifiers, used by Alembic.
revision = '2808584031e9'
down_revision = '232613356081'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_query',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('query_string', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('querytoken', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_query')
    ### end Alembic commands ###

"""empty message

Revision ID: ac0d73a95c0a
Revises: cc6c2a3152bd
Create Date: 2016-07-29 21:54:12.780000

"""

# revision identifiers, used by Alembic.
revision = 'ac0d73a95c0a'
down_revision = 'cc6c2a3152bd'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('zipcode', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'zipcode')
    ### end Alembic commands ###

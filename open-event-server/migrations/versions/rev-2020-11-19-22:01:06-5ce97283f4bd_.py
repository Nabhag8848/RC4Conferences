"""empty message

Revision ID: 5ce97283f4bd
Revises: 74a148c0100d
Create Date: 2020-11-19 22:01:06.632440

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '5ce97283f4bd'
down_revision = '74a148c0100d'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('microlocations', sa.Column('position', sa.Integer(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('microlocations', 'position')
    # ### end Alembic commands ###

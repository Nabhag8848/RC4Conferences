"""empty message

Revision ID: 5d4c7b24818d
Revises: b006b725586f
Create Date: 2018-07-16 21:46:14.932695

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '5d4c7b24818d'
down_revision = 'b006b725586f'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_system_role', sa.Column('event_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_system_role', 'events', ['event_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_system_role', type_='foreignkey')
    op.drop_column('user_system_role', 'event_id')
    # ### end Alembic commands ###

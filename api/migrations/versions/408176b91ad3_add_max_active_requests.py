"""'add_max_active_requests'

Revision ID: 408176b91ad3
Revises: 7e6a8693e07a
Create Date: 2024-07-04 09:25:14.029023

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = '408176b91ad3'
down_revision = '161cadc1af8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('max_active_requests', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.drop_column('max_active_requests')

    # ### end Alembic commands ###

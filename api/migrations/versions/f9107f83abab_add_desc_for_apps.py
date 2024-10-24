"""add desc for apps

Revision ID: f9107f83abab
Revises: cc04d0998d4d
Create Date: 2024-02-28 08:16:14.090481

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f9107f83abab'
down_revision = 'cc04d0998d4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), server_default=sa.text("''::character varying"), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###

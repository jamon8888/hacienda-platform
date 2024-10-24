"""add use_icon_as_answer_icon fields for app and site

Revision ID: 030f4915f36a
Revises: d0187d6a88dd
Create Date: 2024-09-01 12:55:45.129687

"""

import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = "030f4915f36a"
down_revision = "d0187d6a88dd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("apps", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("use_icon_as_answer_icon", sa.Boolean(), server_default=sa.text("false"), nullable=False)
        )

    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("use_icon_as_answer_icon", sa.Boolean(), server_default=sa.text("false"), nullable=False)
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.drop_column("use_icon_as_answer_icon")

    with op.batch_alter_table("apps", schema=None) as batch_op:
        batch_op.drop_column("use_icon_as_answer_icon")

    # ### end Alembic commands ###

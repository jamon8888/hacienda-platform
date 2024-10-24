"""increase max model_name length

Revision ID: eeb2e349e6ac
Revises: 53bf8af60645
Create Date: 2024-07-26 12:02:00.750358

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = 'eeb2e349e6ac'
down_revision = '53bf8af60645'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dataset_collection_bindings', schema=None) as batch_op:
        batch_op.alter_column('model_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('embeddings', schema=None) as batch_op:
        batch_op.alter_column('model_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False,
               existing_server_default=sa.text("'text-embedding-ada-002'::character varying"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('embeddings', schema=None) as batch_op:
        batch_op.alter_column('model_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False,
               existing_server_default=sa.text("'text-embedding-ada-002'::character varying"))

    with op.batch_alter_table('dataset_collection_bindings', schema=None) as batch_op:
        batch_op.alter_column('model_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###

"""add tool file

Revision ID: 4823da1d26cf
Revises: 053da0c1d756
Create Date: 2024-01-15 11:37:16.782718

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4823da1d26cf'
down_revision = '053da0c1d756'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool_files',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=False),
    sa.Column('tenant_id', postgresql.UUID(), nullable=False),
    sa.Column('conversation_id', postgresql.UUID(), nullable=False),
    sa.Column('file_key', sa.String(length=255), nullable=False),
    sa.Column('mimetype', sa.String(length=255), nullable=False),
    sa.Column('original_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id', name='tool_file_pkey')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tool_files')
    # ### end Alembic commands ###

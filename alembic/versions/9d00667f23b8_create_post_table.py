"""create post table

Revision ID: 9d00667f23b8
Revises: 
Create Date: 2022-03-31 18:55:12.504428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d00667f23b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False),)
    pass


def downgrade():
    op.drop_table('posts')
    pass

"""empty message

Revision ID: cdad0907ed3e
Revises: 9d00667f23b8
Create Date: 2022-03-31 19:03:41.216050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdad0907ed3e'
down_revision = '9d00667f23b8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

"""empty message

Revision ID: 8aa80aec4ddd
Revises: b6a0b2844f3b
Create Date: 2022-03-31 19:33:53.650634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa80aec4ddd'
down_revision = 'b6a0b2844f3b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('publised', sa.Boolean(),
                  nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     server_default=sa.text('now()'), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

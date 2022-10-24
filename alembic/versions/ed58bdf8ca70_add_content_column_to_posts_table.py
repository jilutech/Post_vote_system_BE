"""add content column to posts table

Revision ID: ed58bdf8ca70
Revises: ecbc9b3698c7
Create Date: 2022-10-24 19:24:28.738338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed58bdf8ca70'
down_revision = 'ecbc9b3698c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass


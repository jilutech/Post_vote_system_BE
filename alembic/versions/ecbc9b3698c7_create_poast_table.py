"""create poast table

Revision ID: ecbc9b3698c7
Revises: 
Create Date: 2022-10-24 19:22:36.028002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecbc9b3698c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column(
                    'id', sa.Integer(), nullable=False,primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
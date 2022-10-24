"""add foreign-key to posts table

Revision ID: a64705c103c5
Revises: eec8b9c2ba67
Create Date: 2022-10-24 21:03:30.007252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a64705c103c5'
down_revision = 'eec8b9c2ba67'
branch_labels = None
depends_on = None

def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

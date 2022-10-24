"""re adding foreign key to post table

Revision ID: 96eb6d1227db
Revises: e1f5219a2c92
Create Date: 2022-10-24 21:49:28.944250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96eb6d1227db'
down_revision = 'e1f5219a2c92'
branch_labels = None
depends_on = None




def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

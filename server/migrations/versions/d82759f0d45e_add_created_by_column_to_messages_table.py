"""Add created_by column to messages table

Revision ID: d82759f0d45e
Revises: 4c18c85f2c51
Create Date: 2024-10-08 22:29:13.675087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd82759f0d45e'
down_revision = '4c18c85f2c51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'created_at')
    # ### end Alembic commands ###

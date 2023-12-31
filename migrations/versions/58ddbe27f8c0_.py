"""empty message

Revision ID: 58ddbe27f8c0
Revises: c745dfd62085
Create Date: 2023-11-16 23:15:55.458188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58ddbe27f8c0'
down_revision = 'c745dfd62085'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###

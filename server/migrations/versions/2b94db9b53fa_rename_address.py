"""rename address

Revision ID: 2b94db9b53fa
Revises: 86882bdff90c
Create Date: 2023-11-20 03:08:59.986352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b94db9b53fa'
down_revision = '86882bdff90c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###

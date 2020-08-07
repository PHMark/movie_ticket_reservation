"""not null long/lat

Revision ID: cb13e3f05a8f
Revises: ff89c2a1dd36
Create Date: 2020-08-05 23:46:25.458052

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb13e3f05a8f'
down_revision = 'ff89c2a1dd36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('location', 'latitude',
               existing_type=mysql.CHAR(length=16),
               nullable=False)
    op.alter_column('location', 'longitude',
               existing_type=mysql.CHAR(length=16),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('location', 'longitude',
               existing_type=mysql.CHAR(length=16),
               nullable=True)
    op.alter_column('location', 'latitude',
               existing_type=mysql.CHAR(length=16),
               nullable=True)
    # ### end Alembic commands ###
"""remove status column in reservation tbl

Revision ID: 36cb896c1ea3
Revises: a4ea4549515e
Create Date: 2020-08-10 14:01:12.951251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36cb896c1ea3'
down_revision = 'a4ea4549515e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('status', mysql.CHAR(length=16), nullable=False))
    # ### end Alembic commands ###

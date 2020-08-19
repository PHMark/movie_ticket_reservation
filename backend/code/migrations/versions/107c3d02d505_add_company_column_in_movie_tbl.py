"""add company column in movie tbl

Revision ID: 107c3d02d505
Revises: b805760e462a
Create Date: 2020-08-19 17:56:46.156235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107c3d02d505'
down_revision = 'b805760e462a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('company', sa.String(120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'company')
    # ### end Alembic commands ###

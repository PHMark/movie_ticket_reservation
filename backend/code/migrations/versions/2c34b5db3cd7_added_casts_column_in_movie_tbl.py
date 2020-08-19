"""added casts column in movie tbl

Revision ID: 2c34b5db3cd7
Revises: 107c3d02d505
Create Date: 2020-08-19 17:58:22.670192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c34b5db3cd7'
down_revision = '107c3d02d505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('casts', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'casts')
    # ### end Alembic commands ###

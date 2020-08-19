"""reservation default status is failed

Revision ID: b805760e462a
Revises: 36cb896c1ea3
Create Date: 2020-08-10 14:01:26.545183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b805760e462a'
down_revision = '36cb896c1ea3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('status', sa.CHAR(length=16), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'status')
    # ### end Alembic commands ###

"""add screen_id on schedule tbl

Revision ID: 05ad6266e0cd
Revises: 566159ee2a26
Create Date: 2020-08-07 18:08:07.246584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05ad6266e0cd'
down_revision = '566159ee2a26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedule', sa.Column('screen_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_schedule_screen_id_screen'), 'schedule', 'screen', ['screen_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_schedule_screen_id_screen'), 'schedule', type_='foreignkey')
    op.drop_column('schedule', 'screen_id')
    # ### end Alembic commands ###
"""re-add screen_id and unique constraint in schedule tbl

Revision ID: d91a71574034
Revises: f6d4179cecaf
Create Date: 2020-08-09 20:28:00.286412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91a71574034'
down_revision = 'f6d4179cecaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedule', sa.Column('screen_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f('uq_schedule_screen_id'), 'schedule', ['screen_id', 'play_datetime', 'end_datetime'])
    op.create_foreign_key(op.f('fk_schedule_screen_id_screen'), 'schedule', 'screen', ['screen_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_schedule_screen_id_screen'), 'schedule', type_='foreignkey')
    op.drop_constraint(op.f('uq_schedule_screen_id'), 'schedule', type_='unique')
    op.drop_column('schedule', 'screen_id')
    # ### end Alembic commands ###

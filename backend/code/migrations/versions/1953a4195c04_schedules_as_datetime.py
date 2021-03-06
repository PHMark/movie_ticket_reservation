"""schedules as datetime

Revision ID: 1953a4195c04
Revises: 7140d0981e14
Create Date: 2020-08-09 19:47:19.424519

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1953a4195c04'
down_revision = '7140d0981e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_schedule_master_schedule_id_master_schedule', 'schedule', type_='foreignkey')
    op.drop_constraint('fk_schedule_screen_id_screen', 'schedule', type_='foreignkey')
    op.drop_index('uq_schedule_screen_id', table_name='schedule')
    op.add_column('schedule', sa.Column('end_datetime', sa.DateTime(), nullable=False))
    op.add_column('schedule', sa.Column('play_datetime', sa.DateTime(), nullable=False))
    op.drop_column('schedule', 'master_schedule_id')
    op.drop_column('schedule', 'screen_id')
    op.drop_column('schedule', 'play_time')
    op.drop_column('schedule', 'end_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedule', sa.Column('end_time', mysql.TIME(), nullable=False))
    op.add_column('schedule', sa.Column('play_time', mysql.TIME(), nullable=False))
    op.add_column('schedule', sa.Column('screen_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('schedule', sa.Column('master_schedule_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_schedule_screen_id_screen', 'schedule', 'screen', ['screen_id'], ['id'])
    op.create_foreign_key('fk_schedule_master_schedule_id_master_schedule', 'schedule', 'master_schedule', ['master_schedule_id'], ['id'])
    op.create_index('uq_schedule_screen_id', 'schedule', ['screen_id', 'master_schedule_id', 'play_time', 'end_time'], unique=True)
    op.drop_column('schedule', 'play_datetime')
    op.drop_column('schedule', 'end_datetime')
    # ### end Alembic commands ###

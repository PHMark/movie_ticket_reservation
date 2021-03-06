"""drop foreign keys in movie_screen tbl

Revision ID: 857ae8c4bc0c
Revises: cc6964695fa6
Create Date: 2020-08-21 19:25:43.188108

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '857ae8c4bc0c'
down_revision = 'cc6964695fa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('master_schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('launch_date', sa.Date(), nullable=False),
    sa.Column('phase_out_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_master_schedule'))
    )
    
    op.drop_constraint('fk_movie_screen_screen_id_screen', 'movie_screen', type_='foreignkey')
    op.drop_constraint('fk_movie_screen_schedule_id_schedule', 'movie_screen', type_='foreignkey')
    op.drop_constraint('fk_movie_screen_movie_id_movie', 'movie_screen', type_='foreignkey')
    op.drop_column('movie_screen', 'movie_id')
    op.drop_column('movie_screen', 'screen_id')
    op.drop_column('movie_screen', 'schedule_id')
    op.drop_index('uq_movie_screen_movie_id', table_name='movie_screen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_screen', sa.Column('schedule_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('movie_screen', sa.Column('screen_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('movie_screen', sa.Column('movie_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_movie_screen_movie_id_movie', 'movie_screen', 'movie', ['movie_id'], ['id'])
    op.create_foreign_key('fk_movie_screen_schedule_id_schedule', 'movie_screen', 'schedule', ['schedule_id'], ['id'])
    op.create_foreign_key('fk_movie_screen_screen_id_screen', 'movie_screen', 'screen', ['screen_id'], ['id'])
    op.create_index('uq_movie_screen_movie_id', 'movie_screen', ['movie_id', 'screen_id', 'schedule_id'], unique=True)
    op.drop_table('master_schedule')
    # ### end Alembic commands ###

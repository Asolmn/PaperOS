"""models.py --version2.1.3 更新paper库名

Revision ID: 421a50059617
Revises: 9a5398dd553c
Create Date: 2021-12-20 19:12:42.378513

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '421a50059617'
down_revision = '9a5398dd553c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=128), nullable=False),
    sa.Column('uuid', sa.String(length=128), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename'),
    sa.UniqueConstraint('uuid')
    )
    op.drop_index('filename', table_name='paperos')
    op.drop_index('uuid', table_name='paperos')
    op.drop_table('paperos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paperos',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('filename', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('uuid', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('student_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='paperos_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('uuid', 'paperos', ['uuid'], unique=True)
    op.create_index('filename', 'paperos', ['filename'], unique=True)
    op.drop_table('paper')
    # ### end Alembic commands ###

"""models.py --version2.0.2 Student and Teacher add password

Revision ID: ee8083000cc7
Revises: 0c58cdf35185
Create Date: 2021-12-10 17:59:49.011375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee8083000cc7'
down_revision = '0c58cdf35185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('password', sa.String(length=64), nullable=True))
    op.add_column('teachers', sa.Column('password', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teachers', 'password')
    op.drop_column('students', 'password')
    # ### end Alembic commands ###

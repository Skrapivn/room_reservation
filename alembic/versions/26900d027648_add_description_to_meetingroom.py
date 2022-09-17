"""Add description to MeetingRoom

Revision ID: 26900d027648
Revises: ad156421e965
Create Date: 2022-09-13 17:25:56.142491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26900d027648'
down_revision = 'ad156421e965'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###

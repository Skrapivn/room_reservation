"""Add user relationship to Reservation

Revision ID: 05
Revises: 04
Create Date: 2022-09-20 19:01:03.923532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05'
down_revision = '04'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.create_foreign_key(
            'fk_reservation_user_id_user',
            'user',
            ['user_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.drop_constraint(
            'fk_reservation_user_id_user',
            type_='foreignkey'
        )
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###

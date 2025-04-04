"""empty message

Revision ID: 541720594bd7
Revises: e90912ae00a4
Create Date: 2025-04-04 12:35:03.097355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541720594bd7'
down_revision = 'e90912ae00a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('melody_battle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('melody_battle', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###

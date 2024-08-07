"""Add MenuItem model

Revision ID: 70804713f267
Revises: c2a0e9362dc6
Create Date: 2024-06-29 18:41:46.365691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70804713f267'
down_revision = 'c2a0e9362dc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('users')
    op.drop_table('order_items')
    op.drop_table('menu_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('order_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=256), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=256), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=False),
    sa.Column('is_admin', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), nullable=False),
    sa.Column('address', sa.VARCHAR(length=150), nullable=False),
    sa.Column('card_number', sa.VARCHAR(length=20), nullable=False),
    sa.Column('card_name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('expiration_date', sa.VARCHAR(length=10), nullable=False),
    sa.Column('cvv', sa.VARCHAR(length=4), nullable=False),
    sa.Column('food_item', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

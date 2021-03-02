"""Initial Migration

Revision ID: 99a732c31bb8
Revises: 58e3a8aec7c4
Create Date: 2021-03-02 23:40:15.582535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '99a732c31bb8'
down_revision = '58e3a8aec7c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('downvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    op.drop_column('pitches', 'time')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=False))
    op.drop_column('users', 'secure_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('secure_password', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('users', 'pass_secure')
    op.add_column('pitches', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'posted')
    op.drop_table('upvotes')
    op.drop_table('downvotes')
    op.drop_table('comments')
    # ### end Alembic commands ###

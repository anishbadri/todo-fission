"""Task and Todo table

Revision ID: 094994ff3734
Revises: 
Create Date: 2019-06-20 13:07:41.537593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094994ff3734'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=100), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_task'), 'task', ['task'], unique=False)
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo_task', sa.String(length=100), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_todo_task'), 'todo', ['todo_task'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_todo_task'), table_name='todo')
    op.drop_table('todo')
    op.drop_index(op.f('ix_task_task'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###

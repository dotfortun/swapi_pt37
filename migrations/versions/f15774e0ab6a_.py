"""empty message

Revision ID: f15774e0ab6a
Revises: 6f1659efa74f
Create Date: 2022-07-12 00:51:45.896154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f15774e0ab6a'
down_revision = '6f1659efa74f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lesson_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lesson_group', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('paragraph', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'lesson_group')
    )
    op.create_table('vocab',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=128), nullable=True),
    sa.Column('phonetic', sa.String(length=128), nullable=True),
    sa.Column('mandarin', sa.String(length=128), nullable=True),
    sa.Column('phon_mandarin', sa.String(length=128), nullable=True),
    sa.Column('images', sa.String(length=128), nullable=True),
    sa.Column('part_of_speech', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lesson_page_to_lesson_page',
    sa.Column('node_id_parent', sa.Integer(), nullable=True),
    sa.Column('node_id_child', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['node_id_child'], ['lesson_page.id'], ),
    sa.ForeignKeyConstraint(['node_id_parent'], ['lesson_page.id'], )
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'people', ['id'])
    op.create_unique_constraint(None, 'planets', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'planets', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_table('question')
    op.drop_table('lesson_page_to_lesson_page')
    op.drop_table('vocab')
    op.drop_table('lesson_page')
    # ### end Alembic commands ###

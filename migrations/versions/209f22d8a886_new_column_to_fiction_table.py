"""new column to fiction table

Revision ID: 209f22d8a886
Revises: 1917bc11fab9
Create Date: 2021-03-20 05:26:32.243361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '209f22d8a886'
down_revision = '1917bc11fab9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fiction', sa.Column('mediafire_link', sa.Text(), nullable=True))
    op.add_column('fiction', sa.Column('tiki_link', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fiction', 'tiki_link')
    op.drop_column('fiction', 'mediafire_link')
    # ### end Alembic commands ###
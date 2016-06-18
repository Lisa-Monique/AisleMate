from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item = Table('item', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('aisle_id', INTEGER),
    Column('name', VARCHAR(length=140)),
    Column('user_id', INTEGER),
)

item = Table('item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('aisle_id', Integer),
    Column('list_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['item'].columns['user_id'].drop()
    post_meta.tables['item'].columns['list_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['item'].columns['user_id'].create()
    post_meta.tables['item'].columns['list_id'].drop()

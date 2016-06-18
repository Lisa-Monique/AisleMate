from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
aisle = Table('aisle', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('items', String(length=140)),
    Column('list_id', Integer),
)

list = Table('list', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120)),
    Column('_password', String(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['aisle'].create()
    pre_meta.tables['list'].columns['body'].drop()
    pre_meta.tables['list'].columns['timestamp'].drop()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['_password'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['aisle'].drop()
    pre_meta.tables['list'].columns['body'].create()
    pre_meta.tables['list'].columns['timestamp'].create()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['_password'].drop()

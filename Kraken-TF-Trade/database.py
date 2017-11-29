from peewee import *
from configparse import Config
databasetype = Config.get('database', 'type')


if databasetype == "SQLite":
    database = SqliteDatabase(Config.get('database', 'path'))
elif databasetype == "Mysql":
    databasename = Config.get('database', 'dbname')
    databaseuser = Config.get('database', 'user')
    database = MySQLDatabase(databasename, user=databaseuser)
elif databasetype == "Postgresql":
    database = PostgresqlDatabase()


def db_connect():
    database.connect()


def db_close():
    if not database.is_closed():
        database.close()


def create_tables():
    db_connect()
    database.create_tables([currency_history], safe=True)
    db_close()


class BaseModel(Model):
    class Meta:
        database = database


class currency_history(BaseModel):
    currency = CharField(max_length=16, null=False, index=True)
    time = DateTimeField(null=False, index=True)
    interval = IntegerField()
    open = DecimalField()
    high = DecimalField()
    low = DecimalField()
    close = DecimalField()
    vwap = DecimalField()
    volume = DecimalField()
    count = DecimalField()

    class Meta:
        order_by = ('-time',)


# Create all tables so we can use them later
create_tables()

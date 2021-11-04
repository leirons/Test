from peewee import *

#TODO Изменить перед тем как показывать
db = SqliteDatabase("C:/Users/Chokeup/PycharmProjects/pythonProject9/services/calculation/db.db")#T


class User(Model):
    role = CharField(max_length=25,
                     default="User")  # Peewee как ОРМ не очень, поэтому тут нельзя сделать CHOICEFIELD, вроде.
    name = CharField(max_length=25)
    surname = CharField(max_length=25)
    email = CharField(max_length=50,unique=True)
    password = CharField(max_length=50)

    class Meta:
        database = db


class Category(Model):
    name_of_category = CharField(max_length=25,unique=True)

    class Meta:
        database = db


class Calculation(Model):
    user = ForeignKeyField(User, backref="calculation")
    price = IntegerField(default=0)
    category = ForeignKeyField(Category, backref="category")
    date = DateTimeField()

    class Meta:
        database = db



# Использовать DI?
db.connect()
db.create_tables([User, Category, Calculation])

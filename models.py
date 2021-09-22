from peewee import * 
from db_config import database_path

db = SqliteDatabase(database_path)

class Tree(Model):    
    name = CharField(unique=True)
    max_height = DecimalField() 

    class Meta:
        database = db

    def __str__(self):
        return f'The {self.name} tree has a maximum height of {self.max_height} meters.  (Tree ID={self.id})'


db.create_tables([Tree])
from peewee import * 
from db_config import database_path

db = SqliteDatabase(database_path)

class Tree(Model):    
    name = CharField(unique=True) #, constraints=[Check('length(name) > 1')] )
    max_height = DecimalField() # constraints=[Check('max_height >= 0 and max_height <= 500' ) ])

    class Meta:
        database = db

    def __str__(self):
        return f'The {self.name} tree has a maximum height of {self.max_height} meters.  (Tree ID={self.id})'


db.create_tables([Tree])
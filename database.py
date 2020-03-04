from peewee import IntegrityError
from models import Tree 

def add_tree(name, max_height):
    try:
        Tree(name=name, max_height=max_height).save()
    except IntegrityError as e:
        raise TreeError('Error adding tree because ' + str(e)) 


def get_all_trees():
    result = Tree.select().execute()
    return list(result)


def delete_tree_by_name(name):
    trees_deleted = Tree.delete().where(Tree.name==name).execute()
    return trees_deleted > 0



class TreeError(Exception):
    pass
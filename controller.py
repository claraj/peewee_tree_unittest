import database 
from database import TreeError
import ui

def add_tree():
    name = ui.get_string('Enter name of tree')
    max_height = ui.get_positive_float(f'Enter max height of {name}')
    try:
        database.add_tree(name, max_height)
        print('Added tree')
    except TreeError as e:
        print(e)


def all_trees():
    trees = database.get_all_trees()
    ui.display_trees(trees)


def delete_tree():
    name = ui.get_string('Enter name of tree')
    deleted = database.delete_tree_by_name(name)
    if deleted:
        print('Tree was deleted')
    else:
        print('That tree was not in the database')
    
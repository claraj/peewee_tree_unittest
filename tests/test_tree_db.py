import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import *

import db_config
test_db_path = 'test_trees.db'
db_config.database_path = test_db_path 

from models import Tree
import controller 
import database
from database import TreeError


class TreeDatabaseTest(TestCase):

    def setUp(self):
        # connect to test database, drop and create tables 
        self.db = SqliteDatabase(test_db_path)
        self.db.drop_tables([Tree])
        self.db.create_tables([Tree])


    def test_add_tree(self):
        database.add_tree('oak', 50)
        oak_tree = Tree.get_or_none(Tree.name=='oak' and Tree.max_height==50)
        self.assertIsNotNone(oak_tree)


    def test_add_tree_duplicate(self):
        Tree(name='oak', max_height=40).save()
        with self.assertRaises(TreeError):
            database.add_tree('oak', 50)
        

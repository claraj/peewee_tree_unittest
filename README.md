# Peewee and unittests

Run all the tests from the base directory of the project 

`python3 -m unittest discover tests`

Things to note:

* The database connection information is in the db_config.py file.
* The test imports the file, and then changes the value

```
import db_config  # import the db_config module
test_db_path = 'test_trees.db'   
db_config.database_path = test_db_path  # and change the variable  
```

* The test must do this **before** it imports the database module.  The database module imports the db_config file to get the database path, and if the test has changed it first, it will read the test database path. 

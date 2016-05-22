# project/_config.py


import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

# the WTF config setting is used for cross-suite request forgery prevention
# The SECRET_KEY is used with WTF to create a cryptographic token that is used to validate a form

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# The database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
import os

# grab the foler where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

# the WTF config seeting is used for cross-sute request forgery prevention
# The SECRET_KEY is used with WTF to create a cryptographic token that is used to cvalidate a form

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
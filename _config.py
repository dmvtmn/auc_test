import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'offre.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'hard_to_guess'


# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

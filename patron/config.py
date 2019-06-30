import os


# Mongo
DB_HOST = os.environ['DB_HOST']
DB_PATRON = os.environ['DB_PATRON']
DB_USR = os.environ.get('DB_USR', None)
DB_PWD = os.environ.get('DB_PWD', None)

# Dollar
KEY_DOLLAR = os.environ['KEY_DOLLAR']

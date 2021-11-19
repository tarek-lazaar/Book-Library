import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:' + SECRET_KEY + '@database-1.cmcycie0rurf.eu-west-3.rds.amazonaws.com/Library'
    DEBUG = True
    CSRF_ENABLED = True




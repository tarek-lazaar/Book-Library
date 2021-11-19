import os

class Config(object):
    SECRET_KEY = "ttllzz00"
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:' + SECRET_KEY + '@database-1.cmcycie0rurf.eu-west-3.rds.amazonaws.com/Library'
    DEBUG = True
    CSRF_ENABLED = True




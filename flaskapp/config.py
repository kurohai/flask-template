import os
from datetime import datetime
from dicto import dicto


class Config(dicto):
    appname = 'Flask Template'
    appnamed = 'flask-template'
    pwd = os.path.abspath(os.curdir)
    working_dir = pwd
    data_dir = os.path.join(working_dir, 'data')
    logging = False
    # sqlite db for this app
    dbpath = '{dir}/{app}.db'.format(dir=working_dir, app=appnamed)
    dburi = 'sqlite:///{db}'.format(db=dbpath)

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'all-your-base-are-belong-to-us-on-or-after-{0}'.format(datetime.now().date().isoformat())
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = dburi
    SESSION_PROTECTION = 'strong'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

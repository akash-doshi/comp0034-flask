"""Flask config class."""
from os.path import dirname, abspath, join

class Config(object):
    """Set Flask base configuration"""
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'

    # General Config
    DEBUG = False
    TESTING = False

    # Forms config
    WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'

    # Database config
    CWD = dirname(abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'cscourses.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    # The following are fictitious details for a MySQL server database! Included to illustrate the syntax.
    DB_SERVER = '192.168.19.32'
    SQLALCHEMY_DATABASE_URI = 'mysql://akash.doshi@{}/foo'.format(DB_SERVER)
    DEBUG = False
    TESTING = False

class TestConfig(Config):
    TESTING = True

class DevConfig(Config):
    DEBUG = True

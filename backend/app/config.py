import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-api-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT specific configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret-jwt-key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '..', 'api-dev.sqlite')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

class Config(object):
    SECRET_KEY = "2afdc1d89de14fdbbfb87341259237a0z"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    # setup the recaptcha keys
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = 'public'
    RECAPTCHA_PRIVATE_KEY = 'private'
    RECAPTCHA_OPTIONS = {'theme': 'white'}


class ProductionuctionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True

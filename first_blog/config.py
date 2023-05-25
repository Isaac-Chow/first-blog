class Config(object):
    SECRET_KEY="2afdc1d89de14fdbbfb87341259237a0z"
    SQLALCHEMY_DATABASE_URI="sqlite:///database.db"

class ProductionuctionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True

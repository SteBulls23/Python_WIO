import os
class Config:
    SECRET_KEY = "my secret..."
    TESTING = False
    JSON_SORT_KEYS=False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or "sqlite://"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "mysql+mysqlconnector://root:root@localhost:3306/wioterminal"
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or \
        "mysql+mysqlconnector://root:root@localhost:3306/wioterminal"

config = {
    "testing" : TestingConfig,
    "development" : DevelopmentConfig,
    "production" : ProductionConfig,

    "default" : DevelopmentConfig
}
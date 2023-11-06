class Config:
    SECRET_KEY = "my secret..."
    TESTING = False
    JSON_SORT_KEYS=False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@localhost:3306/wioterminal"
    
class ProductionConfig(Config):
    DEBUG = False

config = {
    "testing" : TestingConfig,
    "development" : DevelopmentConfig,
    "production" : ProductionConfig,

    "default" : DevelopmentConfig
}
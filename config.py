class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

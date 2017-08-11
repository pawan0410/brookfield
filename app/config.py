"""
Configuration file
"""


class Config:
    """
    Base Configuration
    """

    DEBUG = True
    SECRET_KEY = r'f\x13\xd9fM\xdc\x82\x01b\xdb\x03'


class DevelopmentConfig(Config):
    """
    Local Development
    """

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
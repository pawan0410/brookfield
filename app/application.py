"""
Application
"""

import locale
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.contrib.fixers import ProxyFix

from flask import Flask

from app.config import app_config
from app.views import default_blueprint



def application(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    handler = RotatingFileHandler('app.log')
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Register Extension

    app.register_blueprint(default_blueprint)
    app.register_blueprint(default_blueprint, url_prefix='/thankyou')


    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return app

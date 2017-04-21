#!/bin/env python

from flask import Flask
from flask_pagedown import PageDown
from flaskext.markdown import Markdown
from config import DevelopmentConfig, TestingConfig, ProductionConfig, StagingConfig

settings = DevelopmentConfig()



flasktemplate = Flask(__name__)

flasktemplate.config.SECRET_KEY = 'enydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
flasktemplate.config.SESSION_PROTECTION = 'strong'

pagedown = PageDown(flasktemplate)
Markdown(flasktemplate)


@flasktemplate.template_global()
def appname():
    return settings.appname


@flasktemplate.template_global()
def appnamed():
    return settings.appnamed

@flasktemplate.template_global()
def global_settings():
    return settings


@flasktemplate.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return 'No page here, dood. 404!', 404

import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True
    
    # mail configurations
    MAIL_SERVER = 'smtp.live.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    MAIL_MAX_EMAILS = 5
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

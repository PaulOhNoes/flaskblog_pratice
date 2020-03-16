import os


class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # FOR THIS TO WORK YOU NEED 3 THINGS
    #   CHANGE SECURITY OPTION TO ALLOW UN-SECURE APPS
    #   HAVE 2-STEP AUTHENTICATION
    #   GENERATE A PASSWORD FOR APPS
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # Environment variables
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
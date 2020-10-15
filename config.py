import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456890'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')                          # Using environment variable 'DATABASE_URL' as database adress. 
                                                                                # If not defined default adress '/app.db' is used and stored into basedir variable. 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
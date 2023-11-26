import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "SOMESECRETKEY"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
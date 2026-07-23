import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mat-khau-bao-mat-flask'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
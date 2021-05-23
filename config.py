import os

from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@localhost/single_db'
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = bool(os.environ.get('FLASK_DEBUG', False))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///melody.db')

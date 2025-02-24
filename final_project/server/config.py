import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'set this key in .env file'


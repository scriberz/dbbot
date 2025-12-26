# config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN', '')
DB_PATH = os.getenv('DB_PATH', 'database.db')

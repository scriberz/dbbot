# Скопируйте этот файл в config.py и заполните своими значениями
# Или используйте переменные окружения через .env файл

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
DB_PATH = os.getenv('DB_PATH', 'database.db')


import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')  # CLAVE API
BASE_URL = "https://api.themoviedb.org/3"  # URL BASE PARA HACER LA PETICIÓN

from dotenv import load_dotenv  # save environment variables in venv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')  # get environment variables
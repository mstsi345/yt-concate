from dotenv import load_dotenv  # save environment variables in venv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')  # get environment variables


DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')

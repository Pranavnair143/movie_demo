import os
from dotenv import load_dotenv

load_dotenv()

POSTGRESQL_ENGINE=os.getenv('POSTGRESQL_ENGINE')
POSTGRESQL_DATABASE=os.getenv('POSTGRESQL_DATABASE')
POSTGRESQL_USER=os.getenv('POSTGRESQL_USER')
POSTGRESQL_PASSWORD=os.getenv('POSTGRESQL_PASSWORD')
POSTGRESQL_HOST=os.getenv('POSTGRESQL_HOST')
POSTGRESQL_PORT=os.getenv('POSTGRESQL_PORT')
MOVIES_API_URL=os.getenv('MOVIES_API_URL')
MOVIES_API_AUTH_USERNAME=os.getenv('MOVIES_API_AUTH_USERNAME')
MOVIES_API_AUTH_PASSWORD=os.getenv('MOVIES_API_AUTH_PASSWORD')

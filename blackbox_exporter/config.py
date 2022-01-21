# Read config from .env file
from dotenv import load_dotenv
load_dotenv()

def return_conf(key):
    return os.getenv(key)
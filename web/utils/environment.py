import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_env(env_var: str = '') -> str:
    return os.environ.get(env_var) \
            or open(os.environ.get(f'{env_var}_FILE')).read()
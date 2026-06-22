import os
from dotenv import load_dotenv

load_dotenv()


SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
ZAPI_INSTANCE = os.getenv('ZAPI_INSTANCE')
ZAPI_TOKEN = os.getenv('ZAPI_TOKEN')
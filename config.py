import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
ZAPI_INSTANCE = os.getenv('ZAPI_INSTANCE')
ZAPI_TOKEN = os.getenv('ZAPI_TOKEN')
ZAPI_CLIENT_TOKEN = os.getenv('ZAPI_CLIENT_TOKEN')

def validar_configuracoes():    
    variaveis = {
        'SUPABASE_URL': SUPABASE_URL,
        'SUPABASE_KEY': SUPABASE_KEY,
        'ZAPI_INSTANCE': ZAPI_INSTANCE,
        'ZAPI_TOKEN': ZAPI_TOKEN,
        'ZAPI_CLIENT_TOKEN': ZAPI_CLIENT_TOKEN
    }
    
    faltando = []
    for nome, valor in variaveis.items():
        if not valor:
            faltando.append(nome)
    
    if faltando:
        print("\nERRO: Variáveis de ambiente não configuradas:")
        for var in faltando:
            print(f"   - {var}")
        print("\nConfigure o arquivo .env com base no .env.example")
        return False
    
    print("Configurações validadas com sucesso")
    return True
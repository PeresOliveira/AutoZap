from config import SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE, ZAPI_TOKEN
from supabase_client import SupabaseClient

def main():
    print("Buscando contatos no Supabase")
    
    # Criar cliente Supabase
    supabase = SupabaseClient()
    
    # Buscar contatos 
    contacts = supabase.get_contacts(limit=3)
    
    # Mostrar resultados
    if contacts:
        print(f"\n Encontrados {len(contacts)} contatos:")
        for contact in contacts:
            print(f"  - {contact.get('nome_contato')} ({contact.get('telefone')})")
    else:
        print("Nenhum contato encontrado")

if __name__ == "__main__":
    main()
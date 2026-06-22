from config import SUPABASE_URL, SUPABASE_KEY
from supabase_client import SupabaseClient
from zapi_client import ZAPIClient

def main():
    print("Enviando mensagens via Z-API")
    
    # Buscar contatos
    supabase = SupabaseClient()
    contacts = supabase.get_contacts(limit=3)
    
    if not contacts:
        print("Nenhum contato encontrado")
        return
    
    # Preparar cliente Z-API
    zapi = ZAPIClient()
    
    # Enviar mensagens
    print(f"\nEnviando para {len(contacts)} contatos...")
    
    for contact in contacts:
        name = contact.get('nome_contato')
        phone = contact.get('telefone')
        
        message = f"Olá, {name} tudo bem com você?"
        
        print(f"\nEnviando para {name} ({phone})")
        print(f"   Mensagem: {message}")
        
        zapi.send_message(phone, message)
    
    print("\nProcessamento concluído!")

if __name__ == "__main__":
    main()
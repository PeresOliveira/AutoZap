from config import validar_configuracoes
from supabase_client import SupabaseClient
from zapi_client import ZAPIClient

def main():
    print("Enviando mensagens via Z-API")
    
    # Validar configurações
    print("\nValidando configurações...")
    if not validar_configuracoes():
        return
    
    # Buscar contatos
    print("\nConectando ao Supabase...")
    supabase = SupabaseClient()
    contacts = supabase.get_contacts(limit=3)
    
    if not contacts:
        print("\n Nenhum contato ativo encontrado no banco")
        print(" Programa finalizado")
        return
    
    # Preparar cliente Z-API
    zapi = ZAPIClient()
    
    # Enviar mensagens
    print(f"\nIniciando envio para {len(contacts)} contatos...")    
    
    resultados = {
        'total': len(contacts),
        'enviados': 0,
        'falhas': 0,
        'detalhes': []
    }
    
    for i, contact in enumerate(contacts, 1):
        name = contact.get('nome_contato', 'Cliente')
        phone = contact.get('telefone')
        
        if not phone:
            print(f"\n[{i}/{len(contacts)}] {name} - Sem telefone, ignorando")
            resultados['falhas'] += 1
            resultados['detalhes'].append({
                'nome': name,
                'telefone': 'SEM TELEFONE',
                'status': 'FALHA',
                'erro': 'Telefone não informado'
            })
            continue
        
        message = f"Olá, {name} tudo bem com você?"
        
        print(f"\n [{i}/{len(contacts)}] Enviando para {name}")
        print(f"   Telefone: {phone}")
        print(f"   Mensagem: {message}")
        
        resultado = zapi.send_message(phone, message)
        
        if resultado['success']:
            print("   Enviado com sucesso!")
            resultados['enviados'] += 1
            resultados['detalhes'].append({
                'nome': name,
                'telefone': phone,
                'status': 'ENVIADO',
                'erro': None
            })
        else:
            erro = resultado.get('error', 'Erro desconhecido')
            print(f"   Falha: {erro}")
            resultados['falhas'] += 1
            resultados['detalhes'].append({
                'nome': name,
                'telefone': phone,
                'status': 'FALHA',
                'erro': erro
            })

if __name__ == "__main__":
    main()
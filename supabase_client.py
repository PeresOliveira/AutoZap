from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

class SupabaseClient:
    def __init__(self):
        self.client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Conectado ao Supabase")
    
    def get_contacts(self, limit=3):
        try:
            response = self.client.table('contacts')\
                .select('*')\
                .eq('active', True)\
                .limit(limit)\
                .execute()
            
            return response.data
        except Exception as e:
            print(f"Erro ao buscar contatos: {e}")
            return []
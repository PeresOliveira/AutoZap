import requests
from config import ZAPI_INSTANCE, ZAPI_TOKEN, ZAPI_CLIENT_TOKEN

class ZAPIClient:
    def __init__(self):
        self.instance = ZAPI_INSTANCE
        self.token = ZAPI_TOKEN
        self.client_token = ZAPI_CLIENT_TOKEN
        self.base_url = "https://api.z-api.io"
    
    def send_message(self, phone, message):
        url = f"{self.base_url}/instances/{self.instance}/token/{self.token}/send-text"
        
        headers = {
            "Content-Type": "application/json",
            "Client-Token": self.client_token
        }
        
        payload = {
            "phone": phone,
            "message": message
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                print(f"Mensagem enviada para {phone}")
                return True
            else:
                print(f"Erro {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            return False
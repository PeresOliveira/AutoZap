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
                return {"success": True, "status": response.status_code}
            else:
                return {"success": False, "status": response.status_code, "error": response.text}
                
        except requests.exceptions.Timeout:
            return {"success": False, "error": "Timeout - A requisição demorou muito"}
        except requests.exceptions.ConnectionError:
            return {"success": False, "error": "Erro de conexão - Verifique sua internet"}
        except Exception as e:
            return {"success": False, "error": str(e)}
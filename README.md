# AutoZap - Envio de Mensagens via Z-API + Supabase


## 1. Setup da tabela no Supabase

No painel do Supabase, em **SQL Editor**, rode:

```sql
CREATE TABLE contacts (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nome_contato TEXT NOT NULL,
    telefone TEXT NOT NULL,
    active BOOLEAN DEFAULT TRUE
);
```

Para testar, adicione contatos, exemplo:

```sql
INSERT INTO contacts (nome_contato, telefone) VALUES
('João Silva', '5511999999999'),
('Maria Santos', '5511888888888');
```

## 2. Variáveis de ambiente (.env)

Copie o `.env.example` pra `.env`:

```bash
copy .env.example .env
```

E preencha:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
ZAPI_INSTANCE=sua_instancia_zapi
ZAPI_TOKEN=seu_token_zapi
ZAPI_CLIENT_TOKEN=seu_client_token_zapi
```


## 3. Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

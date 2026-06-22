import config

def main():
    print("Projeto iniciado!")
    print(f"Supabase URL: {config.SUPABASE_URL}")
    print(f"Z-API Instance: {config.ZAPI_INSTANCE}")

if __name__ == "__main__":
    main()
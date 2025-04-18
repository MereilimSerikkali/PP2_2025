import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="12345678"
    )
    print("✅ Connected to the PostgreSQL server.")
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")

import requests
from database import get_connection
import random

URL = "https://fakestoreapi.com/products"
products = requests.get(URL).json()

conn = get_connection()
cur = conn.cursor()

for p in products:
    cur.execute("""
        INSERT INTO raw.dim_products
        (product_id, product_name, category, price, weight_kg)
        VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (product_id) DO NOTHING;
    """, (
        p["id"],
        p["title"],
        p["category"],
        p["price"],
        round(random.uniform(0.2, 5.0), 2)   # mock weight
    ))

conn.commit()
cur.close()
conn.close()

print("dim_products loaded successfully")

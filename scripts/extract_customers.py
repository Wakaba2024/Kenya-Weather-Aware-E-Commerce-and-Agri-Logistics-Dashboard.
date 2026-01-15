import requests
from database import get_connection

URL = "https://fakerapi.it/api/v2/persons?_quantity=50"
response = requests.get(URL).json()
customers = response["data"]

conn = get_connection()
cur = conn.cursor()

for i, c in enumerate(customers, start=1):

    city = c["address"]["city"]
    lat = c["address"]["latitude"]
    lon = c["address"]["longitude"]

    cur.execute("""
        INSERT INTO raw.dim_customers
        (customer_id, full_name, city, latitude, longitude)
        VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (customer_id) DO NOTHING;
    """, (
        i,
        f"{c['firstname']} {c['lastname']}",
        city,
        lat,
        lon
    ))

conn.commit()
cur.close()
conn.close()

print("✅ dim_customers loaded successfully")

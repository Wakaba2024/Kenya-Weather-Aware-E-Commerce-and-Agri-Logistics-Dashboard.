import psycopg2
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="John@4401"
)
cur = conn.cursor()

# -------------------------
# PRODUCTS
# -------------------------
products = [
    ("Maize Flour 2kg", "Food", 220, 2.0),
    ("Rice 5kg", "Food", 750, 5.0),
    ("Cooking Oil 3L", "Food", 950, 3.0),
    ("Cement Bag", "Construction", 780, 50.0),
    ("Animal Feed 25kg", "Agriculture", 1800, 25.0),
]

for p in products:
    cur.execute("""
        INSERT INTO raw.dim_products (product_name, category, price, weight_kg)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, p)

# -------------------------
# CUSTOMERS
# -------------------------
cities = [
    ("Nairobi", -1.286389, 36.817223),
    ("Nakuru", -0.303099, 36.080025),
    ("Eldoret", 0.514277, 35.269779),
    ("Kisumu", -0.091702, 34.767956),
    ("Mombasa", -4.043477, 39.668206)
]

for _ in range(50):
    city = random.choice(cities)
    cur.execute("""
        INSERT INTO raw.dim_customers (full_name, city, latitude, longitude)
        VALUES (%s, %s, %s, %s);
    """, (
        fake.name(),
        city[0],
        city[1],
        city[2]
    ))

# -------------------------
# ORDERS
# -------------------------
cur.execute("SELECT customer_id FROM raw.dim_customers;")
customers = [r[0] for r in cur.fetchall()]

cur.execute("SELECT product_id FROM raw.dim_products;")
products_ids = [r[0] for r in cur.fetchall()]

for _ in range(200):
    cur.execute("""
        INSERT INTO raw.fact_orders (
            customer_id,
            product_id,
            order_date,
            quantity,
            delivery_status
        )
        VALUES (%s, %s, %s, %s, %s);
    """, (
        random.choice(customers),
        random.choice(products_ids),
        date.today() - timedelta(days=random.randint(0, 14)),
        random.randint(1, 10),
        random.choice(["DELIVERED", "IN_TRANSIT", "DELAYED"])
    ))

conn.commit()
cur.close()
conn.close()

print("Business data loaded successfully.")

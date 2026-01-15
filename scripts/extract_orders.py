from database import get_connection
import random
from datetime import date

conn = get_connection()
cur = conn.cursor()

delivery_statuses = ["ON_TIME", "DELAYED", "CANCELLED"]

TOTAL_ORDERS = 50

for i in range(1, TOTAL_ORDERS + 1):

    cur.execute("""
        INSERT INTO raw.fact_orders
        (order_id, customer_id, product_id,
         order_date, quantity, delivery_status)
        VALUES (%s,%s,%s,%s,%s,%s)
        ON CONFLICT (order_id) DO NOTHING;
    """, (
        i,
        random.randint(1, 50),   # customer_id
        random.randint(1, 20),   # product_id
        date.today(),
        random.randint(1, 5),
        random.choice(delivery_statuses)
    ))

conn.commit()
cur.close()
conn.close()

print("✅ fact_orders loaded successfully")

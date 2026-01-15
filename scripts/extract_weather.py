import requests
import psycopg2
from datetime import datetime

# -----------------------
# CONFIGURATION
# -----------------------
API_KEY = ""

CITIES = {
    "Nairobi": (-1.286389, 36.817223),
    "Mombasa": (-4.043477, 39.668206),
    "Kisumu": (-0.091702, 34.767956),
    "Eldoret": (0.514277, 35.269779),
    "Nakuru": (-0.303099, 36.080025),
}

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "",
    "port": 5432
}

# -----------------------
# CONNECT DB
# -----------------------
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# -----------------------
# INGEST WEATHER
# -----------------------
for city, coords in CITIES.items():
    print(f"Fetching weather for {city}")

    url = (
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={coords[0]}&lon={coords[1]}"
        f"&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()
    print(data)

    for record in data["list"]:
        forecast_time = datetime.fromtimestamp(record["dt"])
        rain_mm = record.get("rain", {}).get("3h", 0)
        wind_speed = record["wind"]["speed"]
        temperature = record["main"]["temp"]

        cur.execute(
            """
            INSERT INTO "raw"."fact_weather_forecast"
            (city_id, forecast_datetime, rain_mm, wind_speed, temperature)
            VALUES (
                (SELECT city_id FROM warehouse.dim_city WHERE city_name = %s),
                %s, %s, %s, %s
            )
            """,
            (city, forecast_time, rain_mm, wind_speed, temperature)
        )

    conn.commit()
    print(f"{city} done.")

cur.close()
conn.close()
print("Weather ingestion complete.")

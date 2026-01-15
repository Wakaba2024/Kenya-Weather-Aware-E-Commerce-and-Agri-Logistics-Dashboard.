CREATE TABLE warehouse.fact_orders (
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES warehouse.dim_customer(customer_id),
    product_id INT REFERENCES warehouse.dim_product(product_id),
    city_id INT REFERENCES warehouse.dim_city(city_id),
    order_date TIMESTAMP,
    delivery_date TIMESTAMP,
    delivery_minutes INT,
    delivery_status VARCHAR(20)
);

CREATE TABLE raw.fact_weather_forecast (
    city_id INT,
    forecast_datetime TIMESTAMP,
    rain_mm NUMERIC(6,2),
    wind_speed NUMERIC(6,2),
    temperature NUMERIC(5,2)
);

CREATE TABLE IF NOT EXISTS raw.fact_orders (
    order_id          SERIAL PRIMARY KEY,
    customer_id       INT REFERENCES raw.dim_customers(customer_id),
    product_id        INT REFERENCES raw.dim_products(product_id),
    order_date        DATE,
    quantity          INT,
    delivery_status   TEXT,
    created_at        TIMESTAMP DEFAULT now()
);

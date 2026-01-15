CREATE TABLE warehouse.dim_city (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(50) UNIQUE,
    latitude NUMERIC(8,5),
    longitude NUMERIC(8,5)
);

CREATE TABLE warehouse.dim_customer (
    customer_id INT PRIMARY KEY,
    city_id INT REFERENCES warehouse.dim_city(city_id),
    signup_date DATE
);

CREATE TABLE warehouse.dim_product (
    product_id INT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC(10,2)
);

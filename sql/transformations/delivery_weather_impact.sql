DROP TABLE IF EXISTS warehouse.delivery_weather_impact;

CREATE TABLE warehouse.delivery_weather_impact AS
SELECT
    o.city_id,
    DATE(o.order_date) AS order_date,
    COUNT(*) AS total_orders,
    AVG(CASE 
            WHEN o.delivery_status = 'On-time' THEN 1 
            ELSE 0 
        END) AS on_time_rate,
    AVG(CASE 
            WHEN o.delivery_status = 'Cancelled' THEN 1 
            ELSE 0 
        END) AS cancellation_rate,
    AVG(o.delivery_minutes) AS avg_delivery_minutes,
    (w.rain_risk_flag * 0.6 + w.wind_risk_flag * 0.4) AS delivery_risk_index
FROM warehouse.fact_orders o
JOIN warehouse.agg_daily_weather w
    ON o.city_id = w.city_id
   AND DATE(o.order_date) = w.weather_date
GROUP BY
    o.city_id,
    DATE(o.order_date),
    w.rain_risk_flag,
    w.wind_risk_flag;


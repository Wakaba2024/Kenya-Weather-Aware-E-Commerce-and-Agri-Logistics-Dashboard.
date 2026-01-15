DROP TABLE IF EXISTS warehouse.agg_daily_weather;

CREATE TABLE warehouse.agg_daily_weather AS
SELECT
    city_id,
    DATE(forecast_datetime) AS weather_date,
    SUM(rain_mm) AS daily_rainfall_mm,
    COUNT(*) FILTER (WHERE rain_mm > 0) AS rain_hours,
    MAX(wind_speed) AS max_wind_speed,
    CASE
        WHEN SUM(rain_mm) >= 5
          OR COUNT(*) FILTER (WHERE rain_mm > 0) >= 3
        THEN 1 ELSE 0
    END AS rain_risk_flag,
    CASE
        WHEN MAX(wind_speed) >= 10
        THEN 1 ELSE 0
    END AS wind_risk_flag
FROM raw.fact_weather_forecast
GROUP BY city_id, DATE(forecast_datetime);
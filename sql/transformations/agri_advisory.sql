DROP TABLE IF EXISTS warehouse.agri_advisory;

CREATE TABLE warehouse.agri_advisory AS
SELECT
    city_id,
    weather_date,
    rolling_rain_7day AS rain_7day_mm,
    CASE
        WHEN rolling_rain_7day >= 20 THEN 'YES'
        ELSE 'NO'
    END AS planting_window_flag
FROM (
    SELECT
        city_id,
        weather_date,
        SUM(daily_rainfall_mm) OVER (
            PARTITION BY city_id
            ORDER BY weather_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS rolling_rain_7day
    FROM warehouse.agg_daily_weather
) t;

--- The t is a table alias for the subquery. SQL requires every subquery in the FROM clause to have a name so the outer query can reference it.


# Kenya Weather-Aware Logistics Risk Analytics

## Executive Summary

This project builds an end-to-end data analytics pipeline that
integrates **weather forecasts, customer data, product catalog, and
order transactions** to analyze logistics delivery risk in Kenya. Data
is ingested using Python (VS Code), transformed and modeled in
PostgreSQL (DBeaver), and visualized in Power BI.

The objective is to: - Understand how **weather impacts delivery
performance**. - Monitor **product sales trends and delivery
efficiency**. - Enable **data-driven logistics planning and agricultural
advisory insights**.

------------------------------------------------------------------------

## Architecture Overview

**1. Data Sources** - OpenWeather API → Weather Forecasts - FakeStore
API → Products - Synthetic API / Mock Data → Customers & Orders

**2. Ingestion Layer (VS Code)** - Python scripts using requests +
psycopg2 - Data loaded into PostgreSQL raw schema

**3. Warehouse Layer (PostgreSQL / DBeaver)** - Dimensional modeling -
Aggregations and risk metrics

**4. Visualization Layer (Power BI)** - KPIs - Risk trends - Product
analytics

------------------------------------------------------------------------


## Database Configuration

Example connection in db.py:

host = "localhost"\
database = "logistics"\
user = "postgres"\
password = "123456"

Make sure the database exists in PostgreSQL.

------------------------------------------------------------------------


## Dashboard Pages

### 1. Weather vs Delivery Performance

-   Rainfall vs delivery delays
-   Risk index trend
-   Wind impact analysis

### 2. Product Sales Analytics

-   Top 10 products by orders
-   Category revenue distribution
-   Quantity trends

### 3. Agricultural Advisory Panel

-   Rainfall trend
-   High rainfall alerts
-   Planning indicators

------------------------------------------------------------------------


## Results

-   Identified periods where rainfall increases delivery delays.
-   High wind speeds correlate with increased delivery risk.
-   Top-selling products drive majority of revenue.
-   Certain cities show consistently higher logistics risk.
-   Weather aggregation enables daily operational planning.

------------------------------------------------------------------------

## Key Takeaways

1.  Weather data significantly improves logistics risk forecasting.
2.  Aggregated models simplify analytics and improve performance.
3.  Power BI enables fast operational visibility.
4.  Data quality and referential integrity are critical.
5.  Modular ETL pipelines scale easily for new datasets.

------------------------------------------------------------------------

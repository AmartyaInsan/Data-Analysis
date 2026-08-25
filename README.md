# PT Aneka Sport — Sales & Inventory Data Pipeline

A data engineering capstone project built by a team of four. The pipeline
takes raw sales, customer, product, and inventory data and turns it into a
clean, analysis-ready warehouse.

## What this project does

Raw `.txt` exports are ingested, cleaned, and modeled into a star schema,
then aggregated into business-ready summaries:

1. **Ingest** — raw pipe-delimited `.txt` files loaded as-is (Bronze layer)
2. **Clean** — whitespace trimmed, empty strings converted to `NULL`,
   duplicate rows removed, columns cast to proper types (Silver layer)
3. **Model** — cleaned data reshaped into a **star schema**: dimension
   tables (`dim_product`, `dim_customer`, `dim_salesman`, `dim_location`,
   `dim_territory`) and fact tables (`fact_sales`,
   `fact_inventory_daily_balance`, `fact_inventory_aging`) (Gold layer)
4. **Aggregate** — summarized into CSV data marts for BI tools (Power BI
   dashboards included)
5. **Analyze** — SQL and PySpark queries answering business questions:
   product and salesperson performance, product segmentation, top-selling
   products, and profit margin by product

## Architecture

```
                    PT ANEKA SPORT
                         │
              Raw TXT / Source Data
                         │
                         ▼
                  ┌─────────────┐
                  │   BRONZE    │
                  │ Raw ingestion│
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   SILVER    │
                  │ Cleaned     │
                  │ Typed       │
                  │ Deduplicated│
                  │ Parquet     │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │    GOLD     │
                  │ Star Schema │
                  └──────┬──────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Data Mart              Spark SQL
              │                     │
              ▼                     ▼
          Power BI              KPI / Insights
```

## Tech stack

- **PySpark** — ETL, cleaning, and star-schema transformations
- **Parquet** — Silver and Gold layer storage
- **Spark SQL** — KPI and business-question queries
- **Power BI** — dashboards built on the data mart

## My contribution

I worked across the full pipeline, with primary ownership of:

- Raw data ingestion through to the Silver layer (parsing, cleaning,
  deduplication, type casting)
- The analysis phase — writing both PySpark-based queries and direct SQL
  to answer the business questions above

## Team

Group 4, NDDE2A 2026 — Winda Mailindra, Zaora Zulmianah Anah,
Fathan Nuha Octovan, Amartya Maulana Insan

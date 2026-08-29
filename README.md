# PT Aneka Sport — Sales & Inventory Data Pipeline

An end-to-end PySpark portfolio project that turns raw sales, customer, product, and inventory exports into an analysis-ready warehouse and Power BI data marts.

The pipeline follows a Bronze → Silver → Gold design:

1. **Bronze** — ingest pipe-delimited source exports as received.
2. **Silver** — trim whitespace, standardize nulls, remove exact duplicates, cast types, and parse dates.
3. **Gold** — create product, customer, salesman, location, and territory dimensions plus sales and inventory facts.
4. **Data marts** — export Power BI-ready summaries and KPI queries.

## Highlights

- 9 raw source tables and a star-schema warehouse
- PySpark transformations and Spark SQL KPI analysis
- Data profiling, primary-key checks, pipeline logging, and customer-name masking
- Power BI dashboards for sales and inventory analysis
- Portable notebook configuration: run locally or in Colab without a hard-coded Drive path

## Repository contents

| Path | Purpose |
| --- | --- |
| [`Portfolio_Sales_Inventory_Pipeline.ipynb`](Portfolio_Sales_Inventory_Pipeline.ipynb) | End-to-end ETL and analysis notebook |
| [`docs/data-contract.md`](docs/data-contract.md) | Source-to-warehouse model and validation rules |
| [`src/aneka_sport_pipeline/contracts.py`](src/aneka_sport_pipeline/contracts.py) | Testable raw-source header contract |
| [`data/README.md`](data/README.md) | Local data layout and privacy guidance |
| [`Data Presentation.pdf`](Data%20Presentation.pdf) | Project presentation and Power BI deliverable |

## Quick start

### Prerequisites

- Python 3.10+
- Java 8 or 11 (required by PySpark)
- The nine raw `.txt` files listed in [`data/README.md`](data/README.md)

### Set up

```bash
git clone https://github.com/AmartyaInsan/Data-Analysis.git
cd Data-Analysis
python -m venv .venv
```

Activate the environment, then install packages:

```bash
pip install -r requirements.txt
```

Place the supplied files in `data/raw/`. They are deliberately excluded from Git because they may contain confidential operational and customer information.

Point the notebook to the folder that contains `raw/`, `silver/`, `gold/`, and `datamart/`:

```bash
# macOS/Linux
export ANEKA_SPORT_DATA_ROOT="$PWD/data"

# PowerShell
$env:ANEKA_SPORT_DATA_ROOT = "$PWD/data"
```

Open the notebook with JupyterLab and run it top to bottom:

```bash
jupyter lab
```

For Colab, upload or mount your own data location and set `ANEKA_SPORT_DATA_ROOT` before running the path-configuration cell.

## Data model

The Gold layer contains:

- Dimensions: `dim_product`, `dim_customer`, `dim_salesman`, `dim_location`, `dim_territory`
- Facts: `fact_sales`, `fact_inventory_daily_balance`, `fact_inventory_aging`

See the [data contract](docs/data-contract.md) for grain, relationships, source fields, and validation expectations.

## Data quality and metric caveats

The pipeline detects exact duplicates and checks candidate primary keys. Before using the result for financial reporting, reconcile every invoice's calculated line total with the source header's `INVNETWTX`. In the supplied raw data, `INVNETWTX` is not consistently equal to `QTYSHIPPED × UNITPRICE`; its treatment of discounts and other adjustments must be confirmed with the source-system owner.

The current `sales_amount` field is therefore best described as **gross line sales** until that reconciliation rule is defined. The inventory-aging calculation should likewise be validated against the opening-balance business date before it is used as an audited stock-aging report.

## Privacy

Do not commit the full raw exports, generated Silver/Gold data, pipeline logs, or identifiable customer fields. The included `.gitignore` protects these local artifacts by default.

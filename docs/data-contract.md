# Data contract

## Warehouse model

| Gold table | Grain | Main business keys | Source |
| --- | --- | --- | --- |
| `dim_product` | One product | `product_id` | `tbl_master_product.ITEMNO` |
| `dim_customer` | One customer | `customer_id` | `tbl_master_customer.IDCUST` |
| `dim_salesman` | One salesman | `salesman_id` | `tbl_master_salesman.CODESLSP` |
| `dim_location` | One location | `location_id` | `tbl_master_location.LOCATION` |
| `dim_territory` | One territory | `territory_id` | `tbl_master_territory.Kode_Teritory` |
| `fact_sales` | Invoice line | `invoice_id`, `product_id` | Invoice header joined to invoice detail |
| `fact_inventory_daily_balance` | Product-location-day | `item_no`, `location`, `date` | Beginning balance plus inventory movements |
| `fact_inventory_aging` | Product-location-season-age bucket | `item_no`, `location`, `season`, `age_bucket` | Inventory movements and product season |

## Required raw-source fields

The executable header contract in [`src/aneka_sport_pipeline/contracts.py`](../src/aneka_sport_pipeline/contracts.py) checks the required source fields before transformation. The nine expected raw files are:

- `tbl_master_salesman.txt`
- `tbl_master_territory.txt`
- `tbl_master_product.txt`
- `tbl_master_location.txt`
- `tbl_master_customer.txt`
- `tbl_invoice_header.txt`
- `tbl_invoice_detail.txt`
- `tbl_inventory.txt`
- `tbl_inventory_beginning_balance.txt`

## Validation rules

1. Fail fast if a raw file has a missing required column.
2. Record source row counts, exact duplicate counts, and null/empty values before Silver transformations.
3. Keep rejected or failed casts in an audit output; do not silently convert invalid numeric/date values to null.
4. Validate dimension keys are unique and report orphan foreign keys in facts.
5. Treat invoice detail as a line-level fact. `INVUNIQ + ITEM` is a candidate business key, not a guaranteed unique key in the raw data.
6. Reconcile source header `INVNETWTX` with a documented net-sales calculation before reporting revenue as net sales.
7. Confirm the effective date of `tbl_inventory_beginning_balance` before combining it with movements and calculating aging.

## Metric definitions pending source-owner confirmation

- **Gross line sales:** `QTYSHIPPED × UNITPRICE`
- **Cost:** `EXTICOST`
- **Profit:** gross line sales minus cost
- **Net sales:** not yet defined in the project because the relationship between `INVNETWTX`, `INVDISC`, `INVDISCPER`, and line values has not been formally reconciled.

This distinction prevents a dashboard label from overstating the certainty of the financial metric.

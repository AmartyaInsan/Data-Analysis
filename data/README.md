# Local data layout

The original source exports are intentionally not versioned in this public repository. They include operational and customer information and should remain local.

Create this structure before running the notebook:

```text
data/
  raw/
    tbl_master_salesman.txt
    tbl_master_territory.txt
    tbl_master_product.txt
    tbl_master_location.txt
    tbl_master_customer.txt
    tbl_invoice_header.txt
    tbl_invoice_detail.txt
    tbl_inventory.txt
    tbl_inventory_beginning_balance.txt
  silver/      # created by the notebook
  gold/        # created by the notebook
  datamart/    # created by the notebook
  _logs/       # created by the notebook
```

Set `ANEKA_SPORT_DATA_ROOT` to the `data/` folder. See the root README for commands.

If you want to publish a runnable demonstration, add a separately approved, anonymized `data/sample/` dataset with preserved key relationships. Never publish the full raw exports by default.

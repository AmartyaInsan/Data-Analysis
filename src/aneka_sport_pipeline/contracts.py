"""Raw-file contracts used by the PT Aneka Sport pipeline."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

RAW_TABLE_REQUIRED_COLUMNS: dict[str, frozenset[str]] = {
    "tbl_master_salesman": frozenset({"CODESLSP", "NAMEEMPL"}),
    "tbl_master_territory": frozenset({"Kode_Teritory", "Description"}),
    "tbl_master_product": frozenset(
        {"ITEMNO", "DESC", "CATEGORY", "BRAND", "SEASONCRN", "SEASONEND", "UnitPrice"}
    ),
    "tbl_master_location": frozenset({"LOCATION", "DESC", "CITY", "STATE", "COUNTRY"}),
    "tbl_master_customer": frozenset(
        {"IDCUST", "NAMECUST", "NAMECITY", "CODESTTE", "CODECTRY", "CODETERR", "CODESLSP1"}
    ),
    "tbl_invoice_header": frozenset(
        {"INVUNIQ", "INVNUMBER", "CUSTOMER", "INVDATE", "LOCATION", "SALESPER1", "INVNETWTX"}
    ),
    "tbl_invoice_detail": frozenset(
        {"INVUNIQ", "ITEM", "QTYSHIPPED", "EXTICOST", "UNITPRICE", "INVDISC", "DISCPER"}
    ),
    "tbl_inventory": frozenset(
        {"LOCATION", "ITEMNO", "TRANSDATE", "QUANTITY", "TRANSCOST", "DOCNUM", "ENTRYSEQ", "LINENO"}
    ),
    "tbl_inventory_beginning_balance": frozenset(
        {"ITEMNO", "LOCATION", "QTYONHAND", "TOTALCOST", "SEASONCRN"}
    ),
}


class SchemaValidationError(ValueError):
    """Raised when a required source field is absent from a raw export."""


def parse_header(line: str) -> tuple[str, ...]:
    """Return trimmed field names from a pipe-pair-delimited source header."""
    return tuple(field.strip() for field in line.rstrip("\n").split("||"))


def validate_header(table_name: str, header: Iterable[str]) -> None:
    """Raise a clear error when the source header lacks required fields."""
    try:
        required = RAW_TABLE_REQUIRED_COLUMNS[table_name]
    except KeyError as error:
        raise SchemaValidationError(f"Unknown source table: {table_name}") from error

    missing = sorted(required.difference({column.strip() for column in header}))
    if missing:
        raise SchemaValidationError(
            f"{table_name} is missing required columns: {', '.join(missing)}"
        )


def validate_raw_file(table_name: str, path: str | Path) -> None:
    """Validate the first line of a raw source file against its table contract."""
    with Path(path).open(encoding="utf-8-sig") as source_file:
        validate_header(table_name, parse_header(source_file.readline()))

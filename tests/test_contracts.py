from aneka_sport_pipeline.contracts import (
    RAW_TABLE_REQUIRED_COLUMNS,
    SchemaValidationError,
    parse_header,
    validate_header,
)


def test_parse_header_trims_pipe_pair_delimited_fields():
    assert parse_header(" INVUNIQ || ITEM || QTYSHIPPED\\n") == (
        "INVUNIQ",
        "ITEM",
        "QTYSHIPPED",
    )


def test_header_contract_accepts_all_required_invoice_detail_fields():
    validate_header("tbl_invoice_detail", RAW_TABLE_REQUIRED_COLUMNS["tbl_invoice_detail"])


def test_header_contract_reports_missing_fields():
    try:
        validate_header("tbl_master_salesman", ["CODESLSP"])
    except SchemaValidationError as error:
        assert "NAMEEMPL" in str(error)
    else:
        raise AssertionError("Expected a missing-column validation error")

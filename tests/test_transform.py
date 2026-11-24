"""Start here. normalise_postcode is done for you: add a test for every rule you write."""
import pytest

from insurecraft_etl import transform as t


@pytest.mark.parametrize("raw, expected", [
    ("nr1 3ju", "NR1 3JU"),
    ("  NR13JU ", "NR1 3JU"),
    ("NR1", None),
    ("UNKNOWN", None),
    (None, None),
])
def test_normalise_postcode(raw, expected):
    assert t.normalise_postcode(raw) == expected


# TODO: test parse_mixed_date with all three formats and one it should reject.
# TODO: test clean_claims removes each kind of bad row (build a tiny DataFrame by hand).
# TODO: test build_claims_summary calculates total_paid, payment_count, days_to_report and days_open.

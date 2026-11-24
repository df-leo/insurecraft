"""Extract: one function per source. Each returns a DataFrame and does NO cleaning.

Keep an untouched copy of everything you extract (save_raw), so any run can be audited or replayed.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import requests
from sqlalchemy.engine import Engine

POSTCODES_API = "https://api.postcodes.io/postcodes"
POSTCODE_FIELDS = ["postcode", "region", "country", "admin_district", "latitude", "longitude"]


def extract_claims(engine: Engine) -> pd.DataFrame:
    """Return every row of claims_ops.claims, exactly as stored.

    Hint: pd.read_sql(sql, engine)
    """
    raise NotImplementedError("TODO")


def extract_claim_payments(engine: Engine) -> pd.DataFrame:
    """Return every row of claims_ops.claim_payments, exactly as stored."""
    raise NotImplementedError("TODO")


def extract_policyholders(path: str | Path) -> pd.DataFrame:
    """Read the policyholder export.

    Hint: read every column as text (dtype=str). The file mixes date formats and you will fix them later.
    """
    raise NotImplementedError("TODO")


def lookup_postcodes(postcodes: list[str], session: requests.Session | None = None,
                     offline_file: str | None = None, batch_size: int = 100) -> pd.DataFrame:
    """Look up postcodes on postcodes.io and return one row per postcode with POSTCODE_FIELDS as columns.

    - Use the bulk endpoint: POST {"postcodes": [...]} to POSTCODES_API, at most 100 per call.
    - Ask about each postcode once (de-duplicate first).
    - Postcodes the API cannot find should come back with empty columns, not disappear.
    - Accept a `session` argument so tests can pass in a fake one instead of calling the real API.
    - If `offline_file` is set, read that CSV snapshot instead (your trainer's fallback if the API is down).
    """
    raise NotImplementedError("TODO")


def save_raw(df: pd.DataFrame, name: str, raw_dir: str | Path) -> Path:
    """Write df to <raw_dir>/<name>.csv and return the path."""
    raise NotImplementedError("TODO")

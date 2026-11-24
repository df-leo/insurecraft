"""Load: write DataFrames to your group's analytics schema."""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from sqlalchemy.engine import Engine


def load_table(df: pd.DataFrame, table: str, engine: Engine, schema: str | None = None,
               if_exists: str = "replace") -> int:
    """Write df to schema.table and return the number of rows written.

    It must be safe to rerun: running the pipeline twice must not double the data.
    Hint: df.to_sql(..., if_exists="replace") inside `with engine.begin() as conn:`
    """
    raise NotImplementedError("TODO")


def save_processed(df: pd.DataFrame, name: str, processed_dir: str | Path) -> Path:
    """Write df to <processed_dir>/<name>.csv (you will upload claims_summary.csv to Databricks in week 4)."""
    raise NotImplementedError("TODO")

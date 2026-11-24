"""Settings come from a .env file (copy .env.example). Credentials never go in code or email."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    source_db_url: str
    target_db_url: str
    target_schema: str
    policyholders_csv: str
    pseudonym_salt: str
    as_of_date: str
    postcodes_offline_file: str | None
    raw_dir: str = "data/raw"
    processed_dir: str = "data/processed"


def get_settings() -> Settings:
    load_dotenv()
    return Settings(
        source_db_url=os.environ["SOURCE_DB_URL"],
        target_db_url=os.environ["TARGET_DB_URL"],
        target_schema=os.environ["TARGET_SCHEMA"],
        policyholders_csv=os.environ.get("POLICYHOLDERS_CSV", "data/policyholders.csv"),
        pseudonym_salt=os.environ["PSEUDONYM_SALT"],
        as_of_date=os.environ.get("AS_OF_DATE", "2026-10-31"),
        postcodes_offline_file=os.environ.get("POSTCODES_OFFLINE_FILE") or None,
    )

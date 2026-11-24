"""Run the InsureCraft ETL end to end:  python main.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from sqlalchemy import create_engine  # noqa: E402

from insurecraft_etl import extract, load, transform  # noqa: E402,F401
from insurecraft_etl.config import get_settings  # noqa: E402


def run() -> None:
    s = get_settings()
    source = create_engine(s.source_db_url)
    target = create_engine(s.target_db_url)

    # TODO 1. Extract claims, payments and policyholders; save raw copies.
    # TODO 2. Clean each source. Look up postcodes for the CLEANED policyholder postcodes.
    # TODO 3. Build claims_summary.
    # TODO 4. Load raw_claims, raw_claim_payments, raw_policyholders, raw_postcodes and claims_summary
    #         into s.target_schema, and save claims_summary.csv to s.processed_dir.
    # Print row counts at each step: they are your first data quality check.


if __name__ == "__main__":
    run()

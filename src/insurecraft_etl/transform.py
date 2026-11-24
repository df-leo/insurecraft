"""Transform: small functions you can test one at a time.

Write each rule down as you decide it. In week 5 you will rebuild exactly these rules in dbt (SQL),
and the two outputs must match.
"""
from __future__ import annotations

import hashlib
import re

import pandas as pd

# Canonical values. Map messy inputs to these, case- and whitespace-insensitively.
PERILS = ["Escape of water", "Storm", "Flood", "Theft", "Fire", "Accidental damage", "Subsidence"]
STATUSES = ["Open", "Settled", "Declined", "Closed", "Reopened"]
PRODUCTS = ["Buildings", "Contents", "Buildings & Contents"]
POSTCODE_RE = re.compile(r"^[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{2}$")

SUMMARY_COLUMNS = [
    "claim_id", "policy_ref", "product", "claim_type", "peril", "region", "local_authority", "latitude",
    "longitude", "loss_date", "reported_date", "days_to_report", "status", "days_open", "total_paid",
    "payment_count",
]


def normalise_postcode(value) -> str | None:
    """WORKED EXAMPLE. Upper-case, remove spaces, re-insert the space before the last three characters,
    then validate against POSTCODE_RE. Anything invalid or blank becomes None."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    compact = str(value).upper().replace(" ", "")
    if not 5 <= len(compact) <= 7:
        return None
    candidate = f"{compact[:-3]} {compact[-3:]}"
    return candidate if POSTCODE_RE.match(candidate) else None


def parse_mixed_date(value) -> pd.Timestamp | None:
    """Parse '2021-03-04', '04/03/2021' or '04-Mar-2021'. Anything else becomes None.

    Never let pandas guess: is 04/03 the 4th of March or the 3rd of April? Use explicit formats.
    """
    raise NotImplementedError("TODO")


def pseudonymise(policy_id: str, salt: str) -> str:
    """Return a stable, non-reversible reference such as 'PH-1a2b3c4d5e6f'.

    Use: "PH-" + sha256(salt + policy_id).hexdigest()[:12]. The salt comes from your trainer so every
    group produces the same references.
    """
    raise NotImplementedError("TODO")


def clean_claims(claims: pd.DataFrame) -> pd.DataFrame:
    """Return valid claims only. Decide, test and document how you handle:
    exact duplicate rows; messy peril and status values (map to PERILS / STATUSES, e.g. 'CLSD' means Closed);
    missing loss or reported dates; reported dates before the loss date; repeated claim_ids.
    """
    raise NotImplementedError("TODO")


def clean_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """Return valid payments. Watch for exact duplicates and missing amounts.
    Negative amounts are recoveries (money coming back): should they stay?"""
    raise NotImplementedError("TODO")


def clean_policyholders(policyholders: pd.DataFrame) -> pd.DataFrame:
    """Return one row per policy with policy_id, product, postcode (normalised) and start_date (parsed).
    Names and dates of birth must NOT leave this function."""
    raise NotImplementedError("TODO")


def clean_postcodes(lookup: pd.DataFrame) -> pd.DataFrame:
    """Return postcode, region, local_authority, latitude, longitude.
    Hint: postcodes.io only gives a region for England. What should Scotland, Wales and Northern Ireland show?"""
    raise NotImplementedError("TODO")


def build_claims_summary(claims: pd.DataFrame, payments: pd.DataFrame, policyholders: pd.DataFrame,
                         postcodes: pd.DataFrame, as_of: str, salt: str) -> pd.DataFrame:
    """One row per claim with SUMMARY_COLUMNS (see docs/brief.md for definitions).

    - total_paid and payment_count come from the cleaned payments (0 when a claim has none).
    - days_to_report = reported_date - loss_date.
    - days_open = closed_date - reported_date for closed claims, otherwise as_of - reported_date.
    - policy_ref replaces policy_id.
    """
    raise NotImplementedError("TODO")

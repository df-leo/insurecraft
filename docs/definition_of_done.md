# Definition of Done (week 3)

- [ ] `python main.py` runs end to end without errors.
- [ ] `pytest` passes, with at least one test per transform rule and one extract test that does not call the real API.
- [ ] Running the pipeline twice gives the same row counts (no duplicated data).
- [ ] `claims_summary` has exactly the columns in the brief, one row per claim, and no names, dates of birth or policy ids.
- [ ] Raw tables (`raw_claims`, `raw_claim_payments`, `raw_policyholders`, `raw_postcodes`) and `claims_summary` are in your group's schema.
- [ ] `data/processed/claims_summary.csv` exists (you will need it in week 4).
- [ ] No credentials in the code or the repository; `.env` is not committed.
- [ ] The README explains how to run the pipeline and lists the cleaning rules you chose.

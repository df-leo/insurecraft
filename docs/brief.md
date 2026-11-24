# InsureCraft — Week 3: Into the analytical space

## The client
InsureCraft is a UK home insurer offering buildings and contents cover. Its claims team cannot yet trust its own numbers: claims sit in an operational system, policyholder details arrive as a file export, and nobody can say reliably where claims happen or how long they take. Your group is InsureCraft's data team. Your job is to give the claims team one trusted table they can analyse.

## Your task
Build a Python pipeline that extracts three messy sources, cleans and joins them, and loads a `claims_summary` table into your group's analytics schema. The pipeline must run end to end with one command and be safe to rerun.

| Source | Where | What to watch for |
| --- | --- | --- |
| Operational claims system | Postgres, schema `claims_ops`, tables `claims` and `claim_payments` (read only) | Duplicate rows, messy peril and status values, missing or impossible dates, missing payment amounts |
| Policyholder export | `data/policyholders.csv` (from your trainer) | Mixed date formats, inconsistent casing and spacing, duplicates, invalid postcodes |
| postcodes.io | `https://api.postcodes.io/postcodes` (bulk lookup, no key) | Maximum 100 postcodes per call; some postcodes are not found |

## The target: `claims_summary` (one row per valid claim)

| Column | Definition |
| --- | --- |
| claim_id | From the claims system |
| policy_ref | Pseudonymised policy reference (see hints). Never the raw policy id |
| product | Buildings, Contents, or Buildings & Contents |
| claim_type | Buildings or Contents |
| peril | One of: Escape of water, Storm, Flood, Theft, Fire, Accidental damage, Subsidence |
| region, local_authority, latitude, longitude | From postcodes.io (England gives a region; elsewhere use the country) |
| loss_date, reported_date | Dates |
| days_to_report | reported_date minus loss_date |
| status | One of: Open, Settled, Declined, Closed, Reopened |
| days_open | closed_date minus reported_date for closed claims (Settled, Declined, Closed); otherwise the as-of date (31 October 2026) minus reported_date |
| total_paid | Sum of valid payments in pounds, including negative recoveries; 0 if none |
| payment_count | Number of valid payments; 0 if none |

## User stories
See `user_stories.md`. They are written for you so you can start building straight away.

## Definition of Done
See `definition_of_done.md`.

## Getting set up
1. Clone the starter repository (checkpoint `cp0-start`) and create a branch for your group.
2. Copy `.env.example` to `.env`. Your trainer gives you the database login, your schema (for example `w3_g2`) and the pseudonym salt.
3. Put `policyholders.csv` in `data/`.
4. `pip install -r requirements.txt`, then `pytest`. The worked example test should pass.

## Timings
- **Half day:** kick-off (45 min), sketch the pipeline in Mermaid (15 min), build the three extract functions with at least one test (2 hr 15 min), stand-up (15 min).
- **Full day:** transform in the morning, load in the early afternoon, then `main.py` end to end, README, show-and-tell and a short retro.

## Hints
- Read the CSV with `dtype=str`. Parse dates with explicit formats, never by guessing.
- Look up postcodes after cleaning them, and ask about each postcode only once.
- `policy_ref = "PH-" + sha256(salt + policy_id).hexdigest()[:12]`.
- Print row counts after every step. They are your first data quality check.
- Raw tables containing names would be access-restricted in a real organisation. Discuss: who should be able to see them?

## Hand-over
Before the end of the day, update your README with how to run the pipeline, the cleaning rules you chose and anything unfinished. Next week a different group will start from the reference version of this work, but your README is how your thinking travels.

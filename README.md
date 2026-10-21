# DofBank Internal Tools

Internal toolset for managing database schema migrations for the
DofBank Core Banking System (v2 upgrade project).

## Overview

Python-based scripts to transition account data, transaction
history, and customer records from the legacy Oracle 11g database
to the new PostgreSQL 14 backend.

Scripts are organized by migration phase and must be run in order.

## Requirements

- Python 3.9+
- psycopg2-binary
- SQLAlchemy 1.4
- python-dotenv
- tqdm

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Dry run — no writes to production
python migrate.py --phase 1 --dry-run

# Run a specific phase
python migrate.py --phase 2 --confirm

# Run all phases in sequence
python migrate.py --phase all --confirm

# Rollback last completed phase
python migrate.py --rollback --phase 2

# Validate output after migration
python validate.py --phase 1
```

## Migration Phases

| Phase | Description            | Status         |
|-------|------------------------|----------------|
| 1     | User accounts table    | ✅ Complete    |
| 2     | Transaction history    | ✅ Complete    |
| 3     | IBAN mapping           | 🔄 In Progress |
| 4     | Audit logs             | ⏳ Pending     |
| 5     | Archival data          | ⏳ Pending     |

## Directory Structure

```
dofbank-tools/
├── migrate.py              # Main migration runner
├── validate.py             # Post-migration validation
├── rollback.py             # Rollback utility
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── config/
│   ├── database.py         # DB connection settings
│   └── phases.py           # Phase definitions
├── phases/
│   ├── phase1_users.py
│   ├── phase2_transactions.py
│   └── phase3_iban.py
├── utils/
│   ├── logger.py
│   ├── checksums.py
│   └── validators.py
└── logs/                   # Runtime logs (gitignored)
```

## Notes

- Always run `--dry-run` before any live migration
- Phase 3 is unstable on datasets larger than 500k rows — use batch_size=100
- Do not run on production between 08:00 and 18:00
- All operations are logged to `./logs/migration.log`

## Contributing

Internal use only. Contact the DofBank DevOps team for access.

---

*DofBank Core Banking System — Migration Project 2024*
*Proprietary — Do not distribute*

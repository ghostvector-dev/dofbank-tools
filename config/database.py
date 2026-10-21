# Database Configuration — DofBank Migration Tool

import os
from dotenv import load_dotenv

load_dotenv()

# ── Target: PostgreSQL (new system) ──────────────────────────
DB_CONFIG = {
    "host":     os.getenv("PG_HOST", "localhost"),
    "port":     int(os.getenv("PG_PORT", 5432)),
    "name":     os.getenv("PG_NAME"),
    "user":     os.getenv("PG_USER"),
    "password": os.getenv("PG_PASS"),
}

# ── Source: Oracle 11g (legacy system) ───────────────────────
ORACLE_CONFIG = {
    "host": os.getenv("ORACLE_HOST", "localhost"),
    "port": int(os.getenv("ORACLE_PORT", 1521)),
    "sid":  os.getenv("ORACLE_SID", "DOFBANKPROD"),
    "user": os.getenv("ORACLE_USER"),
    "pass": os.getenv("ORACLE_PASS"),
}

#!/usr/bin/env python3
"""
phase1_users.py — Phase 1: User Account Migration
Migrates the user accounts table from Oracle to PostgreSQL.
DofBank Core Banking System — Migration Project 2024
"""

import logging
from config.database import DB_CONFIG, ORACLE_CONFIG
from utils.logger import get_logger

log = get_logger(__name__)

ORACLE_QUERY = """
    SELECT
        user_id,
        username,
        full_name,
        email,
        account_status,
        created_date,
        last_login
    FROM DOF_USERS
    WHERE account_status != 'DELETED'
    ORDER BY user_id
"""

PG_INSERT = """
    INSERT INTO users (
        legacy_id, username, full_name, email,
        status, created_at, last_login_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (username) DO NOTHING
"""


def run(dry_run: bool = True, batch_size: int = 500) -> dict:
    """
    Execute Phase 1 migration.
    Returns a summary dict with migrated/skipped/error counts.
    """
    log.info("Phase 1 starting — User accounts migration")
    log.info(f"Mode: {'DRY RUN' if dry_run else 'LIVE WRITE'}")
    log.info(f"Batch size: {batch_size}")

    summary = {"migrated": 0, "skipped": 0, "errors": []}

    # TODO: connect Oracle source
    # TODO: stream rows in batches
    # TODO: insert into PostgreSQL target
    # TODO: write checksum log

    log.info(f"Phase 1 complete — {summary}")
    return summary


if __name__ == "__main__":
    run(dry_run=True)

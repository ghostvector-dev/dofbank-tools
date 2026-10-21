#!/usr/bin/env python3
"""
phase3_iban.py — Phase 3: IBAN Mapping Migration
Maps legacy account numbers to new IBAN format.
DofBank Core Banking System — Migration Project 2024

STATUS: In Progress — estimated completion end of October 2024
"""

from config.database import DB_CONFIG, ORACLE_CONFIG
from utils.logger import get_logger
from utils.validators import validate_iban

log = get_logger(__name__)


def legacy_to_iban(account_number: str, branch_code: str) -> str:
    """
    Converts a DofBank legacy account number to the new IBAN format.
    Format: DOF-XXXX
    """
    numeric = ''.join(filter(str.isdigit, account_number))
    return f"DOF-{numeric.zfill(4)}"


def run(dry_run: bool = True, batch_size: int = 100) -> dict:
    """
    Execute Phase 3 migration.
    NOTE: Use batch_size=100 — larger batches cause timeout on current dataset size.
    """
    log.info("Phase 3 starting — IBAN mapping migration")
    log.warning("Phase 3 is unstable on datasets > 500k rows. Use batch_size=100.")

    summary = {"mapped": 0, "invalid": 0, "errors": []}

    # TODO: in progress
    log.info(f"Phase 3 status — {summary}")
    return summary


if __name__ == "__main__":
    run(dry_run=True)

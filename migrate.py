#!/usr/bin/env python3
"""
migrate.py — Main Migration Runner
DofBank Core Banking System — Migration Project 2024
"""

import sys
import argparse
from utils.logger import get_logger
from phases import phase1_users, phase2_transactions, phase3_iban

log = get_logger("migration-runner")


def parse_args():
    parser = argparse.ArgumentParser(description="DofBank Database Migration Tool")
    parser.add_argument(
        "--phase",
        choices=["1", "2", "3", "all"],
        required=True,
        help="Migration phase to run (1: Users, 2: Transactions, 3: IBAN, all: All sequential)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Execute in simulation mode without committing database changes",
    )
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Acknowledge execution on target PostgreSQL instance",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=500,
        help="Number of records per transaction batch (default: 500)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.dry_run and not args.confirm:
        log.error("Live runs require the --confirm flag. Use --dry-run for testing.")
        sys.exit(1)

    log.info("=" * 60)
    log.info("DofBank Core Banking Migration Orchestrator v2.1")
    log.info(f"Target Phase : {args.phase}")
    log.info(f"Mode         : {'DRY RUN' if args.dry_run else 'LIVE RUN'}")
    log.info("=" * 60)

    phases_to_run = []
    if args.phase in ["1", "all"]:
        phases_to_run.append(("Phase 1 (Users)", phase1_users.run))
    if args.phase in ["2", "all"]:
        phases_to_run.append(("Phase 2 (Transactions)", phase2_transactions.run))
    if args.phase in ["3", "all"]:
        phases_to_run.append(("Phase 3 (IBAN Mapping)", phase3_iban.run))

    for name, run_fn in phases_to_run:
        log.info(f"Starting {name}...")
        res = run_fn(dry_run=args.dry_run, batch_size=args.batch_size)
        log.info(f"Finished {name}. Result: {res}")

    log.info("All requested phases completed successfully.")


if __name__ == "__main__":
    main()

# utils/validators.py — Validation helpers for DofBank migration

import re


def validate_iban(iban: str) -> bool:
    """Validate DofBank internal IBAN format (e.g. DOF-0001) or standard IBAN."""
    cleaned = iban.strip().upper()
    if re.match(r"^DOF-\d{4}$", cleaned):
        return True
    return bool(re.match(r"^[A-Z]{2}\d{2}[A-Z0-9]{4,30}$", cleaned.replace(" ", "")))


def validate_account_status(status: str) -> bool:
    """Allowed account statuses in DofBank Core."""
    return status.upper() in {"ACTIVE", "DORMANT", "FROZEN", "PENDING_VERIFICATION"}

# utils/checksums.py — Data integrity checksums for migration tables

import hashlib


def compute_row_checksum(row_dict: dict) -> str:
    """Compute deterministic SHA-256 hash of sorted key-value pairs in a record."""
    serialized = "|".join(f"{k}:{str(v)}" for k, v in sorted(row_dict.items()))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def verify_batch_integrity(source_rows: list[dict], target_rows: list[dict]) -> bool:
    """Ensure records count and hashes match between Oracle source and PostgreSQL target."""
    if len(source_rows) != len(target_rows):
        return False
    source_hashes = {compute_row_checksum(r) for r in source_rows}
    target_hashes = {compute_row_checksum(r) for r in target_rows}
    return source_hashes == target_hashes

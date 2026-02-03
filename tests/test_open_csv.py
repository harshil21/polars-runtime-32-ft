"""Simple test which uses scan_csv and collects the result."""

from pathlib import Path

import polars as pl

CSV_PATH = Path(__file__).parent / "sample_csv.csv"


def test_scan_csv() -> None:
    """Test scan_csv and collect."""
    headers = pl.scan_csv(CSV_PATH).collect_schema().names()
    assert headers == ["Name", "Age", "Gender", "Occupation"], (
        f"Unexpected headers: {headers}"
    )

    scanned_df = pl.scan_csv(CSV_PATH, has_header=True, skip_rows_after_header=2)
    collected_df = scanned_df.collect()

    assert collected_df.shape == (2, 4)
    assert collected_df["Name"].to_list() == ["Charlie", "Diana"]
    assert collected_df["Age"].to_list() == [35, 28]
    assert collected_df["Gender"].to_list() == ["M", "F"]
    assert collected_df["Occupation"].to_list() == ["Teacher", "Designer"]


def test_selected_fields() -> None:
    """Test scan_csv with selected fields and collect."""
    scanned_df = pl.scan_csv(
        CSV_PATH,
        has_header=True,
        skip_rows_after_header=0,
    ).select(["Name", "Occupation"])
    collected_df = scanned_df.collect()

    assert collected_df.shape == (4, 2)
    assert collected_df["Name"].to_list() == ["Alice", "Bob", "Charlie", "Diana"]
    assert collected_df["Occupation"].to_list() == [
        "Nurse",
        "Engineer",
        "Teacher",
        "Designer",
    ]

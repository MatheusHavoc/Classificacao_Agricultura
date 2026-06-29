from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

LOGGER = logging.getLogger(__name__)


class DataValidationError(ValueError):
    """Raised when an input dataset does not match the expected contract."""


@dataclass(frozen=True)
class ProjectConfig:
    """Runtime configuration for the crop recommendation profiling pipeline."""

    project_name: str
    default_dataset: str
    target_column: str = "label"


CONFIG = ProjectConfig("Crop recommendation classification", "Crop_recommendation.csv")


def normalize_column_name(column: object) -> str:
    """Return a normalized column name."""
    return str(column).strip().lower().replace(" ", "_").replace("-", "_")


def load_dataset(
    path: str | Path, required_columns: Sequence[str] = ()
) -> pd.DataFrame:
    """Load CSV or Excel data with validation and normalized column names."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    LOGGER.info("Loading dataset from %s", dataset_path)
    suffix = dataset_path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(dataset_path)
    elif suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(dataset_path)
    else:
        raise DataValidationError(f"Unsupported file format: {suffix}")
    df = df.copy()
    df.columns = [normalize_column_name(column) for column in df.columns]
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    return df


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing-value metrics by column."""
    total_rows = len(df)
    summary = pd.DataFrame(
        {"column": df.columns, "missing_count": df.isna().sum().values}
    )
    summary["missing_pct"] = (
        0.0 if total_rows == 0 else summary["missing_count"] / total_rows
    )
    return summary.sort_values(
        ["missing_count", "column"], ascending=[False, True]
    ).reset_index(drop=True)


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return numeric descriptive statistics."""
    numeric_df = df.select_dtypes(include="number")
    return (
        pd.DataFrame()
        if numeric_df.empty
        else numeric_df.describe().transpose().reset_index(names="column")
    )


def crop_class_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return crop-label distribution when the expected target column is available."""
    if CONFIG.target_column not in df.columns:
        LOGGER.info(
            "Skipping crop class summary; missing optional column: %s",
            CONFIG.target_column,
        )
        return pd.DataFrame()
    return (
        df[CONFIG.target_column]
        .value_counts(dropna=False)
        .rename_axis(CONFIG.target_column)
        .reset_index(name="records")
        .sort_values("records", ascending=False)
    )


def run_pipeline(
    input_path: str | Path, output_dir: str | Path = "data/processed"
) -> dict[str, Any]:
    """Run local profiling and optional crop-label summaries for an available dataset."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    df = load_dataset(input_path)
    missing_summary(df).to_csv(output_path / "missing_summary.csv", index=False)
    numeric_summary(df).to_csv(output_path / "numeric_summary.csv", index=False)
    class_summary = crop_class_summary(df)
    if not class_summary.empty:
        class_summary.to_csv(output_path / "crop_class_summary.csv", index=False)
    metrics = {"row_count": int(len(df)), "duplicate_rows": int(df.duplicated().sum())}
    (output_path / "dataset_metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    LOGGER.info("Pipeline completed for %s", CONFIG.project_name)
    return {
        "rows": metrics["row_count"],
        "duplicate_rows": metrics["duplicate_rows"],
        "outputs": str(output_path),
    }


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entrypoint."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    parser = argparse.ArgumentParser(description=CONFIG.project_name)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="data/processed")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run_pipeline(args.input, args.output), indent=2))
    except Exception:
        LOGGER.exception("Pipeline failed")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

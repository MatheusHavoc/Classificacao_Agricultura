from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from crop_recommendation.pipeline import load_dataset, missing_summary, run_pipeline


def test_load_dataset_normalizes_columns(tmp_path):
    dataset = tmp_path / "sample.csv"
    pd.DataFrame({"Soil PH": [6.1, None], "Label": ["rice", "maize"]}).to_csv(
        dataset, index=False
    )
    df = load_dataset(dataset)
    assert list(df.columns) == ["soil_ph", "label"]


def test_missing_summary_counts_nulls():
    summary = missing_summary(pd.DataFrame({"a": [1, None]}))
    assert summary.loc[0, "missing_count"] == 1


def test_run_pipeline_writes_outputs(tmp_path):
    dataset = tmp_path / "sample.csv"
    output = tmp_path / "processed"
    pd.DataFrame({"n": [1, 2], "label": ["a", "b"]}).to_csv(dataset, index=False)
    result = run_pipeline(dataset, output)
    assert result["rows"] == 2
    assert (output / "dataset_metrics.json").exists()

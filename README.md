# Classificacao Agricultura - Crop Recommendation

This repository contains the original crop recommendation notebook and a new lightweight Python profiling layer under `src/crop_recommendation/`.

## What this PR changes

The notebook remains the source of the full supervised-learning workflow. The Python code added here does not retrain the models from the notebook. It provides:

- local CSV/Excel ingestion with explicit errors;
- normalized column names;
- missing-value and numeric profiling outputs;
- duplicate-row metrics;
- an optional `crop_class_summary.csv` when the dataset includes `label`;
- tests for ingestion and profiling behavior.

## Structure

```text
.
├── Classificacao_Agricultura2V.ipynb
├── data/
├── images/
├── notebooks/
├── src/crop_recommendation/
├── tests/
├── requirements.txt
└── README.md
```

## Dataset requirement

The expected local input is `data/raw/Crop_recommendation.csv`. That file is not committed. Without it, the pipeline cannot be executed end to end, although the code and tests can be reviewed.

## How to run when the dataset is available

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m crop_recommendation.pipeline --input data/raw/Crop_recommendation.csv --output data/processed
```

## Outputs

Always generated when the input file exists:

- `data/processed/missing_summary.csv`
- `data/processed/numeric_summary.csv`
- `data/processed/dataset_metrics.json`

Generated only when the expected target column exists:

- `data/processed/crop_class_summary.csv`

## Limitations and next steps

- Model training and LIME interpretation remain in the notebook.
- This PR does not invent saved models or production inference.
- Expected schema and target-class checks should be formalized later.

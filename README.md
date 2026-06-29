# Classificacao Agricultura - Crop Recommendation

Python portfolio project for crop recommendation classification. The original notebook is preserved, and reusable project code now lives in `src/crop_recommendation/`.

## Staff Data Engineer assessment

This is one of the stronger repositories because it has a complete supervised-learning storyline and interpretability with LIME. The engineering gaps were reproducibility, dependency management, tests and separation between exploration and reusable code.

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

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m crop_recommendation.pipeline --input data/raw/Crop_recommendation.csv --output data/processed
```

## Pipeline capabilities

- CSV/Excel ingestion with clear errors.
- Column normalization.
- Missing-value summary.
- Numeric profiling.
- Duplicate-row metrics.
- Output artifacts under `data/processed/`.

## Limitations and next steps

- The dataset is not committed and must be provided locally.
- Model training remains in the notebook and should be extracted in a later PR.
- Expected schema and target-class checks should be formalized.
- Metrics and model-selection criteria should be exported to reproducible reports.

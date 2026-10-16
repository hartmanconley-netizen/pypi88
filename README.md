# pypi88 — Data Investigation

Workspace for data investigation projects.

## Layout

- `data/` — raw and processed datasets (git-ignored by default)
- `notebooks/` — Jupyter notebooks, numbered by step
- `src/` — reusable helpers shared across notebooks
- `scripts/` — one-off analysis scripts

## Quickstart

1. Create a virtual environment and install dependencies:

   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Drop your dataset into `data/`
3. Open `notebooks/01_data_exploration.ipynb` and start digging

## Notes

- Data files are git-ignored on purpose so nothing large or sensitive gets
  committed by accident. To track a small dataset deliberately:
  `git add -f data/your-file.csv`

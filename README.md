# Biomedical Data Harmonization, Validation and Quality Platform

A reproducible biomedical data engineering platform for acquiring,
harmonizing, validating, and documenting public gene-expression datasets.

## Objectives

- Retrieve public gene-expression datasets from NCBI GEO.
- Preserve original source metadata and downloaded artifacts.
- Standardize biomedical metadata using configurable rules.
- Detect missing values, duplicates, inconsistencies, and invalid fields.
- Store structured data in PostgreSQL.
- Maintain provenance and transformation history.
- Generate automated data-quality reports.
- Expose datasets and quality metrics through FastAPI.

## Scientific scope

The initial project focuses on metadata harmonization and data quality.

It does not automatically perform biological normalization of gene-expression
measurements. Original expression measurements will be preserved.

## Technology stack

Python, Biopython, Pandas, NumPy, PostgreSQL, SQLAlchemy, Alembic,
FastAPI, Pydantic, Pytest, Ruff, Docker.

## Project status

Phase 1: Repository and environment setup.

## Development

Activate the virtual environment before running project commands:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run tests:

```powershell
pytest
```

Run code-quality checks:

```powershell
ruff check .
```

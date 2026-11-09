# Platform Architecture

## Main processing layers

1. External data sources: NCBI GEO.
2. Acquisition: GEO connectors and retrieval management.
3. Raw storage: original files, metadata, checksums and manifests.
4. Ingestion: parsing and structured intermediate representations.
5. Harmonization: configurable metadata standardization.
6. Validation: completeness, uniqueness, consistency, validity and references.
7. Database: PostgreSQL with raw, core, QA and audit schemas.
8. API: FastAPI endpoints for studies, samples and quality reports.

## Data integrity principles

- Never silently overwrite original source data.
- Preserve source metadata.
- Record transformations and their provenance.
- Keep metadata harmonization distinct from expression normalization.

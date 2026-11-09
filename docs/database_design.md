# Database Design

Planned PostgreSQL schemas:

## raw
- source_artifacts
- raw_studies
- raw_samples

## core
- studies
- samples
- platforms
- metadata_fields
- sample_metadata

## qa
- quality_checks
- quality_issues
- quality_reports

## audit
- processing_runs
- transformation_events
- harmonization_rules

Database models and migrations will be implemented in a later phase.

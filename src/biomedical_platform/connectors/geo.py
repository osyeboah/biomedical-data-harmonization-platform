"""Utilities for validating NCBI GEO accession identifiers."""

import re
from dataclasses import dataclass
from enum import StrEnum


class GeoAccessionType( StrEnum):
    """Supported NCBI GEO accession types."""

    SERIES = "GSE"
    SAMPLE = "GSM"
    PLATFORM = "GPL"


@dataclass(frozen=True)
class GeoAccession:
    """A validated GEO accession and its type."""

    value: str
    accession_type: GeoAccessionType


def parse_geo_accession(
    accession: str,
    expected_type: GeoAccessionType | str | None = None,
) -> GeoAccession:
    """Validate and parse a GEO accession identifier.

    This checks identifier format only. It does not verify that the
    accession exists in the NCBI GEO database.
    """
    if not isinstance(accession, str):
        raise TypeError("GEO accession must be a string.")

    normalized = accession.strip().upper()

    match = re.fullmatch(r"(GSE|GSM|GPL)([0-9]+)", normalized)

    if match is None:
        raise ValueError(f"Invalid GEO accession format: {accession!r}")

    accession_type = GeoAccessionType(match.group(1))

    if expected_type is not None:
        try:
            expected = GeoAccessionType(expected_type)
        except ValueError as exc:
            raise ValueError(
                f"Unsupported expected GEO accession type: {expected_type!r}"
            ) from exc

        if accession_type != expected:
            raise ValueError(
                f"Expected {expected.value} accession, "
                f"but received {accession_type.value}."
            )

    return GeoAccession(
        value=normalized,
        accession_type=accession_type,
    )

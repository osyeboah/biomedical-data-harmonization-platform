import pytest

from biomedical_platform.connectors.geo import (
    GeoAccession,
    GeoAccessionType,
    parse_geo_accession,
)


@pytest.mark.parametrize(
    ("accession", "expected_type"),
    [
        ("GSE12345", GeoAccessionType.SERIES),
        ("GSM12345", GeoAccessionType.SAMPLE),
        ("GPL12345", GeoAccessionType.PLATFORM),
    ],
)
def test_parse_valid_accessions(accession, expected_type):
    result = parse_geo_accession(accession)

    assert isinstance(result, GeoAccession)
    assert result.value == accession
    assert result.accession_type == expected_type


def test_accession_is_normalized():
    result = parse_geo_accession("  gse12345  ")

    assert result.value == "GSE12345"
    assert result.accession_type == GeoAccessionType.SERIES


@pytest.mark.parametrize(
    "accession",
    [
        "",
        "GSE",
        "GSMABC",
        "GPL-12345",
        "12345",
        "GDS12345",
        "GSE 12345",
    ],
)
def test_reject_invalid_accession_formats(accession):
    with pytest.raises(ValueError):
        parse_geo_accession(accession)


def test_reject_non_string_accession():
    with pytest.raises(TypeError):
        parse_geo_accession(12345)


def test_expected_type_matches():
    result = parse_geo_accession(
        "GSE12345",
        expected_type=GeoAccessionType.SERIES,
    )

    assert result.accession_type == GeoAccessionType.SERIES


def test_expected_type_mismatch():
    with pytest.raises(ValueError, match="Expected GSM"):
        parse_geo_accession(
            "GSE12345",
            expected_type=GeoAccessionType.SAMPLE,
        )


def test_reject_unsupported_expected_type():
    with pytest.raises(ValueError, match="Unsupported expected"):
        parse_geo_accession(
            "GSE12345",
            expected_type="GDS",
        )

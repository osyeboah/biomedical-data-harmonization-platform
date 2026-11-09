"""Initial project structure tests."""

def test_project_package_imports():
    import biomedical_platform

    assert biomedical_platform is not None


def test_application_entry_point_imports():
    from biomedical_platform.main import main

    assert callable(main)

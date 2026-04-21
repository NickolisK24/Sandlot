import sandlot


def test_package_imports() -> None:
    assert sandlot is not None


def test_version_is_string() -> None:
    assert isinstance(sandlot.__version__, str)


def test_version_matches_expected() -> None:
    assert sandlot.__version__ == "0.0.1"

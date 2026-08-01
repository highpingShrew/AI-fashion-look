from app.services.reference_loader import load_reference


def test_load_categories():
    categories = load_reference("categories")

    assert isinstance(categories, list)
    assert "top" in categories
    assert "bottom" in categories
    assert "shoes" in categories


def test_load_types():
    types = load_reference("types")

    assert isinstance(types, dict)
    assert "top" in types
    assert "shirt" in types["top"]


def test_load_colors():
    colors = load_reference("colors")

    assert isinstance(colors, list)
    assert "black" in colors
    assert "white" in colors


def test_load_patterns():
    patterns = load_reference("patterns")

    assert isinstance(patterns, list)
    assert "solid" in patterns


def test_load_fits():
    fits = load_reference("fits")

    assert isinstance(fits, list)
    assert "regular" in fits
    assert "oversized" in fits
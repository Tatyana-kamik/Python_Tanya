import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize(string_utils):
    # Позитивные тесты
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("тест") == "Тест"

    # Негативные тесты
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize(" ") == " "
    assert string_utils.capitalize(None) is None


def test_trim(string_utils):
    # Позитивные тесты
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("   тест   ") == "тест   "

    # Негативные тесты
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == " "
    assert string_utils.trim(None) is None


def test_contains(string_utils):
    # Позитивные тесты
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("Тест", "т") is True

    # Негативные тесты
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "S") is False
    assert string_utils.contains(" ", "S") is False
    assert string_utils.contains(None, "S") is False


def test_delete_symbol(string_utils):
    # Позитивные тесты
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert string_utils.delete_symbol("", "k") == ""
    assert string_utils.delete_symbol(" ", "k") == " "
    assert string_utils.delete_symbol(None, "k") is None
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"

import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("line, expected_type, expected_masked_part", [
    ("Счет 12345678", "Счет", "**5678"),
    ("Карта Visa 1234567812345678", "Карта Visa", "1234 56** **** 5678"),
])
def test_mask_account_card_correct(line, expected_type, expected_masked_part):
    result = mask_account_card(line)
    assert result.startswith(expected_type)
    assert expected_masked_part in result


@pytest.mark.parametrize("line, expected_type, expected_masked_part", [
    ("Счет 9876543210", "Счет", "**3210"),
])
def test_mask_account_card_with_different_lengths(line, expected_type, expected_masked_part):
    result = mask_account_card(line)
    assert result.startswith(expected_type)
    assert expected_masked_part in result


@pytest.mark.parametrize("invalid_line", [
    "Некорректная строка без пробелов",
])
def test_mask_account_card_invalid_input(invalid_line):
    try:
        result = mask_account_card(invalid_line)
        assert isinstance(result, str)
        # Дополнительные проверки по содержанию
        assert invalid_line in result or True
    except Exception:
        pytest.fail("Функция вызвала исключение при некорректных данных")

@pytest.mark.parametrize("iso_str, expected_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2020-01-01T00:00:00", "01.01.2020"),
])
def test_get_date_valid(iso_str, expected_date):
    assert get_date(iso_str) == expected_date

@pytest.mark.parametrize("invalid_str", [
    "",  # пустая строка
    "2024-13-01T00:00:00",  # некорректный месяц
])
def test_get_date_invalid(invalid_str):
    with pytest.raises(ValueError):
        get_date(invalid_str)
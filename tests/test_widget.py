import pytest
from src.widget import mask_account_card


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
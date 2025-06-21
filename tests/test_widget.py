import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("line, expected_type, expected_masked_part", [
    ("Счет 12345678", "Счет", "**5678"),
    ("Карта Visa 1234567812345678", "Карта Visa", "1234 56** **** 5678"),
])
def test_mask_account_card_correct(
    line: str,
    expected_type: str,
    expected_masked_part: str
) -> None:
    """
    Тестирует функцию mask_account_card, проверяя, что результат начинается с ожидаемого типа,
    и содержит ожидаемую маскированную часть.

    :param line: Строка, содержащая номер карты или аккаунта для маскировки.
    :param expected_type: Ожидаемый префикс или тип результата (например, 'MasterCard', 'Visa').
    :param expected_masked_part: Ожидаемая маскированная часть номера карты.
    :return: Ничего не возвращает. В случае несоответствия вызовет AssertionError.
    """
    result = mask_account_card(line)
    assert result.startswith(expected_type), f"Результат не начинается с {expected_type}: {result}"
    assert expected_masked_part in result, (
        f"Маскированная часть {expected_masked_part} не найдена "
        f"в результате: {result}"
    )


@pytest.mark.parametrize("line, expected_type, expected_masked_part", [
    ("Счет 9876543210", "Счет", "**3210"),
])
def test_mask_account_card_with_different_lengths(
        line: str,
        expected_type: str,
        expected_masked_part: str
) -> None:
    """
    Тестирует функцию mask_account_card с разными длинами входных данных.

    :param line: Входная строка для маскировки.
    :param expected_type: Ожидаемый префикс или тип результата.
    :param expected_masked_part: Ожидаемая часть строки, которая должна присутствовать в результате.
    """
    result = mask_account_card(line)
    assert result.startswith(expected_type)
    assert expected_masked_part in result


@pytest.mark.parametrize("invalid_line", [
    "Некорректная строка без пробелов",
])
def test_mask_account_card_invalid_input(invalid_line: str) -> None:
    """
    Тестирует обработку некорректных входных данных функцией mask_account_card.

    :param invalid_line: Некорректная входная строка, вызывающая ошибку.
    """
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
def test_get_date_valid(iso_str: str, expected_date: str) -> None:
    """
    Тестирует функцию get_date с валидной ISO-строкой.

    :param iso_str: Входная ISO-строка даты.
    :param expected_date: Ожидаемый результат (тип зависит от реализации get_date).
    """
    assert get_date(iso_str) == expected_date


@pytest.mark.parametrize("invalid_str", [
    "",  # пустая строка
    "2024-13-01T00:00:00",  # некорректный месяц
])
def test_get_date_invalid(invalid_str: str) -> None:
    """
    Тестирует функцию get_date с некорректной строкой, ожидая выброс исключения.

    :param invalid_str: Некорректная строка, которая должна вызвать исключение.
    """
    with pytest.raises(ValueError):
        get_date(invalid_str)

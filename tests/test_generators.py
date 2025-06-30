import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример данных для тестирования
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2020-01-01T00:00:00",
        "operationAmount": {
            "amount": "100.00",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Test USD transaction",
        "from": "Account1",
        "to": "Account2"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2020-01-02T00:00:00",
        "operationAmount": {
            "amount": "200.00",
            "currency": {"name": "EUR", "code": "EUR"}
        },
        "description": None,
        "from": "Account3",
        "to": "Account4"
    }
]


@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [1]),
    ("EUR", [2]),
    ("RUB", []),
])
def test_filter_by_currency(currency_code, expected_ids):
    result_ids = [tx["id"] for tx in filter_by_currency(transactions, currency_code)]
    assert result_ids == expected_ids


def test_filter_by_currency_empty():
    empty_list = []
    result = list(filter_by_currency(empty_list, 'USD'))
    assert result == []


def test_transaction_descriptions():
    descs = list(transaction_descriptions(transactions))
    assert descs == ["Test USD transaction", ""]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def format_card_number(number: int) -> str:
    """Форматирует число в строку вида 'XXXX XXXX XXXX XXXX'."""
    card_str = f"{number:016d}"
    return " ".join(card_str[i:i + 4] for i in range(0, 16, 4))


@pytest.mark.parametrize("start, stop, expected_numbers", [
    (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003"
            ]
    ),
    (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999"
            ]
    ),
])
def test_generate_range(start, stop, expected_numbers):
    """Проверка генерации номеров в диапазоне."""
    result = list(card_number_generator(start, stop))
    assert result == expected_numbers, f"Ожидали: {expected_numbers}, получили: {result}"


@pytest.mark.parametrize("start, stop", [
    (1, 1),
    (9999999999999999, 9999999999999999),
])
def test_single_value_range(start, stop):
    """Проверка генерации при диапазоне из одного числа."""
    result = list(card_number_generator(start, stop))
    expected = [format_card_number(start)]
    assert result == expected


def test_formatting_of_generated_numbers():
    """Проверка правильности форматирования каждого номера."""
    start = 1
    stop = 5
    for number in card_number_generator(start, stop):
        # Проверяем длину строки и наличие пробелов
        assert len(number) == 19, f"Неверная длина номера: {number}"
        parts = number.split()
        assert len(parts) == 4, f"Неверное количество групп: {number}"
        for part in parts:
            assert len(part) == 4 and part.isdigit(), f"Некорректная группа: {part}"


def test_end_of_generation():
    """Проверка завершения генератора после последнего числа."""
    start = 10
    stop = 12
    gen = card_number_generator(start, stop)

    # Получаем все значения
    results = list(gen)

    # Проверяем что генератор выдал правильные номера
    expected = [format_card_number(n) for n in range(start, stop + 1)]

    assert results == expected

    # После завершения генератора он не выдает новых значений
    with pytest.raises(StopIteration):
        next(gen)


# Можно добавить фикстуру для повторного использования диапазонов или настроек
@pytest.fixture
def small_range():
    return (1000, 1003)


def test_with_fixture(small_range):
    start, stop = small_range
    result = list(card_number_generator(start, stop))
    expected = [format_card_number(n) for n in range(start, stop + 1)]
    assert result == expected

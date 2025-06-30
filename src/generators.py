from typing import List, Dict, Iterator, Optional

def filter_by_currency(
    transactions: List[Dict],
    currency_code: str
) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по заданному коду валюты.

    Args:
        transactions (List[Dict]): список транзакций.
        currency_code (str): код валюты для фильтрации (например, 'USD').

    Returns:
        Iterator[Dict]: итератор по транзакциям с указанной валютой.
    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction

def transaction_descriptions(
    transactions: List[Dict]
) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions (List[Dict]): список транзакций.

    Returns:
        Iterator[str]: итератор описаний транзакций.
    """
    for transaction in transactions:
        description: Optional[str] = transaction.get("description")
        yield description if description is not None else ""


def card_number_generator(
    start: int,
    stop: int
) -> Iterator[str]:
    """
    Генерирует номера карт в формате 'XXXX XXXX XXXX XXXX' в диапазоне от start до stop включительно.

    Args:
        start (int): начальное число диапазона.
        stop (int): конечное число диапазона.

    Yields:
        str: номер карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for number in range(start, stop + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_num_str: str = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted: str = " ".join(card_num_str[i:i+4] for i in range(0, 16, 4))
        yield formatted

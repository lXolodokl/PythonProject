from .masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(line: str) -> str:
    """
    Маскирует номер карты или счета в единой строке.

    :param line: Исходная строка с типом и номером карты/счета
    :return: Строка с замаскированным номером
    """
    if line.startswith("Счет "):
        # счет
        *account_type, account_number = line.split()
        masked = get_mask_account(account_number)
        return f'{" ".join(account_type)} {masked}'
    else:
        # карта
        *card_type, card_number = line.split()
        masked = get_mask_card_number(card_number)
        return f'{" ".join(card_type)} {masked}'

def get_date(iso_datetime_str: str) -> str:
    """
    Переводит из формата "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ"
    """
    dt = datetime.fromisoformat(iso_datetime_str)
    return dt.strftime('%d.%m.%Y')
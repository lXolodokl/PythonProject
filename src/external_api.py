import os
import requests
from typing import Dict, Any


def get_exchange_rate(currency_code: str) -> float:
    """
    Получает текущий обменный курс для указанной валюты к рублю через внешний API.

    Аргументы:
        currency_code (str): Код валюты ('USD' или 'EUR').

    Возвращает:
        float: Текущий курс обмена валюты к рублю.
               В случае ошибки возвращает 0.0.
    """
    api_token = os.getenv('API_ACCESS_KEY')
    if not api_token:
        raise ValueError("Переменная окружения API_ACCESS_KEY не установлена.")

    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {
        "apikey": api_token
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        rates = data.get('rates', {})
        rate = rates.get(currency_code)
        if rate:
            return float(rate)
        else:
            return 0.0
    except requests.RequestException as e:
        print(f"Ошибка при получении курса валют: {e}")
        return 0.0


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Если валюта транзакции — USD или EUR, происходит обращение к API для получения курса и конвертация.
    Для других валют возвращается сумма как есть.

    Аргументы:
        transaction (Dict[str, Any]): Данные о транзакции, содержащие сумму и валюту.

    Возвращает:
        float: Сумма транзакции в рублях.

    Исключения:
        ValueError: если структура данных некорректна или отсутствует необходимая информация.
    """
    amount_info = transaction.get('operationAmount', {})

    amount = amount_info.get('amount')
    currency = amount_info.get('currency', {}).get('name')

    if amount is None or currency is None:
        raise ValueError("Некорректная структура данных о транзакции.")

    try:
        amount_value = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Некорректное значение суммы.")

    if currency == 'RUB':
        return amount_value
    elif currency in ('USD', 'EUR'):
        rate = get_exchange_rate(currency)
        return amount_value * rate
    else:
        # Для других валют можно оставить как есть или обработать по необходимости.
        return amount_value

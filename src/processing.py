from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Возвращает список транзакций, у которых ключ 'state' совпадает с переданным значением.

    :param data: список словарей с данными о транзакциях
    :param state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: отфильтрованный список транзакций
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Возвращает список транзакций, отсортированный по дате.

    :param data: список словарей с данными о транзакциях
    :param descending: если True, сортирует по убыванию даты; если False — по возрастанию
    :return: отсортированный список транзакций
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
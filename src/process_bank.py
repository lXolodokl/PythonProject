import re
from collections import Counter
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Поиск транзакций с использованием регулярных выражений.

    Args:
        data (list of dict): список транзакций.
        search (str): строка поиска.

    Returns:
        list of dict: список транзакций, у которых в описании есть искомая строка.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = [transaction for transaction in data if pattern.search(transaction.get('description', ''))]
    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчет количества операций по категориям.

    Args:
        data (list of dict): список транзакций.
        categories (list of str): список категорий для подсчета.

    Returns:
        dict: словарь {категория: количество}.
    """
    category_counts: Counter = Counter()
    for transaction in data:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break  # одна транзакция относится к одной категории
        else:
            category_counts['Другие'] += 1  # если ни одна категория не подошла
    return dict(category_counts)

import json
import os
from typing import List, Dict, Any

def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает файл JSON, содержащий список финансовых транзакций.

    Аргументы:
        file_path (str): Путь к файлу JSON.

    Возвращает:
        список словарей с данными о транзакциях.
        Если файл не найден, содержит некорректный JSON или не является списком,
        возвращается пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

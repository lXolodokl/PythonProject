"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.

Функции:
- read_transactions_from_csv: читает транзакции из CSV файла.
- read_transactions_from_excel: читает транзакции из Excel файла (.xlsx).
"""
import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Читает транзакции из CSV файла.

    Args:
        file_path (str): Путь к CSV файлу.

    Returns:
        List[Dict]: Список словарей, каждый из которых представляет транзакцию.
                     Если файл не найден или произошла ошибка, возвращается пустой список.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"Файл пустой или содержит только заголовки: {file_path}")
        return []
    except pd.errors.ParserError as e:
        print(f"Ошибка парсинга CSV файла {file_path}: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Читает транзакции из Excel файла (.xlsx).

    Args:
        file_path (str): Путь к Excel файлу.

    Returns:
        List[Dict]: Список словарей, каждый из которых представляет транзакцию.
                     Если файл не найден или произошла ошибка, возвращается пустой список.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except ValueError as e:
        # Например, если отсутствует openpyxl или файл поврежден
        print(f"Ошибка при чтении Excel файла {file_path}: {e}")
        return []

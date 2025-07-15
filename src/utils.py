import json
import logging
from typing import Any
from typing import Dict
from typing import List

from logging_config import utils_logger

logger = logging.getLogger('utils')


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
        utils_logger.info(f"Попытка чтения файла: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        utils_logger.info(f"Успешное чтение файла: {file_path}")
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Некорректный JSON в файле: {file_path}")
        return []
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []

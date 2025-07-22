import pytest
from src.process_bank import process_bank_search, process_bank_operations


def test_process_bank_search():
    data_sample = [
        {'description': 'Перевод с карты на карту'},
        {'description': 'Открытие вклада'},
        {'description': 'Перевод организации'},
    ]

    result = process_bank_search(data_sample, 'перевод')

    assert len(result) == 2


def test_process_bank_operations() -> None:
    data_sample = [
        {'description': 'Перевод с карты на карту'},
        {'description': 'Открытие вклада'},
        {'description': 'Перевод организации'},
        {'description': 'Перевод со счета на счет'}
    ]

    categories = ['перевод']
    result = process_bank_operations(data_sample, categories)

    assert result['перевод'] >= 1

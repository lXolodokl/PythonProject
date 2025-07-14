import pytest
from unittest.mock import patch, MagicMock
from src.utils import read_transactions
from src.external_api import convert_to_rub


def test_read_transactions_valid_file():
    # Предположим, что файл существует и содержит список транзакций.
    transactions = read_transactions('data/operations.json')
    assert isinstance(transactions, list)


def test_read_transactions_invalid_file():
    # Файл не существует или содержит некорректный JSON.
    result = read_transactions('data/nonexistent.json')
    assert result == []


@patch('src.external_api.requests.get')
def test_convert_to_rub_usd_eur(mock_get):
    # Мокаем ответ API для курса валют.

    mock_response = MagicMock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 75.0,
            'EUR': 85.0,
            'RUB': 1.0,
        }
    }

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    # Установка переменной окружения для API токена.
    with patch.dict('os.environ', {'API_ACCESS_KEY': 'test_token'}):
        transaction_usd = {
            'operationAmount': {
                'amount': '100',
                'currency': {'name': 'USD'}
            }
        }

        transaction_eur = {
            'operationAmount': {
                'amount': '100',
                'currency': {'name': 'EUR'}
            }
        }

        result_usd = convert_to_rub(transaction_usd)
        result_eur = convert_to_rub(transaction_eur)

        assert abs(result_usd - 7500) < 1e-6  # 100 USD * 75 курс
        assert abs(result_eur - 8500) < 1e-6  # 100 EUR * 85 курс
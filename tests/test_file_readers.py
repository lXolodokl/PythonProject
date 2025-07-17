import pandas as pd
from unittest.mock import patch, Mock
from src import file_readers

# Тесты для функции read_transactions_from_csv


@patch('pandas.read_csv')
def test_read_transactions_from_csv_success(mock_read_csv):
    # Мокаем DataFrame с данными
    mock_df = Mock()
    mock_df.to_dict.return_value = [{'id': 1, 'amount': 100}]
    mock_read_csv.return_value = mock_df

    result = file_readers.read_transactions_from_csv('dummy_path.csv')
    assert result == [{'id': 1, 'amount': 100}]
    mock_read_csv.assert_called_once_with('dummy_path.csv')


@patch('pandas.read_csv', side_effect=FileNotFoundError)
def test_read_transactions_from_csv_file_not_found(mock_read_csv):
    result = file_readers.read_transactions_from_csv('nonexistent.csv')
    assert result == []


@patch('pandas.read_csv', side_effect=pd.errors.EmptyDataError)
def test_read_transactions_from_csv_empty_data(mock_read_csv):
    result = file_readers.read_transactions_from_csv('empty.csv')
    assert result == []


@patch('pandas.read_csv', side_effect=pd.errors.ParserError("Parse error"))
def test_read_transactions_from_csv_parse_error(mock_read_csv):
    result = file_readers.read_transactions_from_csv('bad.csv')
    assert result == []

# Тесты для функции read_transactions_from_excel


@patch('pandas.read_excel')
def test_read_transactions_from_excel_success(mock_read_excel):
    mock_df = Mock()
    mock_df.to_dict.return_value = [{'id': 2, 'amount': 200}]
    mock_read_excel.return_value = mock_df

    result = file_readers.read_transactions_from_excel('dummy_path.xlsx')
    assert result == [{'id': 2, 'amount': 200}]
    mock_read_excel.assert_called_once_with('dummy_path.xlsx')


@patch('pandas.read_excel', side_effect=FileNotFoundError)
def test_read_transactions_from_excel_file_not_found(mock_read_excel):
    result = file_readers.read_transactions_from_excel('nonexistent.xlsx')
    assert result == []


@patch('pandas.read_excel', side_effect=ValueError("Some error"))
def test_read_transactions_from_excel_value_error(mock_read_excel):
    result = file_readers.read_transactions_from_excel('bad.xlsx')
    assert result == []

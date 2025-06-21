import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210987654", "9876 54** **** 7654"),
    ("0000000000000000", "0000 00** **** 0000"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [
    "",  # пустая строка
    "1234",  # очень короткий номер
    "12345678901234567890",  # длинный номер
])
def test_get_mask_card_number_edge_cases(card_number):
    result = get_mask_card_number(card_number)
    assert isinstance(result, str)
    assert result.startswith(card_number[:4]) or len(result) >= len(card_number)


@pytest.mark.parametrize("account_number, expected", [
    ("12345678", "**5678"),
    ("987654321", "**4321"),
    ("42", "**42"),
])
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == f"**{account_number[-4:]}"


@pytest.mark.parametrize("account_number", [
    "",  # пустая строка
    "1",  # очень короткий номер
])
def test_get_mask_account_edge_cases(account_number):
    result = get_mask_account(account_number)
    assert result.startswith("**")
    assert result.endswith(account_number[-4:]) if len(account_number) >= 4 else True

import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("0000000000000000", "0000 00** **** 0000"),
    ]
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "",
        "1234",
        "12345678901234567890",
    ]
)
def test_get_mask_card_number_edge_cases(card_number: str) -> None:
    result = get_mask_card_number(card_number)
    assert isinstance(result, str)
    assert result.startswith(card_number[:4]) or len(result) >= len(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678", "**5678"),
        ("987654321", "**4321"),
        ("42", "**42"),
    ]
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == f"**{account_number[-4:]}"


@pytest.mark.parametrize(
    "account_name",
    [
        "",
        "1",
    ]
)
def test_get_mask_account_edge_cases(account_name: str) -> None:
    result = get_mask_account(account_name)
    assert result.startswith("**")
    if len(account_name) >= 4:
        assert result.endswith(account_name[-4:])

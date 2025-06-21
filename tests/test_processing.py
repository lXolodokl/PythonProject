import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-11-30T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-02T11:30:00"},
        {"id": 4, "state": "CANCELLED", "date": "2023-10-15T08:45:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
    ]


@pytest.mark.parametrize("state_value,expected_ids",
                         [("EXECUTED", [1, 3, 5]),
                          ("PENDING", [2]),
                          ("CANCELLED", [4]),
                          ("NON_EXISTENT", [])])
def test_filter_by_state(sample_transactions, state_value, expected_ids):
    filtered = filter_by_state(sample_transactions, state=state_value)
    ids = [item['id'] for item in filtered]
    assert ids == expected_ids


def test_filter_by_state_default():
    data = [{"state": "EXECUTED"}, {"state": "PENDING"}]
    result = filter_by_state(data)
    assert all(item['state'] == 'EXECUTED' for item in result)


def test_sort_by_date_descending(sample_transactions):
    sorted_data = sort_by_date(sample_transactions)

    dates = [item['date'] for item in sorted_data]

    # Проверка порядка убывания дат
    for i in range(len(dates) - 1):
        assert dates[i] >= dates[i + 1]


def test_sort_by_date_ascending(sample_transactions):
    sorted_data = sort_by_date(sample_transactions, descending=False)
    dates = [item['date'] for item in sorted_data]
    for i in range(len(dates) - 1):
        assert dates[i] <= dates[i + 1]


def test_sort_with_same_dates():
    data = [
        {"date": "2023-12-01T10:00:00"},
        {"date": "2023-12-01T10:00:00"},
        {"date": "2023-11-30T09:59:59"}
    ]
    sorted_desc = sort_by_date(data)
    sorted_asc = sort_by_date(data, descending=False)
    assert sorted_desc[0]['date'] >= sorted_desc[1]['date']
    assert sorted_asc[0]['date'] <= sorted_asc[1]['date']
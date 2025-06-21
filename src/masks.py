def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер карты в виде строки.
    :return: Замаскированный номер карты в формате XXXX XX** **** XXXX.
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    :param account_number: Номер счета в виде строки.
    :return: Замаскированный номер счета в формате **XXXX.
    """
    return f"**{account_number[-4:]}"

import logging

from logging_config import masks_logger

logger = logging.getLogger('masks')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер карты в виде строки.
    :return: Замаскированный номер карты в формате XXXX XX** **** XXXX.
    """
    try:
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.info(f"Маскировка номера карты: {card_number} -> {masked}")
        return masked
    except Exception as e:
        masks_logger.error(f"Ошибка маскировки номера карты {card_number}: {e}")
        return ""


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    :param account_number: Номер счета в виде строки.
    :return: Замаскированный номер счета в формате **XXXX.
    """
    try:
        masked = f"**{account_number[-4:]}"
        masks_logger.info(f"Маскировка номера счета: {account_number} -> {masked}")
        return masked
    except Exception as e:
        masks_logger.error(f"Ошибка маскировки номера счета {account_number}: {e}")
        return ""

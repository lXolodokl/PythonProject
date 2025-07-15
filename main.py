from logging_config import utils_logger
from src.utils import read_transactions
from src.masks import get_mask_card_number, get_mask_account
import os

# Определение пути к файлу с транзакциями относительно расположения скрипта
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, 'data', 'operations.json')

transactions = read_transactions(json_path)
if __name__ == "__main__":
    utils_logger.info("Запуск программы")

    # Чтение транзакций из файла
    transactions = read_transactions('data/operations.json')

    for t in transactions:
        # Маскирование номера карты и счета
        card_masked = get_mask_card_number(t.get('card_number', ''))
        account_masked = get_mask_account(t.get('account_number', ''))

        # Логирование обработки каждой транзакции
        utils_logger.debug(f"Обработана транзакция: карта={card_masked}, счет={account_masked}")

    utils_logger.info("Завершение работы программы")

from logging_config import utils_logger
from src.utils import read_transactions
from src.file_readers import read_transactions_from_csv, read_transactions_from_excel
from src.masks import get_mask_card_number, get_mask_account
import os
import sys

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


# Импортируем функции из src/file_readers.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def main():
    # Пути к файлам в папке 'data'
    csv_file_path = 'data/transactions.csv'
    excel_file_path = 'data/transactions_excel.xlsx'

    try:
        # Чтение из CSV
        print("Чтение данных из CSV файла...")
        transactions_csv = read_transactions_from_csv(csv_file_path)
        print(f"Найдено {len(transactions_csv)} транзакций из CSV.")
        for transaction in transactions_csv:
            print(transaction)

        print("\n" + "-"*50 + "\n")

        # Чтение из Excel
        print("Чтение данных из Excel файла...")
        transactions_excel = read_transactions_from_excel(excel_file_path)
        print(f"Найдено {len(transactions_excel)} транзакций из Excel.")
        for transaction in transactions_excel:
            print(transaction)

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден. {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()

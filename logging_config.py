import logging
import os

# Путь к папке logs (предполагается, что она в корне проекта)
logs_dir = os.path.join(os.path.dirname(__file__), '.', 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Форматтер для логов
log_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

# Настройка логгера utils
utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)
utils_log_path = os.path.join(logs_dir, 'utils.log')
if not any(isinstance(h, logging.FileHandler) for h in utils_logger.handlers):
    utils_file_handler = logging.FileHandler(utils_log_path, mode='w', encoding='utf-8')
    utils_file_handler.setFormatter(log_formatter)
    utils_logger.addHandler(utils_file_handler)

# Настройка логгера masks
masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)
masks_log_path = os.path.join(logs_dir, 'masks.log')
if not any(isinstance(h, logging.FileHandler) for h in masks_logger.handlers):
    masks_file_handler = logging.FileHandler(masks_log_path, mode='w', encoding='utf-8')
    masks_file_handler.setFormatter(log_formatter)
    masks_logger.addHandler(masks_file_handler)

# Тестовые сообщения для проверки
if __name__ == "__main__":
    utils_logger.debug("Тестовое сообщение для utils.log")
    masks_logger.debug("Тестовое сообщение для masks.log")

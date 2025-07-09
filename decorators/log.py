import functools

def log(filename=None):
    """
    Декоратор для логирования вызовов функции и результатов её выполнения.

    Логирует имя функции и результат выполнения при успешном вызове.
    В случае возникновения ошибки Логирует имя функции, тип ошибки и входные параметры.

    Аргументы:
        filename (str, optional): Имя файла для записи логов.
            Если не задан, логи выводятся в консоль.

    Формат логов:
        При успешном выполнении:
            "<имя_функции> ok"
        При ошибке:
            "<имя_функции> error: <тип_ошибки>. Inputs: <args>, <kwargs>"

    Пример использования:
        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, 2)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as e:
                err_type = type(e).__name__
                message = (f"{func.__name__} error: {err_type}. "
                           f"Inputs: {args}, {kwargs}")
                _write_log(message, filename)
                raise
        return wrapper
    return decorator

def _write_log(message, filename):
    """
    Записывает сообщение в файл или выводит в консоль.

    Аргументы:
        message (str): Сообщение для записи.
        filename (str или None): Имя файла для записи, если None — вывод в консоль.
    """
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)

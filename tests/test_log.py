import pytest
from decorators.log import log


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


@log(filename="test.log")
def faulty_function(x: int) -> None:
    raise ValueError("Некорректное значение")


# Тестовая функция для успешного вызова
@log()
def add(a: int, b: int) -> int:
    return a + b


# Тестовая функция для выбрасывания исключения
@log()
def fail() -> None:
    raise RuntimeError("Ошибка")


def test_successful_log(capsys: pytest.CaptureFixture) -> None:
    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "add ok" in captured.out or "add ok" in open("mylog.txt").read()


def test_error_log(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(RuntimeError):
        fail()

    captured = capsys.readouterr()
    # Проверка наличия сообщения об ошибке в выводе или файле лога
    log_content = ""
    try:
        with open("mylog.txt", "r", encoding="utf-8") as f:
            log_content = f.read()
    except FileNotFoundError:
        pass

    assert "fail error:" in captured.out or "fail error:" in log_content

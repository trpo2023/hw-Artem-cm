import re
from datetime import datetime
from errors import MissingQuotesError, InvalidDateFormatError, MissingFieldError

def extract_data_from_description(description: str) -> tuple:
    """Извлекает данные (ФИО, название темы и дату) из строки с помощью регулярного выражения."""
    if '"' not in description:
        raise MissingQuotesError("Ошибка: строка без кавычек")

    pattern = r'"(.*?)"\s+"(.*?)"\s+(\d{4}\.\d{2}\.\d{2})'
    match = re.search(pattern, description)

    if not match:
        raise MissingFieldError("Строка должна содержать полное ФИО, название темы и дату выдачи.")

    return match.group(1).strip(), match.group(2).strip(), match.group(3).strip()

def parse_date(issue_date_str: str) -> datetime:
    """Преобразует строку с датой в объект datetime."""
    try:
        return datetime.strptime(issue_date_str, '%Y.%m.%d')  # Формат, который ожидается
    except ValueError:
        raise InvalidDateFormatError("Дата должна быть в формате гггг.мм.дд.")

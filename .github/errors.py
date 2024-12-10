# errors.py

class MissingQuotesError(ValueError):
    """Ошибка, возникающая при отсутствии кавычек вокруг ФИО или темы."""
    pass

class InvalidDateFormatError(ValueError):
    """Ошибка, возникающая при некорректном формате даты."""
    pass

class MissingFieldError(ValueError):
    """Ошибка, возникающая при отсутствии одного из полей (ФИО, темы или даты)."""
    pass

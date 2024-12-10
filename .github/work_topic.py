from parser_utils import extract_data_from_description, parse_date
from errors import MissingQuotesError, InvalidDateFormatError, MissingFieldError

class WorkTopic:
    """Класс для хранения информации о студенте, теме работы и дате выдачи."""
    
    def __init__(self, student_name: str, topic_name: str, issue_date):
        self.student_name = student_name
        self.topic_name = topic_name
        self.issue_date = issue_date

    def __repr__(self) -> str:
        """Возвращает строку с полным ФИО, названием темы и датой выдачи."""
        return f"{self.student_name} {self.topic_name} {self.issue_date.strftime('%Y.%m.%d')}"

class WorkTopicFactory:
    """Фабрика для создания объектов WorkTopic на основе строки описания."""

    def create_work_topic(self, description: str) -> WorkTopic:
        try:
            student_name, topic_name, issue_date_str = extract_data_from_description(description)
            issue_date = parse_date(issue_date_str)
            return WorkTopic(student_name, topic_name, issue_date)
        except MissingQuotesError as e:
            raise MissingQuotesError(f"Ошибка при обработке строки '{description}': {e}")
        except InvalidDateFormatError as e:
            raise InvalidDateFormatError(f"Ошибка в формате даты: {e}") from e
        except Exception as e:
            raise MissingFieldError(f"Ошибка при обработке строки '{description}': {e}") from e

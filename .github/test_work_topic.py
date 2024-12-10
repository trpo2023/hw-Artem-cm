import unittest
from work_topic import WorkTopicFactory
from errors import MissingQuotesError, InvalidDateFormatError, MissingFieldError
from datetime import datetime


class TestWorkTopicFactory(unittest.TestCase):

    def setUp(self):
        """Настройка фабрики перед тестами."""
        self.factory = WorkTopicFactory()

    def test_valid_description(self):
        """Тестируем корректную строку описания."""
        description = '"Иванов Иван Иванович" "Исследование алгоритмов" 2024.09.20'
        work_topic = self.factory.create_work_topic(description)
        self.assertEqual(work_topic.student_name, "Иванов Иван Иванович")
        self.assertEqual(work_topic.topic_name, "Исследование алгоритмов")
        self.assertEqual(work_topic.issue_date, datetime(2024, 9, 20))

    def test_missing_quotes(self):
        """Тестируем строку без кавычек."""
        description = 'Иванов Иван Иванович Исследование алгоритмов 2024.09.20'
        with self.assertRaises(MissingQuotesError, msg="Ошибка: строка без кавычек"):
            self.factory.create_work_topic(description)

    """def test_invalid_date_format(self):
        #Тестируем строку с некорректной датой.
        description = '"Иванов Иван Иванович" "Исследование алгоритмов" 20.09.2024'  # Некорректный формат
        with self.assertRaises(InvalidDateFormatError, msg="Ошибка: некорректный формат даты"):
            self.factory.create_work_topic(description)"""


    def test_missing_field(self):
        """Тестируем строку без даты."""
        description = '"Иванов Иван Иванович" "Исследование алгоритмов"'
        with self.assertRaises(MissingFieldError, msg="Ошибка: строка без даты"):
            self.factory.create_work_topic(description)


if __name__ == '__main__':
    unittest.main()

from work_topic import WorkTopicFactory
from file_utils import read_descriptions_from_file


def main():
    """
    Основная функция программы. Читает список строк из файла, создает объекты WorkTopic для каждого студента и выводит их.
    """
    file_path = 'input.txt'
    descriptions = read_descriptions_from_file(file_path)
    factory = WorkTopicFactory()

    for description in descriptions:
        try:
            work_topic = factory.create_work_topic(description)
            print(work_topic)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()

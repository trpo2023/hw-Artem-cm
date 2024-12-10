def read_descriptions_from_file(file_path: str) -> list:
    """
    Читает список строк описаний из файла.
    
    Args:
        file_path (str): Путь к файлу, содержащему описания.

    Returns:
        list: Список строк, каждая из которых представляет одно описание.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

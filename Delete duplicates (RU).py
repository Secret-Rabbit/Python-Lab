import os
from datetime import datetime

primary_part_name = "1"
secondary_part_name = "2"
file_extension = ".txt"
work_directory = f"{os.getcwd()}"

logs = str(datetime.now())


# Перечисляет все файлы с заданным расширением в указанной директории 
# и её подкаталогах.
def list_files(directory, extension):

    # Убедимся, что расширение начинается с точки
    if not extension.startswith("."):
        extension = "." + extension

    found_files = []

    # Проходим по всем элементам в директории и поддиректориях
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, заканчивается ли файл нужным расширением
            if file.endswith(extension):
                # Формируем относительный путь к файлу
                full_path = os.path.join(root, file).replace(directory, "")
                found_files.append(full_path)

    return found_files


def merge_unique_lists(*lists):
    """
    Объединяет несколько списков в один, удаляя дубликаты элементов

    :param lists: произвольное количество списков для объединения
    :return: новый список с уникальными элементами
    """
    # Множество для хранения уникальных элементов
    unique_elements = set()

    # Проходим по всем переданным спискам
    for lst in lists:
        # Добавляем элементы в множество (автоматически убирает дубли)
        unique_elements.update(lst)

    # Преобразуем множество обратно в список
    return list(unique_elements)


def compare_files(file_path1: str, file_path2: str) -> bool:
    """
    Сравнивает содержимое двух текстовых файлов.

    Параметры:
    file_path1 (str): путь к первому файлу
    file_path2 (str): путь ко второму файлу

    """
    try:
        # Открываем оба файла в режиме чтения
        with open(file_path1, "r", encoding="utf-8") as file1:
            content1 = file1.read()

        with open(file_path2, "r", encoding="utf-8") as file2:
            content2 = file2.read()

            # Сравниваем содержимое файлов
        return content1 == content2

    except FileNotFoundError:
        print("Один или оба файла не найдены")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False


primary_part_path = f"{work_directory}\\{primary_part_name}"
secondary_part_path = f"{work_directory}\\{secondary_part_name}"

primary_parts = list_files(primary_part_path, file_extension)
secondary_parts = list_files(secondary_part_path, file_extension)

unique_parts = merge_unique_lists(primary_parts, secondary_parts)
for unique_part in unique_parts:
    file_path1 = f"{primary_part_path}\\{unique_part}"
    file_path2 = f"{secondary_part_path}\\{unique_part}"
    if os.path.isfile(file_path1) and os.path.isfile(file_path2):
        result = compare_files(file_path1, file_path2)
        if result:
            os.remove(file_path2)
            logs += f"\nФайл «{unique_part}» был удалён во вторичном каталоге, так как является аналогичным в первичном каталоге"
    else:
        logs += f"\nФайл {unique_part} не найден в одном из каталогов"
with open("logs.txt", "a", encoding="utf-8") as file:
    file.write(f"{logs}\n\n\n")

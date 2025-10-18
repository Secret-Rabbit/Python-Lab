#### English 🇬🇧
**Python-Lab** is a repository containing Python scripts that it makes no sense to put in a separate repository.
#### Russian 🇷🇺
**Python-Lab** - это репозиторий, содержащий скрипты на Python, которые нет смысла помещать в отдельный репозиторий.

# [`Always-On-VPN.py`](</Always-On-VPN.py>)
#### English 🇬🇧
A script that will constantly check the built-in Windows VPN connection with a given name and interval and automatically reconnect it if it is not connected.
#### Русский 🇷🇺
Скрипт, который будет постоянно проверять встроенное в Windows VPN-соединение с заданным именем и интервалом и автоматически переподключать его, если оно не подключено. Русскоязычная версия [`Always-On-VPN (RU).py`](</Always-On-VPN (RU).py>).

# [`Delete duplicates.py`](</Delete duplicates.py>)
#### English 🇬🇧
A script that allows you to **delete** files with the same contents. It finds all files with the specified resolution in the primary and secondary directories and compares them, **deleting** those with the same contents. When working, the performed file manipulations are written to a file. logs.txt in the current directory. Files that are not found in one of the directories are also logged.

All parameters are configured directly in the script itself.:
| Parameter | Description |
| --- | --- |
| primary_part_name | Name of the primary directory. |
| secondary_part_name | Name of the secondary directory from which duplicates are being deleted** |
| file_extension | Extension of the files being checked |
| work_directory | Working directory (default is the current directory) |

#### Русский 🇷🇺
Скрипт, который позволяет **удалить** файлы с одинаковым содержимым. Он находит все файлы с заданным разрешением в первичном и вторичном каталогах и сравнивает их, **удаляя** те, содержимое которых одинаково. При работе проводимые манипуляции с файлами записывает в файл `logs.txt` в текущем каталоге. Файлы, которые не найдены ни в одном из каталогов, также регистрируются в журнале. Русскоязычная версия [`Delete duplicates (RU).py`](</Delete duplicates (RU).py>).

Все параметры настраиваются непосредственно в самом скрипте:
| Параметр | Описание |
| --- | --- |
| primary_part_name | Название первичного каталога. |
| secondary_part_name | Название вторичного каталога, из которого **удаляются** дубликаты |
| file_extension | Расширение проверяемых файлов |
| work_directory | Рабочий каталог (по умолчанию - текущий каталог)  |
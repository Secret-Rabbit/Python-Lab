import os
import json

# Папка с JSON-файлами локализации
locales_dir = "locales"

# Словарь: {category: {id: {lang: translation}}}
categorized_translations = {}

# Рекурсивная функция для обхода вложенных словарей
def flatten_json(d, parent_key=""):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key))
        else:
            items[new_key] = v.strip()
    return items

# Обработка всех файлов
languages = []
for filename in os.listdir(locales_dir):
    if filename.endswith(".json"):
        lang = filename.split(".")[0]
        languages.append(lang)
        with open(os.path.join(locales_dir, filename), "r", encoding="utf-8") as f:
            data = json.load(f)

        for category, content in data.items():
            if not isinstance(content, dict):
                continue
            if category not in categorized_translations:
                categorized_translations[category] = {}
            for key, value in content.items():
                full_key = f"{category}.{key}"
                if full_key not in categorized_translations[category]:
                    categorized_translations[category][full_key] = {}
                categorized_translations[category][full_key][lang] = value.strip()

# Генерация MediaWiki-текста
output_lines = []

for category, entries in categorized_translations.items():
    output_lines.append(f"== {category} ==")
    output_lines.append('{| class="wikitable"')
    header = "! ID" + "".join(f" !! {lang}" for lang in languages)
    output_lines.append(header)

    for key, lang_map in sorted(entries.items()):
        row = f"|-\n| {key}" + "".join(f" || {lang_map.get(lang, '')}" for lang in languages)
        output_lines.append(row)

    output_lines.append("|}")  # конец таблицы
    output_lines.append("")    # пустая строка между таблицами

# Сохраняем в файл
with open("localization_table.wiki", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("✅ MediaWiki-таблица сохранена в localization_table.wiki")

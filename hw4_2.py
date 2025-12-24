def get_cats_info(path):
    # Створюємо пустий список котів
    cats_list = []
    try:
        # Читаємо файл з данними у відповідному кодуванні
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо прочитанні значення за комами
                id, name, age = line.strip().split(',')
                # Присвоюємо отриманні значення відповідному ключу списку
                cats_list.append({
                    'id': id,
                    'name': name,
                    'age': age
                })
        # Повертаємо список
        return cats_list
    # Додаємо відповідні виключення 
    except ValueError:
        return f'Рядок не відповідає формату: {line.strip()}'
    except FileNotFoundError:
        return f'Файл не знайдено!'


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Відкриття файлу у режимі читання
            for line in file:  # Ітерація по кожному рядку у файлі
                cat_data = line.strip().split(',')  # Розбивка рядка за комами
                cat_info = {  # Створення словника із інформацією про кішку
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)  # Додавання інформації про кішку до списку
    except FileNotFoundError:  # Обробка помилки, якщо файл не знайдено
        print("Файл не найден.")  # Виведення повідомлення про помилку
        return  # Вихід із функції
    except Exception as e:  # Обробка будь-яких інших винятків
        print(f"Виникла помилка: {e}")  # Виведення повідомлення про помилку
        return  # Вихід із функції
    
    for cat in cats_info:  # Ітерація по кожній інформації про кішку
        print(cat)  # Виведення інформації про кішку



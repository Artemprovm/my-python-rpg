import os # Импортируем модуль для работы с путями
from PIL import Image # Импортируем библиотеку для открытия картинок
import customtkinter as ctk # Добавь импорт в начало shop.py

def start_trade(hero, info, BASE_DIR):
    # Вместо torg = input(...)
    dialog = ctk.CTkInputDialog(text="Что хочешь купить?", title="Лавка торговца")
    torg = dialog.get_input() 
    
    if torg is None or torg == "": # Если нажал "Отмена" или ничего не ввел
        return hero.money, hero.damage
    
    torg = torg.capitalize() # Чтобы "меч" превратился в "Меч"
    # ... остальной твой код без изменений ...

    if torg in info: # Если товар есть в базе данных
        price = info[torg]["Цена"] # Узнаем цену
        
        # Если товар НЕ "Зелье" И он УЖЕ есть в инвентаре
        if torg != "Зелье" and torg in hero.inventar:
            print(f"У вас уже есть {torg}! Зачем вам второй?") # Отказываем в покупке
            return hero.money, hero.damage # Возвращаемся в меню без изменений
        
        if hero.money >= price: # Если денег хватает
            hero.money -= price # Списываем золото
            hero.damage += info[torg].get("Урон", 0) # Добавляем урон сразу (как ты и хотел)
            hero.inventar.append(torg) # Добавляем предмет в список сумки
            print(f"Успешно! Куплен {torg}. Ваш общий урон: {hero.damage}") # Отчет
            
            try: # Пробуем показать картинку
                put = os.path.join(BASE_DIR, info[torg]["картинка"]) # Собираем путь к файлу
                img = Image.open(put) # Открываем картинку
                img.show() # Показываем её на экране
            except: # Если картинка не найдена или сломана
                print("Картинку не удалось загрузить.") # Выводим ошибку, но не вылетаем
        else: # Если денег меньше, чем цена
            print("Недостаточно золота!") # Сообщаем о бедности
    else: # Если товара с таким названием нет в словаре
        print("Такого товара нет в ассортименте.") # Ошибка ввода
    
    return hero.money, hero.damage # ВАЖНО: отдаем измененные деньги и урон обратно в главное меню


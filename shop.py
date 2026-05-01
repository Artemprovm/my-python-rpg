import os 
from PIL import Image 
import customtkinter as ctk 
from tkinter import messagebox
import strings # Импортируем файл с переводами

def start_trade(hero, info, BASE_DIR, app):
    # Короткая ссылка на перевод
    t = strings.TEXTS[app.lang]
    
    # 1. Диалог покупки
    dialog = ctk.CTkInputDialog(text=t["shop_ask"], title=t["shop_title"])
    torg_raw = dialog.get_input() 
    
    if torg_raw is None or torg_raw == "": 
        return hero.money, hero.damage
    
    # Логика поиска предмета (игрок может ввести на английском или русском)
    torg = torg_raw.capitalize()
    
    # Если ввели на английском (Sword), переводим обратно в ключ (Меч) для поиска в info
    if app.lang == "en":
        for ru_name, en_name in t["items"].items():
            if torg.lower() == en_name.lower():
                torg = ru_name
                break

    # 2. Проверка товара в базе данных info
    if torg in info: 
        price = info[torg]["Цена"] 
        display_name = t["items"].get(torg, torg) # Имя для вывода в сообщения
        
        # Проверка на дубликат
        if torg != "Зелье" and torg in hero.inventar:
            messagebox.showwarning(t["shop_title"], t["already_have"].format(display_name))
            return hero.money, hero.damage 
        
        # Проверка денег
        if hero.money >= price: 
            hero.money -= price 
            hero.damage += info[torg].get("Урон", 0) 
            hero.inventar.append(torg) 
            
            # Сообщение об успехе
            msg = t["buy_success"].format(display_name, hero.damage)
            messagebox.showinfo(t["shop_title"], msg)
            
            # Показ картинки
            try: 
                put = os.path.join(BASE_DIR, info[torg]["картинка"]) 
                img = Image.open(put) 
                img.show() 
            except: 
                print(t["img_err"]) 
        else: 
            messagebox.showwarning(t["shop_title"], t["no_gold"])
    else: 
        messagebox.showerror(t["shop_title"], t["no_item"])
    
    # ОБНОВЛЯЕМ ИНТЕРФЕЙС
    app.update_stats_ui()
    app.render_inventory()
    
    return hero.money, hero.damage

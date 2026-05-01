import os # Импортируем модуль для работы с путями файлов
import shop # Подключаем твой файл shop.py (торговец)
import hunt # Подключаем твой файл hunt.py (охота)
import casino # Подключаем казино
import customtkinter as ctk
import json # Подключаем json
import sqlite3
from tkinter import messagebox
import strings # Подключаем настройки

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_db():
    conn = sqlite3.connect("rpg_game.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saves (
            slot_id INTEGER PRIMARY KEY,
            name TEXT,
            hp INTEGER,
            money INTEGER,
            damage INTEGER,
            inventar TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- Класс Игрока ---
class Player:
    def __init__(self):
        self.name = "Герой"
        self.damage = 5
        self.money = 100
        self.hp = 100
        self.inventar = ["Зелье"]

# --- База данных предметов ---
info = {
    "Меч": {"Урон": 25, "Цена": 50, "картинка": "mech.png"},
    "Зелье": {"Урон": 0, "Цена": 20, "Лечение": 20, "картинка": "zelie.png"},
    "Лук": {"Урон": 20, "Цена": 40, "картинка": "luk.png"},
    "Нож": {"Урон": 10, "Цена": 20, "картинка": "nozh.png"}
}

class GameApp(ctk.CTk):
    def __init__(self, hero, lang="ru"): # Добавили lang
        super().__init__()
        self.hero = hero
        self.lang = lang
        
        # Берем перевод из strings.py
        t = strings.TEXTS[self.lang]
        
        self.title(t["app_title"])
        self.geometry("700x500")

        # 0. Выбор языка
        # Устанавливаем начальное слово в зависимости от кода языка
        if self.lang == "ru":
            initial_lang = "Русский"
        elif self.lang == "jp":
            initial_lang = "日本語"
        else:
            initial_lang = "English"

        self.lang_var = ctk.StringVar(value=initial_lang)
        self.lang_menu = ctk.CTkOptionMenu(
          self, 
          values=["Русский", "English", "日本語"], # Добавили японский в список
          command=self.change_language,
          variable=self.lang_var
        )
        self.lang_menu.pack(pady=10)


        # 1. Статус (ВАЖНО: Создаем ПЕРЕД вызовом update_stats_ui)
        self.stats_label = ctk.CTkLabel(self, text="", font=("Arial", 18, "bold"))
        self.stats_label.pack(pady=10)
        
        # 2. Кнопка сброса
        self.btn_reset = ctk.CTkButton(self, text=t["new_game"], command=self.reset_game, fg_color="red")
        self.btn_reset.pack(pady=10)

        # 3. Кнопки управления
        self.btn_shop = ctk.CTkButton(self, text=t["shop"], command=self.open_shop)
        self.btn_shop.pack(pady=5)  
        
        self.btn_hunt = ctk.CTkButton(self, text=t["hunt"], command=self.open_hunt)
        self.btn_hunt.pack(pady=5)

        self.btn_casino = ctk.CTkButton(self, text=t["casino"], command=self.open_casino)
        self.btn_casino.pack(pady=5)

        # 4. Сохранение
        self.btn_save = ctk.CTkButton(self, text=t["save_btn"], command=self.save_game)
        self.btn_save.pack(pady=5)

        # 5. Инвентарь
        self.inv_frame = ctk.CTkFrame(self)
        self.inv_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Теперь все виджеты созданы, можно обновлять их текст
        self.update_stats_ui()
        self.render_inventory()



    def change_language(self, choice):
     # 1. Меняем код языка в зависимости от выбора
     if choice == "Русский":
        self.lang = "ru"
     elif choice == "日本語" or choice == "Japanese": # Добавили японский
        self.lang = "jp"
     else:
        self.lang = "en"
    
     # 2. Обновляем заголовок окна
     self.title(strings.TEXTS[self.lang]["app_title"])
    
     # 3. Обновляем текст на всех кнопках
     t = strings.TEXTS[self.lang]
     self.btn_reset.configure(text=t["new_game"])
     self.btn_shop.configure(text=t["shop"])
     self.btn_hunt.configure(text=t["hunt"])
     self.btn_casino.configure(text=t["casino"])
     self.btn_save.configure(text=t["save_btn"])
    
     # 4. Обновляем интерфейс статуса и инвентарь
     self.update_stats_ui()
     self.render_inventory()

    def save_game(self):
        data_to_save = {
            "name": self.hero.name,
            "hp": self.hero.hp,
            "money": self.hero.money,
            "inventar": self.hero.inventar,
            "damage": self.hero.damage
        }
        save_path = os.path.join(BASE_DIR, "save.json")
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        
        # Используем перевод из strings.py
        t = strings.TEXTS[self.lang]
        
        from tkinter import messagebox
        # Берём ключи "save_title" и "save_file_ok"
        messagebox.showinfo(t["save_title"], t["save_file_ok"])


    def update_stats_ui(self):
        # Берем нужный перевод из файла strings.py
        t = strings.TEXTS[self.lang]
        
        if self.hero.hp <= 0:
            self.hero.hp = 0
            # Используем шаблон "hero_dead" из словаря
            death_text = t["hero_dead"].format(self.hero.name)
            self.stats_label.configure(text_color="red", text=death_text)
            self.btn_hunt.configure(state="disabled")
            self.btn_shop.configure(state="disabled")
        else:
            self.stats_label.configure(text_color=("black", "white"))
            
            # Используем шаблон "status_bar", где подставляются значения героя
            status = t["status_bar"].format(
                self.hero.name, 
                self.hero.hp, 
                self.hero.damage, 
                self.hero.money
            )
            
            self.stats_label.configure(text=status)
            self.btn_hunt.configure(state="normal")
            self.btn_shop.configure(state="normal")

    def reset_game(self):
        t = strings.TEXTS[self.lang] # Подключаем перевод
        
        # 1. Всплывающее окно с вопросом (Да/Нет)
        if messagebox.askyesno(t["confirm_title"], t["confirm_reset"]):
            
            # 2. Спрашиваем новое имя
            new_name = ctk.CTkInputDialog(text=t["new_hero_ask"], title=t["new_hero_title"]).get_input()
            
            # Сбрасываем статы (названия предметов оставляем как в БД — "Зелье")
            self.hero.hp = 100
            self.hero.money = 100
            self.hero.damage = 5
            self.hero.inventar = ["Зелье"]
            self.hero.name = new_name if new_name else ("Герой" if self.lang == "ru" else "Hero")

            # Удаляем старый файл сохранения
            save_path = os.path.join(BASE_DIR, "save.json")
            if os.path.exists(save_path):
                os.remove(save_path)

            # Обновляем всё
            self.update_stats_ui()
            self.render_inventory()
            messagebox.showinfo(t["info_title"], t["reset_success"])


    def render_inventory(self):
        for widget in self.inv_frame.winfo_children():
            widget.destroy()
        
        for i, item in enumerate(self.hero.inventar):
            # --- ПЕРЕВОД ТУТ ---
            # Ищем перевод в strings.py. Если слова нет, останется оригинал (item)
            display_name = strings.TEXTS[self.lang]["items"].get(item, item)
            
            # text=display_name — игрок видит перевод (например, Sword)
            # name=item — программа всё еще использует русский ключ (Меч) для логики
            btn = ctk.CTkButton(
                self.inv_frame, 
                text=display_name, 
                command=lambda name=item: self.use_item(name)
            )
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    def use_item(self, item_name):
        item_data = info.get(item_name, {})
        t = strings.TEXTS[self.lang] # Берем нужный язык
        
        # Переводим название предмета для вывода в сообщении
        # Например: "Зелье" -> "Potion"
        display_name = t["items"].get(item_name, item_name)

        if "Лечение" in item_data:
            self.hero.hp = min(100, self.hero.hp + item_data["Лечение"])
            self.hero.inventar.remove(item_name)
            
            # Сообщение об использовании (используем шаблоны из strings.py)
            messagebox.showinfo(t["health_title"], t["healed"].format(display_name))
            
            self.update_stats_ui()
            self.render_inventory()
        else:
            # Сообщение о том, что это оружие
            messagebox.showinfo(t["info_title"], t["is_weapon_msg"].format(display_name))

    def open_shop(self):
        # Добавляем self четвертым аргументом
        self.hero.money, self.hero.damage = shop.start_trade(self.hero, info, BASE_DIR, self)
        
        # Эти строки можно оставить, но в новом shop.py я их тоже добавил 
        # для автоматического обновления прямо во время покупки
        self.update_stats_ui()
        self.render_inventory()

    def open_casino(self):
        t = strings.TEXTS[self.lang] # Подключаем перевод
        
        if self.hero.hp <= 0:
            # Используем заголовок и сообщение из словаря
            messagebox.showwarning(t["dead_warning_title"], t["dead_casino_msg"])
            return
            
        # Если живой — пускаем играть
        casino.start_gamble(self.hero, self)

    def save_game(self):
        t = strings.TEXTS[self.lang] # Короткая ссылка на перевод
        
        # 1. Спрашиваем номер слота
        slot = ctk.CTkInputDialog(text=t["slot_ask"], title=t["save_title"]).get_input()
        
        if not slot or not slot.isdigit():
            messagebox.showwarning(t["err_title"], t["err_number"])
            return

        conn = sqlite3.connect("rpg_game.db")
        cursor = conn.cursor()
        inv_string = ",".join(self.hero.inventar)

        # 2. Сохраняем в БД
        cursor.execute('''
            INSERT OR REPLACE INTO saves (slot_id, name, hp, money, damage, inventar)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (int(slot), self.hero.name, self.hero.hp, self.hero.money, self.hero.damage, inv_string))
        
        conn.commit()
        conn.close()
        
        # 3. Сообщение об успехе
        messagebox.showinfo(t["save_title"], t["save_slot_ok"].format(slot))



    def open_hunt(self):
        t = strings.TEXTS[self.lang] # Подключаем перевод

        if self.hero.hp <= 0:
            # Используем ключи для предупреждения о смерти
            messagebox.showwarning(t["dead_warning_title"], t["dead_hunt_msg"])
            return 

        # Запускаем бой, передавая self (приложение) для доступа к языку и обновлению UI
        hunt.start_hunt(self.hero, self)
        
        # Сразу обновляем цифры на экране
        self.update_stats_ui()
        self.update_idletasks() 

        # Проверяем итог боя
        if self.hero.hp <= 0:
            self.hero.money = max(0, self.hero.money // 2)
            # Используем ключи для поражения
            messagebox.showerror(t["defeat_title"], t["defeat_msg"])
            self.update_stats_ui()


class SaveMenu(ctk.CTk):
    def __init__(self, lang="ru"): # Принимаем язык
        super().__init__()
        self.lang = lang
        t = strings.TEXTS[self.lang] # Ссылка на перевод
        
        self.title(t["load_title"])
        self.geometry("300x400")
        self.selected_slot = None  

        # Заголовок "Выберите слот"
        ctk.CTkLabel(self, text=t["slot_ask"], font=("Arial", 18)).pack(pady=20)

        # Создаем 3 кнопки для слотов
        for i in range(1, 4):
            # Текст кнопки: "Слот 1" / "Slot 1"
            slot_text = f"{t['slot_name']} {i}" 
            btn = ctk.CTkButton(self, text=slot_text, 
                               command=lambda s=i: self.choose_slot(s))
            btn.pack(pady=10)
            
        # Кнопка для новой игры
        ctk.CTkButton(self, text=t["new_game"], fg_color="gray",
                       command=lambda: self.choose_slot(None)).pack(pady=20)

    def choose_slot(self, slot):
        self.selected_slot = slot
        self.quit() # Используем quit, чтобы программа пошла дальше
        self.destroy() 



# --- ЗАПУСК ---
if __name__ == "__main__":
    init_db()  # Инициализируем базу данных
    hero = Player() # Создаем базового игрока

    # 1. Сначала спрашиваем язык через простое окошко
    root_init = ctk.CTk()
    root_init.withdraw()
    
    # Обновили текст, добавив /jp
    lang_choice = ctk.CTkInputDialog(
        text="Выберите язык / Choose language / 言語を選択 (ru/en/jp):", 
        title="Language"
    ).get_input()
    
    root_init.destroy()
    # Если игрок закрыл окно, ставим русский по умолчанию
    selected_lang = lang_choice.lower() if lang_choice and lang_choice.lower() in ['ru', 'en', 'jp'] else 'ru'


    # 2. Теперь открываем твое новое графическое меню слотов на выбранном языке
    menu = SaveMenu(lang=selected_lang)
    menu.mainloop()

    # 3. После того как меню закрылось, берем выбранный слот
    chosen_slot = menu.selected_slot

    # 4. Если слот выбран (не Новая игра), загружаем данные из БД
    if chosen_slot is not None:
        conn = sqlite3.connect("rpg_game.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, hp, money, damage, inventar FROM saves WHERE slot_id = ?", (chosen_slot,))
        row = cursor.fetchone()

        if row:
            hero.name, hero.hp, hero.money, hero.damage, inv_raw = row
            hero.inventar = inv_raw.split(",") if inv_raw else []
            print(f"Загружен герой из слота {chosen_slot}")
        conn.close()

    # 5. Наконец, запускаем саму игру, передавая героя и выбранный язык
    app = GameApp(hero, lang=selected_lang)
    app.mainloop()
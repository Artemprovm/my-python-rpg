import os # Импортируем модуль для работы с путями файлов
import shop # Подключаем твой файл shop.py (торговец)
import hunt # Подключаем твой файл hunt.py (охота)
import casino # Подключаем казино
import customtkinter as ctk
import json # Подключаем json
from tkinter import messagebox
#import strings # Подключаем словарь

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.title("Моя RPG Игра")
        self.geometry("700x500")

        # 1. Статус
        self.stats_label = ctk.CTkLabel(self, text="", font=("Arial", 18, "bold"))
        self.stats_label.pack(pady=10)
        
        # 2. Кнопка сброса
        self.btn_reset = ctk.CTkButton(self, text="🔄 Новая игра", command=self.reset_game, fg_color="red")
        self.btn_reset.pack(pady=10) # Добавляем pack, чтобы она всегда была на экране


        # 3. Кнопки управления
        self.btn_shop = ctk.CTkButton(self, text="🛒 Магазин", command=self.open_shop)
        self.btn_shop.pack(pady=5)  
        
        self.btn_hunt = ctk.CTkButton(self, text="⚔️ Охота", command=self.open_hunt)
        self.btn_hunt.pack(pady=5)

        self.btn_casino = ctk.CTkButton(self, text="🎰 Казино", command=self.open_casino)
        self.btn_casino.pack(pady=5)


        # 4. Инвентарь
        self.inv_frame = ctk.CTkFrame(self)
        self.inv_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.update_stats_ui()
        self.render_inventory()

        # Внутри класса GameApp в методе __init__
        self.btn_save = ctk.CTkButton(self, text="💾 Сохранить прогресс", command=self.save_game)
        self.btn_save.pack(pady=5) # pack() выводит кнопку на экран 


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
        
        from tkinter import messagebox
        messagebox.showinfo("💾 Сохранение", "Твой герой успешно записан в файл!")

    def update_stats_ui(self):
        if self.hero.hp <= 0:
            self.hero.hp = 0
            # Выводим имя даже после смерти, чтобы было понятно, кто пал
            self.stats_label.configure(text_color="red", text=f"❌ ГЕРОЙ {self.hero.name} ПОГИБ")
            self.btn_hunt.configure(state="disabled")
            self.btn_shop.configure(state="disabled")
        else:
            self.stats_label.configure(text_color=("black", "white"))
            # Добавляем self.hero.name в самое начало строки
            status = f"👤 {self.hero.name} | ❤️ HP: {self.hero.hp} | ⚔️ Урон: {self.hero.damage} | 💰 Золото: {self.hero.money}"
            self.stats_label.configure(text=status)
            self.btn_hunt.configure(state="normal")
            self.btn_shop.configure(state="normal")

    def reset_game(self):
        # Всплывающее окно с выбором Да/Нет
        if messagebox.askyesno("Подтверждение", "Вы точно хотите начать новую игру? Весь прогресс будет удален!"):
            
            # Спрашиваем новое имя
            new_name = ctk.CTkInputDialog(text="Введите имя нового героя:", title="Новое приключение").get_input()
            
            # Сбрасываем статы
            self.hero.hp = 100
            self.hero.money = 100
            self.hero.damage = 5
            self.hero.inventar = ["Зелье"]
            self.hero.name = new_name if new_name else "Герой"

            # Удаляем старый файл сохранения
            save_path = os.path.join(BASE_DIR, "save.json")
            if os.path.exists(save_path):
                os.remove(save_path)

            # Обновляем всё
            self.update_stats_ui()
            self.render_inventory()
            messagebox.showinfo("Успех", "Мир обнулен. Удачи!")

    def render_inventory(self):
        for widget in self.inv_frame.winfo_children():
            widget.destroy()
        for i, item in enumerate(self.hero.inventar):
            btn = ctk.CTkButton(self.inv_frame, text=item, command=lambda name=item: self.use_item(name))
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    def use_item(self, item_name):
        item_data = info.get(item_name, {})
        if "Лечение" in item_data:
            self.hero.hp = min(100, self.hero.hp + item_data["Лечение"])
            self.hero.inventar.remove(item_name)
            messagebox.showinfo("Здоровье", f"Вы использовали {item_name}!")
            self.update_stats_ui()
            self.render_inventory()
        else:
            messagebox.showinfo("Инфо", f"{item_name} нельзя использовать, это оружие.")

    def open_shop(self):
        self.hero.money, self.hero.damage = shop.start_trade(self.hero, info, BASE_DIR)
        self.update_stats_ui()
        self.render_inventory()

    def open_casino(self):
     if self.hero.hp <= 0:
        messagebox.showwarning("Мертвец", "Мертвым деньги не нужны!")
        return 

    # Вызываем функцию и передаем в неё само окно (self)
     casino.start_gamble(self.hero, self)

    def save_game(self):
        data = {
            "name": self.hero.name,
            "hp": self.hero.hp,
            "money": self.hero.money,
            "inventar": self.hero.inventar,
            "damage": self.hero.damage
        }
        with open(os.path.join(BASE_DIR, "save.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    def open_hunt(self):
        if self.hero.hp <= 0:
            messagebox.showwarning("Мертвец", "Вы уже мертвы!")
            return 

        # Вызываем охоту ОДИН раз и передаем self
        hunt.start_hunt(self.hero, self)
        
        self.update_stats_ui()
        self.update_idletasks() 

        if self.hero.hp <= 0:
            messagebox.showerror("ПОРАЖЕНИЕ", "Вы погибли в бою!")

    def save_game(self):
        data = {
            "name": self.hero.name,
            "hp": self.hero.hp,
            "money": self.hero.money,
            "inventar": self.hero.inventar,
            "damage": self.hero.damage
        }
        with open(os.path.join(BASE_DIR, "save.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


# --- ЗАПУСК ---
hero = Player() # Создаем пустую заготовку
save_path = os.path.join(BASE_DIR, "save.json")

# Проверяем, есть ли файл сохранения
if os.path.exists(save_path):
    with open(save_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        # Заполняем данные героя из файла
        hero.name = data.get("name", "Герой")
        hero.hp = data.get("hp", 100)
        hero.money = data.get("money", 100)
        hero.inventar = data.get("inventar", ["Зелье"])
        hero.damage = data.get("damage", 5)

# Только теперь запускаем интерфейс с загруженными данными
app = GameApp(hero)
app.mainloop()

import random
import customtkinter as ctk
from tkinter import messagebox

# Добавляем app в аргументы функции
def start_hunt(hero, app): 
    monsters = {
        "Слизень": {"hp": 20, "dmg": 5, "min_g": 5, "max_g": 15},
        "Волк": {"hp": 50, "dmg": 12, "min_g": 20, "max_g": 45},
        "Огр": {"hp": 100, "dmg": 25, "min_g": 60, "max_g": 120}
    }

    name = random.choice(list(monsters.keys()))
    m_info = monsters[name]
    m_hp = m_info["hp"]
    
    dialog = ctk.CTkInputDialog(text=f"Враг: {name} (HP: {m_hp}, Урон: {m_info['dmg']})\nБой или Побег?", title="Враг!")
    choice_raw = dialog.get_input()
    choice = choice_raw.lower() if choice_raw else "побег"

    if choice == "побег":
        if random.random() < 0.5:
            messagebox.showinfo("Побег", "Вы успешно скрылись!")
            return hero.hp, hero.money
        else:
            messagebox.showwarning("Побег", f"Сбежать не удалось! {name} ударил!")
            hero.hp -= m_info["dmg"]
            app.update_stats_ui() # ОБНОВЛЯЕМ ЭКРАН СРАЗУ
            if hero.hp <= 0: return hero.hp, hero.money

    while m_hp > 0 and hero.hp > 0:
        battle_step = ctk.CTkInputDialog(text=f"Ваше HP: {hero.hp} | HP Врага: {m_hp}\nЖмите OK для атаки!", title="БИТВА")
        if battle_step.get_input() is None: break

        m_hp -= hero.damage
        
        if m_hp <= 0:
            gold_win = random.randint(m_info["min_g"], m_info["max_g"])
            hero.money += gold_win
            messagebox.showinfo("ПОБЕДА", f"{name} повержен!\nНаграда: {gold_win} золота.")
            break

        hero.hp -= m_info["dmg"]
        app.update_stats_ui() # ОБНОВЛЯЕМ ЭКРАН СРАЗУ, чтобы видеть как падает HP

        if hero.hp <= 0:
            messagebox.showerror("ПОРАЖЕНИЕ", f"Вы погибли в бою с {name}...")

    return hero.hp, hero.money


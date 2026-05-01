import random
import customtkinter as ctk
from tkinter import messagebox
import strings # или lang_settings

def start_hunt(hero, app): 
    t = strings.TEXTS[app.lang] # Берем перевод
    
    monsters = {
        "Слизень": {"hp": 20, "dmg": 5, "min_g": 5, "max_g": 15},
        "Волк": {"hp": 50, "dmg": 12, "min_g": 20, "max_g": 45},
        "Огр": {"hp": 100, "dmg": 25, "min_g": 60, "max_g": 120}
    }

    # Выбираем ключ (на русском), чтобы найти данные в словаре монстров
    name_key = random.choice(list(monsters.keys()))
    m_info = monsters[name_key]
    m_hp = m_info["hp"]
    
    # Переводим имя монстра для игрока
    display_name = t["monsters"].get(name_key, name_key)

    # 1. Первый выбор
    msg = t["fight_or_run"].format(display_name, m_hp, m_info['dmg'])
    dialog = ctk.CTkInputDialog(text=msg, title=t["enemy"] + "!")
    choice_raw = dialog.get_input()
    
    # Логика проверки ответа (на русском или английском)
    choice = choice_raw.lower() if choice_raw else "побег"
    is_run = choice in ["побег", "escape", "run", "п"]

    if is_run:
        if random.random() < 0.5:
            messagebox.showinfo(t["enemy"], t["run_success"])
            return hero.hp, hero.money
        else:
            messagebox.showwarning(t["enemy"], t["run_fail"].format(display_name))
            hero.hp -= m_info["dmg"]
            app.update_stats_ui()
            if hero.hp <= 0: return hero.hp, hero.money

    # 2. Цикл боя
    while m_hp > 0 and hero.hp > 0:
        battle_msg = t["battle_status"].format(hero.hp, m_hp)
        battle_step = ctk.CTkInputDialog(text=battle_msg, title=t["battle_title"])
        if battle_step.get_input() is None: break

        m_hp -= hero.damage
        
        if m_hp <= 0:
            gold_win = random.randint(m_info["min_g"], m_info["max_g"])
            hero.money += gold_win
            messagebox.showinfo(t["win_title"], t["win_hunt"].format(display_name, gold_win))
            break

        hero.hp -= m_info["dmg"]
        app.update_stats_ui()

        if hero.hp <= 0:
            messagebox.showerror(t["defeat_title"], t["defeat_hunt"].format(display_name))

    app.update_stats_ui()
    return hero.hp, hero.money

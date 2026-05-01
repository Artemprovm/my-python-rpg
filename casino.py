import random
import customtkinter as ctk
from tkinter import messagebox
import strings # Импортируем файл с переводами

def start_gamble(hero, app):
    # Короткая ссылка на словарь нужного языка
    t = strings.TEXTS[app.lang]
    
    # 1. Диалог ставки
    # Добавь ключи 'casino_welcome' и 'bet_ask' в strings.py или используй формат:
    msg = f"{t['casino_welcome']}\n{t['gold']}: {hero.money}\n\n{t['bet_ask']}"
    
    dialog = ctk.CTkInputDialog(text=msg, title=t["casino"])
    bet_input = dialog.get_input()

    if bet_input is None or bet_input.strip() == "":
        return hero.money

    if not bet_input.isdigit():
        messagebox.showwarning(t["err_title"], t["err_number"])
        return hero.money

    bet = int(bet_input)

    # 2. Проверки ставки
    if bet > hero.money:
        messagebox.showwarning(t["casino"], t["no_money"]) # Добавь 'no_money' в словарь
        return hero.money
    
    if bet <= 0:
        messagebox.showwarning(t["casino"], t["min_bet"]) # Добавь 'min_bet' в словарь
        return hero.money

    # 3. ИГРА
    chance = random.random()

    if chance < 0.4: # 40% шанс на победу
        win_money = bet
        hero.money += win_money 
        # Текст победы из словаря
        messagebox.showinfo(t["win_title"], t["win_msg"].format(win_money))
    else: 
        hero.money -= bet 
        # Текст проигрыша из словаря
        messagebox.showerror(t["lose_title"], t["lose_msg"].format(bet))

    # ОБНОВЛЯЕМ ИНТЕРФЕЙС
    app.update_stats_ui()
    
    return hero.money

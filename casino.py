import random
import customtkinter as ctk
from tkinter import messagebox

# Добавляем аргумент app, чтобы обновлять интерфейс
def start_gamble(hero, app):
    # Вместо print используем заголовок в диалоге
    dialog = ctk.CTkInputDialog(
        text=f"--- КАЗИНО 'УДАЧНЫЙ СЛИЗЕНЬ' ---\nУ вас в кошельке: {hero.money} золотых.\n\nСколько поставишь на кон?", 
        title="🎰 Казино"
    )
    bet_input = dialog.get_input()

    # Проверка на выход (если нажал "Cancel" или закрыл окно)
    if bet_input is None or bet_input.strip() == "":
        return hero.money

    # Проверка: число ли это
    if not bet_input.isdigit():
        messagebox.showwarning("Ошибка", "Нужно вводить только числа!")
        return hero.money

    bet = int(bet_input)

    # Проверки ставки
    if bet > hero.money:
        messagebox.showwarning("Казино", "У вас нет столько денег!")
        return hero.money
    
    if bet <= 0:
        messagebox.showwarning("Казино", "Ставка должна быть больше нуля!")
        return hero.money

    # --- ИГРА ---
    chance = random.random()

    if chance < 0.4: # 40% шанс на победу
        win_money = bet # Чистый выигрыш (игрок получает ставку назад + столько же сверху)
        hero.money += win_money 
        messagebox.showinfo("🎰 ПОБЕДА!", f"Поздравляем! Вы выиграли {win_money} золотых!")
    else: 
        hero.money -= bet 
        messagebox.showerror("🎰 ПРОИГРЫШ", f"Удача не на вашей стороне. Вы потеряли {bet}.")

    # ОБНОВЛЯЕМ ОКНО, чтобы золото изменилось сразу
    app.update_stats_ui()
    
    return hero.money

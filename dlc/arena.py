import customtkinter as ctk
from tkinter import messagebox

# Словарь переводов прямо внутри DLC
DLC_TEXTS = {
    "ru": {
        "welcome": "Добро пожаловать на арену! Ваш урон: {}",
        "win_title": "Победа",
        "win_msg": "Вы победили чемпиона арены! +200 золота",
        "lose_title": "Поражение",
        "lose_msg": "Вы слишком слабы для арены..."
    },
    "en": {
        "welcome": "Welcome to the Arena! Your damage: {}",
        "win_title": "Victory",
        "win_msg": "You defeated the Arena Champion! +200 gold",
        "lose_title": "Defeat",
        "lose_msg": "You are too weak for the Arena..."
    },
    "jp": {
        "welcome": "アリーナへようこそ！あなたの攻撃力: {}",
        "win_title": "勝利",
        "win_msg": "アリーナチャンピオンを倒しました！ +200 ゴールド",
        "lose_title": "敗北",
        "lose_msg": "アリーナに挑むには力不足です..."
    },
    "zh": {
        "welcome": "欢迎来到竞技场！你的攻击力: {}",
        "win_title": "胜利",
        "win_msg": "你击败了竞技场冠军！+200 黄金",
        "lose_title": "失败",
        "lose_msg": "对于竞技场来说，你太弱了..."
    }
}

def start_adventure(hero, app):
    # Берем язык из главного приложения. Если такого нет в DLC — берем английский.
    lang = getattr(app, 'lang', 'en')
    t = DLC_TEXTS.get(lang, DLC_TEXTS["en"])
    
    # Сообщение о входе
    messagebox.showinfo("Arena", t["welcome"].format(hero.damage))
    
    if hero.damage > 50:
        hero.money += 200
        messagebox.showinfo(t["win_title"], t["win_msg"])
    else:
        hero.hp -= 20 # Добавим штраф по ХП для интереса
        messagebox.showwarning(t["lose_title"], t["lose_msg"])
    
    # Обновляем интерфейс главного окна
    app.update_stats_ui()

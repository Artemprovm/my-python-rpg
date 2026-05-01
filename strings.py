# strings.py
TEXTS = {
    "ru": {
        # Интерфейс (Page 2)
        "app_title": "Моя RPG Игра",
        "new_game": "🔄 Новая игра",
        "shop": "🛒 Магазин",
        "hunt": "⚔️ Охота",
        "casino": "🎰 Казино",
        "save_btn": "💾 Сохранить прогресс",
        
        # Статусы и Бой (Page 3 & 5)
        "hero_dead": "ГЕРОЙ ❌ {} ПОГИБ",
        "status_bar": " 👤 {} | HP: ❤️ {} | Урон: ⚔️ {} | Золото: 💰 {}",
        "defeat_title": "ПОРАЖЕНИЕ",
        "defeat_msg": "Вы погибли и потеряли половину золота!",

        "load_title": "Загрузка",
        "load_ask": "Какой слот загрузить? (1, 2, 3...):",
        
        # Системные окна и Логика (Page 3, 4, 6)
        "confirm_title": "Подтверждение",
        "confirm_reset": "Вы точно хотите начать новую игру? Весь прогресс будет удален!",
        "new_hero_title": "Новое приключение",
        "new_hero_ask": "Введите имя нового героя:",
        "reset_success": "Мир обнулен. Удачи!",
        "save_title": "Сохранение",
        "save_file_ok": "Твой герой успешно записан в файл!", # для json
        "save_slot_ok": "Игра сохранена в слот №{}!", # для sqlite
        "slot_ask": "Введите номер слота (1, 2, 3):",
        "load_title": "Загрузка",
        "load_ask": "Какой слот загрузить? (1, 2, 3...):",
        "err_title": "Ошибка",
        "err_number": "Введите число (номер слота)!",
        "dead_warning_title": "Мертвец",
        "dead_hunt_msg": "Мертвые не охотятся! Сначала восстановите здоровье.",
        "dead_casino_msg": "Мертвым деньги не нужны!",

        "dead_warning_title": "Мертвец",
        "dead_hunt_msg": "Мертвые не охотятся! Сначала восстановите здоровье.",
        "defeat_title": "ПОРАЖЕНИЕ",
        "defeat_msg": "Вы погибли и потеряли половину золота!",        

        "casino_welcome": "--- КАЗИНО 'УДАЧНЫЙ СЛИЗЕНЬ' ---",
        "bet_ask": "Сколько поставишь на кон?",
        "gold": "Золото",  # Проверь, чтобы этот ключ был!
        "err_title": "Ошибка",
        "err_number": "Введите число!",
        "win_title": "🎰 ПОБЕДА!",
        "win_msg": "Поздравляем! Вы выиграли {} золотых!",
        "lose_title": "🎰 ПРОИГРЫШ",
        "lose_msg": "Удача не на вашей стороне. Вы потеряли {}.",
        "no_money": "У вас нет столько денег!",
        "min_bet": "Ставка должна быть больше нуля!",

        "enemy": "Враг",
        "fight_or_run": "Враг: {} (HP: {}, Урон: {})\nБой или Побег?",
        "run_success": "Вы успешно скрылись!",
        "run_fail": "Сбежать не удалось! {} ударил!",
        "battle_title": "БИТВА",
        "battle_status": "Ваше HP: {} | HP Врага: {}\nНажмите OK для атаки!",
        "win_hunt": "{} повержен!\nНаграда: {} золота.",
        "defeat_hunt": "Вы погибли в бою с {}...",
        "monsters": {
         "Слизень": "Слизень",
         "Волк": "Волк",
         "Огр": "Огр"
        },

        "confirm_title": "Подтверждение",
        "confirm_reset": "Вы точно хотите начать новую игру? Весь прогресс будет удален!",
        "new_hero_title": "Новое приключение",
        "new_hero_ask": "Введите имя нового героя:",
        "reset_success": "Мир обнулен. Удачи!",
        "info_title": "Инфо",

        "slot_name": "Слот",
        "new_game": "🔄 Новая игра",

        "health_title": "Здоровье",
        "healed": "Вы использовали {}!",
        "info_title": "Инфо",
        "is_weapon_msg": "{} нельзя использовать, это оружие.",

        "save_title": "Сохранение",
        "slot_ask": "Введите номер слота (1, 2, 3):",
        "err_title": "Ошибка",
        "err_number": "Введите число (номер слота)!",
        "save_slot_ok": "Игра сохранена в слот №{}!",

        "shop_title": "Лавка торговца",
        "shop_ask": "Что хочешь купить?",
        "already_have": "У вас уже есть {}! Зачем вам второй?",
        "buy_success": "Успешно! Куплен {}. Ваш общий урон: {}",
        "no_gold": "Недостаточно золота!",
        "no_item": "Такого товара нет в ассортименте.",
        "img_err": "Картинку не удалось загрузить.",
        
        # Предметы и Инвентарь (Page 1 & 4)
        "health_title": "Здоровье",
        "use_item_msg": "Вы использовали {}!",
        "info_title": "Инфо",
        "is_weapon_msg": "{} нельзя использовать, это оружие.",
        "items": {
            "Меч": "Меч",
            "Зелье": "Зелье",
            "Лук": "Лук",
            "Нож": "Нож"
        }
    },
    "en": {
        # Interface
        "app_title": "My RPG Game",
        "new_game": "🔄 New Game",
        "shop": "🛒 Shop",
        "hunt": "⚔️ Hunt",
        "casino": "🎰 Casino",
        "save_btn": "💾 Save Progress",
        
        # Stats & Combat
        "hero_dead": "HERO ❌ {} DIED",
        "status_bar": " 👤 {} | HP: ❤️ {} | DMG: ⚔️ {} | Gold: 💰 {}",
        "defeat_title": "DEFEAT",
        "defeat_msg": "You died and lost half of your gold!",

        "save_title": "💾 Сохранение",
        "save_file_ok": "Твой герой успешно записан в файл!",

        "load_title": "Loading",
        "load_ask": "Which slot to load? (1, 2, 3...):",
        
        # System Popups
        "confirm_title": "Confirmation",
        "confirm_reset": "Are you sure you want to start a new game? All progress will be deleted!",
        "new_hero_title": "New Adventure",
        "new_hero_ask": "Enter new hero name:",
        "reset_success": "World reset. Good luck!",
        "save_title": "Save",
        "save_file_ok": "Your hero has been successfully saved to file!",
        "save_slot_ok": "Game saved to slot #{}!",
        "slot_ask": "Enter slot number (1, 2, 3):",
        "load_title": "Load",
        "load_ask": "Which slot to load? (1, 2, 3...):",
        "err_title": "Error",
        "err_number": "Please enter a number (slot ID)!",
        "dead_warning_title": "Dead Man",
        "dead_hunt_msg": "The dead don't hunt! Restore health first.",
        "dead_casino_msg": "The dead don't need money!",

        "confirm_title": "Confirmation",
        "confirm_reset": "Are you sure you want to start a new game? All progress will be lost!",
        "new_hero_title": "New Adventure",
        "new_hero_ask": "Enter new hero name:",
        "reset_success": "World has been reset. Good luck!",
        "info_title": "Info",

        "save_title": "💾 Save",
        "save_file_ok": "Your hero has been successfully saved to the file!",

        "casino_welcome": "--- 'LUCKY SLIME' CASINO ---",
        "bet_ask": "How much will you bet?",
        "gold": "Gold",
        "err_title": "Error",
        "err_number": "Please enter a number!",
        "win_title": "🎰 WIN!",
        "win_msg": "Congratulations! You won {} gold!",
        "lose_title": "🎰 LOSE",
        "lose_msg": "Luck is not on your side. You lost {}.",
        "no_money": "You don't have enough money!",
        "min_bet": "Bet must be greater than zero!",

        "shop_title": "Merchant's Shop",
        "shop_ask": "What do you want to buy?",
        "already_have": "You already have a {}! Why do you need another one?",
        "buy_success": "Success! Bought {}. Your total damage: {}",
        "no_gold": "Not enough gold!",
        "no_item": "This item is not in stock.",
        "img_err": "Could not load image.",

        "slot_name": "Slot",
        "new_game": "🔄 New Game",

        "dead_warning_title": "Dead Man",
        "dead_hunt_msg": "The dead don't hunt! Restore your health first.",
        "defeat_title": "DEFEAT",
        "defeat_msg": "You died and lost half of your gold!",

        "enemy": "Enemy",
        "fight_or_run": "Enemy: {} (HP: {}, DMG: {})\nFight or Escape?",
        "run_success": "You escaped successfully!",
        "run_fail": "Escape failed! {} hit you!",
        "battle_title": "BATTLE",
        "battle_status": "Your HP: {} | Enemy HP: {}\nPress OK to attack!",
        "win_hunt": "{} defeated!\nReward: {} gold.",
        "defeat_hunt": "You died in battle with {}...",
        "monsters": {
         "Слизень": "Slime",
         "Волк": "Wolf",
         "Огр": "Ogre"
        },

        "save_title": "Save Game",
        "slot_ask": "Enter slot number (1, 2, 3):",
        "err_title": "Error",
        "err_number": "Please enter a number (slot ID)!",
        "save_slot_ok": "Game saved to slot #{}!",

        "health_title": "Health",
        "healed": "You used {}!",
        "info_title": "Info",
        "is_weapon_msg": "{} cannot be used, it's a weapon.",

        
        # Items & Inventory
        "health_title": "Health",
        "use_item_msg": "You used {}!",
        "info_title": "Info",
        "is_weapon_msg": "{} cannot be used, it's a weapon.",
        "items": {
            "Меч": "Sword",
            "Зелье": "Potion",
            "Лук": "Bow",
            "Нож": "Knife"
        }
    },
    "jp": {
        "app_title": "私のRPGゲーム",
        "new_game": "🔄 新規ゲーム",
        "shop": "🛒 店",
        "hunt": "⚔️ 狩り",
        "casino": "🎰 カジノ",
        "save_btn": "💾 進捗を保存",
        "hero_dead": "勇者 ❌ {} は倒れた",
        "status_bar": " 👤 {} | HP: ❤️ {} | 攻撃力: ⚔️ {} | 所持金: 💰 {}",
        "defeat_title": "敗北",
        "defeat_msg": "あなたは死亡し、所持金の半分を失った！",
        "save_title": "💾 保存",
        "save_file_ok": "キャラクターがファイルに保存されました！",
        "save_slot_ok": "スロット #{} に保存しました！",
        "slot_ask": "スロット番号を入力してください (1, 2, 3):",
        "load_title": "ロード",
        "load_ask": "どのスロットをロードしますか？ (1, 2, 3...):",
        "err_title": "エラー",
        "err_number": "数値を入力してください！",
        "dead_warning_title": "死者",
        "dead_hunt_msg": "死者は狩りができません！まずは回復してください。",
        "dead_casino_msg": "死者に金は必要ない！",
        "confirm_title": "確認",
        "confirm_reset": "本当に新しく始めますか？全ての進捗が失われます！",
        "new_hero_title": "新しい冒険",
        "new_hero_ask": "新しい勇者の名前を入力してください:",
        "reset_success": "世界がリセットされました。幸運を！",
        "info_title": "情報",
        "casino_welcome": "--- カジノ「ラッキースライム」 ---",
        "bet_ask": "いくら賭けますか？",
        "gold": "ゴールド",
        "win_title": "🎰 勝利！",
        "win_msg": "おめでとうございます！ {} ゴールド獲得しました！",
        "lose_title": "🎰 敗北",
        "lose_msg": "運が悪かったですね。 {} ゴールド失いました。",
        "no_money": "お金が足りません！",
        "min_bet": "賭け金は0より大きくしてください！",
        "shop_title": "商人の店",
        "shop_ask": "何を購入しますか？",
        "already_have": "すでに {} を持っています！",
        "buy_success": "成功！ {} を購入。現在の攻撃力: {}",
        "no_gold": "ゴールドが足りません！",
        "no_item": "その商品は在庫がありません。",
        "img_err": "画像を読み込めませんでした。",
        "slot_name": "スロット",
        "enemy": "敵",
        "fight_or_run": "敵: {} (HP: {}, 攻撃力: {})\n戦うか逃げるか？",
        "run_success": "無事に逃げ切った！",
        "run_fail": "逃げられなかった！ {} の攻撃！",
        "battle_title": "戦闘",
        "battle_status": "自HP: {} | 敵HP: {}\nOKを押して攻撃！",
        "win_hunt": "{} を倒した！\n報酬: {} ゴールド。",
        "defeat_hunt": "{} との戦いで死亡した...",
        "monsters": {
            "Слизень": "スライム",
            "Волк": "ウルフ",
            "Огр": "オーガ"
        },
        "health_title": "体力",
        "healed": "{} を使用した！",
        "is_weapon_msg": "{} は武器なので使用できません。",
        "items": {
            "Меч": "剣",
            "Зелье": "ポーション",
            "Лук": "弓",
            "Нож": "ナイフ"
        }
    }
}


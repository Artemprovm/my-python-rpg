# My Python RPG ⚔️

[Русский](#русский) | [English](#english) | [日本語](#日本語) | [简体中文](#简体中文)

---

## Русский

Серьезная RPG на Python, выросшая в модульную платформу с поддержкой дополнений и модификаций.

### 🎨 Основные механики:
* **Модульность:** Поддержка **DLC** (.py) и **Модов** (.json) без изменения основного кода.
* **Современный GUI:** Интерфейс на CustomTkinter.
* **Локализация:** Полная поддержка RU/EN/JP/ZH языков.
* **Сохранения:** SQLite3 с поддержкой нескольких слотов.
* **Активности:** Охота, Магазин и Казино.

### 📂 Архитектура проекта:
* `main.py` — Ядро игры и GUI.
* `shop.py`, `hunt.py`, `casino.py` — Игровые модули.
* `strings.py` — База локализации (500+ строк).
* `/dlc` — Папка для сюжетных дополнений.
* `/mods` — Папка для пользовательских предметов (JSON).

---

## English

A modular Python RPG platform featuring a custom expansion system and full localization.

### 🎨 Key Features:
* **Extensibility:** Support for **DLC** (.py) and **Mods** (.json).
* **Modern GUI:** Built with CustomTkinter.
* **Localization:** RU/EN/JP/ZH support with real-time switching.
* **Save System:** Multi-slot SQLite3 storage.
* **Activities:** Hunting, Shopping, and Casino.

### 📂 Project Structure:
* `main.py` — Core engine and GUI.
* `/dlc` — Folder for story expansions.
* `/mods` — Folder for custom item modifications.

---

## 日本語

拡張性とモジュール性を備えた、Python製の本格的なマルチランゲージRPGです。

### 🎨 主な機能:
* **拡張性:** **DLC** (.py) と **Mod** (.json) をサポート。
* **多言語対応:** ロシア語、英語、日本語、中国語をリアルタイム切り替え。
* **セーブシステム:** SQLite3によるマルチスロット保存。
* **コンテンツ:** 狩り、ショップ、カジノ。

### 📂 プロジェクト構造:
* `main.py` — メインエンジン。
* `/dlc` — 追加コンテンツ用フォルダ。
* `/mods` — カスタムMod用フォルダ。

---

## 简体中文

基于 Python 开发的模块化 RPG 游戏，支持插件扩展和多语言本地化。

### 🎨 核心机制：
* **扩展性：** 支持 **DLC** (.py) 和 **模组 (Mods)** (.json)。
* **本地化：** 完美支持 RU/EN/JP/ZH 语言实时切换。
* **存档系统：** 使用 SQLite3 进行多档位管理。
* **游戏内容：** 狩猎、商店和赌场。

### 📂 项目架构：
* `main.py` — 游戏核心与 GUI。
* `/dlc` — 附加内容文件夹。
* `/mods` — 自定义物品文件夹。

---

### 🛠 Стек / Tech Stack:
* **Python 3.14+**, **CustomTkinter**, **SQLite3**, **Pillow**.

### 📦 Запуск / How to Run:
```bash
git clone https://github.com
pip install customtkinter pillow
python main.py
```

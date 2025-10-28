# Telegram Echo-Bot (Проєкт №1)

## Опис

Цей проєкт — простий Telegram-бот, написаний на Python з використанням бібліотеки `python-telegram-bot`. Бот був створений як практичне завдання для демонстрації навичок роботи з API та асинхронним програмуванням.

Бот вміє:
* Вітатися з користувачем на команду `/start`.
* Повторювати (як "ехо") будь-яке текстове повідомлення, надіслане користувачем.

## Використані технології

* Python 3.12
* [python-telegram-bot](https://python-telegram-bot.org/) (для взаємодії з Telegram Bot API)
* [python-dotenv](https://pypi.org/project/python-dotenv/) (для безпечного керування токенами)

## Як запустити

1.  Клонуйте репозиторій на свій комп'ютер:
    ```bash
    git clone [https://github.com/madjoe2005/telegram-echo-bot.git](https://github.com/ТВІЙ_НІК/telegram-echo-bot.git)
    ```
2.  Перейдіть в папку з проєктом:
    ```bash
    cd telegram-echo-bot
    ```
3.  Створіть та активуйте віртуальне середовище:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Встановіть залежності:
    ```bash
    pip install -r requirements.txt
    ```
5.  Створіть файл `.env` в корені проєкту.
6.  Додайте в `.env` ваш токен, отриманий від @BotFather:
    ```
    TELEGRAM_TOKEN=1234567890:ABCDEFGHIJK...
    ```
7.  Запустіть скрипт:
    ```bash
    python main.py
    ```
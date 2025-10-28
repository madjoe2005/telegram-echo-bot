import logging
import os  # Потрібен для завантаження токена з .env

from dotenv import load_dotenv  # Імпортуємо функцію для завантаження .env
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Налаштовуємо логування, щоб бачити помилки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Завантажуємо змінні середовища з файлу .env
# Тепер Python "знає" про змінну TELEGRAM_TOKEN
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("Не знайдено TELEGRAM_TOKEN у .env файлі! Перевір крок 1.4.")


# Функція, яка буде викликатись на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Відправляє вітальне повідомлення у відповідь на команду /start."""
    user = update.effective_user
    # update.message.reply_html - відправляє повідомлення з підтримкою HTML
    await update.message.reply_html(
        f"Привіт, {user.mention_html()}! Я простий echo-бот. Напиши мені щось, і я повторю."
    )


# Функція, яка буде викликатись на будь-яке текстове повідомлення
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Повторює повідомлення користувача."""
    logger.info(f"Користувач {update.effective_user.name} написав: {update.message.text}")
    # update.message.reply_text - просто відправляє текст
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Основна функція запуску бота."""

    # 1. Створюємо "Application" і передаємо йому токен
    application = Application.builder().token(TOKEN).build()
    logger.info("Бот запускається...")

    # 2. Додаємо обробник для команди /start
    application.add_handler(CommandHandler("start", start))

    # 3. Додаємо обробник для всіх текстових повідомлень (не команд)
    # filters.TEXT & ~filters.COMMAND - означає "будь-який текст, який не є командою"
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 4. Запускаємо бота (в режимі polling - він сам опитує Telegram)
    # Це буде працювати, доки ти не зупиниш скрипт (Ctrl+C в терміналі)
    application.run_polling()
    logger.info("Бот зупинено.")


if __name__ == "__main__":
    main()
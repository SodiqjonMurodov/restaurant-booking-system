from telegram import Bot
from telegram.error import TelegramError
from core.settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN


async def send_to_telegram(message):
    bot = Bot(token=TELEGRAM_TOKEN)

    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except TelegramError as e:
        print(f"Telegram error: {e}")


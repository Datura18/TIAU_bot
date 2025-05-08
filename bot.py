from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import asyncio
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات دانشگاه هنر خوش اومدی!")

async def send_food_reminder(app):
    while True:
        now = datetime.datetime.now()
        if now.weekday() == 2 and now.hour == 9:
            for chat_id in app.chat_ids:
                await app.bot.send_message(chat_id=chat_id, text="یادت نره غذاتو رزرو کنی!")
            await asyncio.sleep(86400)
        await asyncio.sleep(3600)

async def save_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.application.chat_ids.add(update.message.chat_id)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.chat_ids = set()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("start", save_chat))

    asyncio.create_task(send_food_reminder(app))
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())

import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["TELEGRAM_CHANNEL_ID"])

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    try:
        await context.bot.forward_message(
            chat_id=CHANNEL_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id
        )
        await msg.reply_text("✅ پیام شما دریافت شد.")
    except Exception as e:
        print("خطا:", e)

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(~filters.COMMAND, forward_to_channel))

    # به مدت ۴ دقیقه منتظر پیام‌ها می‌مونه و بعد خودش رو می‌بنده
    await app.initialize()
    await app.updater.start_polling()
    import asyncio
    await asyncio.sleep(240)  # ۴ دقیقه
    await app.updater.stop()
    await app.shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

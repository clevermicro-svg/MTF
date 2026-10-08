import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["TELEGRAM_CHANNEL_ID"])

print("TOKEN:", "OK" if TOKEN else "EMPTY")
print("CHANNEL_ID:", CHANNEL_ID)

async def forward_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    print("پیام دریافت شد از:", msg.chat_id)
    try:
        await context.bot.forward_message(
            chat_id=CHANNEL_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id
        )
        await msg.reply_text("✅ پیام شما دریافت شد.")
        print("فوروارد موفق")
    except Exception as e:
        print("خطا در فوروارد:", e)

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(~filters.COMMAND, forward_to_channel))

    await app.initialize()
    print("ربات initialize شد")
    await app.updater.start_polling()
    print("ربات شروع به دریافت پیام کرد")
    await asyncio.sleep(240)
    await app.updater.stop()
    await app.shutdown()
    print("ربات خاموش شد")

if __name__ == "__main__":
    asyncio.run(main())

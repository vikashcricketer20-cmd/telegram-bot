from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "8634480341:AAEd71n4thTrpQZQF8mNQJ1SJjqxGHBtXBE"
ADMIN_ID = 8211049757

users = set()

async def start(update, context):
    users.add(update.message.chat_id)
    await update.message.reply_text("Welcome to Giveaway Arena Bot 🎁")

async def message(update, context):
    user_id = update.message.chat_id

    if user_id == ADMIN_ID:
        for u in users:
            await context.bot.send_message(chat_id=u, text=update.message.text)
    else:
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=user_id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

app.run_polling()

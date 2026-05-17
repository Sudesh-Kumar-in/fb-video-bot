import os
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8006684924:AAHcV_JXh6CIS7KdTtM0GYYEhpgvdlas2k8"


async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    if "facebook.com" not in url:
        await update.message.reply_text("Facebook video link bhejo.")
        return

    await update.message.reply_text("Downloading... ⏳")

    filename = "video.mp4"

    ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
        'noplaylist': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if os.path.exists(filename):
            await update.message.reply_video(video=open(filename, "rb"))
            os.remove(filename)
        else:
            await update.message.reply_text("Download hua nahi ❌")

    except Exception as e:
        await update.message.reply_text(str(e))


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, download_video))

print("BOT RUNNING ✅")

app.run_polling()

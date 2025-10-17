from telegram.ext import CommandHandler

def site(update, context):
    update.message.reply_text("📊 今日上传：41.3 GB  下载：3.7 GB")

site_handler = CommandHandler("site", site)

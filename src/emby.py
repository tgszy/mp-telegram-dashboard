from telegram.ext import CommandHandler

def refresh(update, context):
    update.message.reply_text("🔄 已通知 Emby 扫描媒体库")

refresh_handler = CommandHandler("refresh", refresh)

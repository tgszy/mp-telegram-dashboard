from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    update.message.reply_text("🔄 已通知 Emby 刷新媒体库")

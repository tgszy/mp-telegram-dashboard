from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    update.message.reply_text("💾 磁盘剩余：\n/volume1  2.3 TB\n/volume2  1.1 TB")

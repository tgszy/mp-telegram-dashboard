from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    # 简易列表
    update.message.reply_text("📥 当前下载任务：\n1. Spider-Man 71 %\n2. Batman  12 %")

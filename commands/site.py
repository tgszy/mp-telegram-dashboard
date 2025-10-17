from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    update.message.reply_text("📈 今日统计：\n上传 127 GB\n下载  3 GB\n魔力  4567")

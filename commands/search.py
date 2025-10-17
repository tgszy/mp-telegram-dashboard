from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("用法：/search 关键词")
        return
    keyword = " ".join(context.args)
    # 这里调用 MoviePilot 搜索 API，简化回显
    update.message.reply_text(f"🔍 搜索「{keyword}」的结果将在此展示")

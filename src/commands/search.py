from telegram.ext import CommandHandler
from app.utils.telegram import TelegramUtils

def search(update, context):
    if not context.args:
        update.message.reply_text("🔍 用法：/search 关键词")
        return
    key = " ".join(context.args)
    # 这里调用 MoviePilot 搜索 API，下面仅示例
    update.message.reply_text(f"搜索「{key}」结果模拟：\n✅ 4K Remux 71.3 GB")

search_handler = CommandHandler("search", search)

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler

def build_menu():
    """返回一个 CallbackQueryHandler，让 Bot 每条消息底部追加按钮"""
    keyboard = [
        [InlineKeyboardButton("🔍 搜索", callback_data="cmd_search"),
         InlineKeyboardButton("📥 下载", callback_data="cmd_down")],
        [InlineKeyboardButton("🔄 刷新库", callback_data="cmd_refresh"),
         InlineKeyboardButton("💾 磁盘", callback_data="cmd_disk")],
        [InlineKeyboardButton("📈 站点", callback_data="cmd_site"),
         InlineKeyboardButton("🧹 清理", callback_data="cmd_clean")],
        [InlineKeyboardButton("🔑 订阅", callback_data="cmd_sub"),
         InlineKeyboardButton("🦾 重启", callback_data="cmd_reboot")]
    ]
    return CallbackQueryHandler(keyboard_callback, pattern="^cmd_")

def keyboard_callback(update, context):
    query = update.callback_query
    cmd = query.data.replace("cmd_", "")
    # 把按钮点击转成对应 /命令
    context.bot.send_message(chat_id=query.message.chat_id,
                             text=f"/{cmd}")
    query.answer()          # 关闭转圈

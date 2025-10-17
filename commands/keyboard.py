from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler

def button_callback(update, context):
    query = update.callback_query
    query.answer()
    # 点按钮 = 发对应命令
    cmd = query.data          # 例如 /search
    context.bot.send_message(chat_id=query.message.chat_id, text=cmd)

def install(utils, cfg):
    if not cfg.get("enable_keyboard"):
        return
    kb = [
        [InlineKeyboardButton("🔍 搜索", callback_data="/search"),
         InlineKeyboardButton("📥 下载", callback_data="/down")],
        [InlineKeyboardButton("🔄 刷新", callback_data="/refresh"),
         InlineKeyboardButton("💾 磁盘", callback_data="/disk")],
        [InlineKeyboardButton("📈 站点", callback_data="/site"),
         InlineKeyboardButton("🧹 清理", callback_data="/clean_tv 90")],
        [InlineKeyboardButton("🦾 重启", callback_data="/reboot"),
         InlineKeyboardButton("⬆️ 更新", callback_data="/update")]
    ]
    utils.add_handler(CallbackQueryHandler(button_callback))
    # 把 kb 注入到 MP 的 telegram_utils 全局变量，dashboard 会在发消息时自动 append
    utils.global_keyboard = InlineKeyboard

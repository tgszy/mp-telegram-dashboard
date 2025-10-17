from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def append_keyboard():
    """
    返回 InlineKeyboardMarkup 实例，供 dashboard.py 每条消息追加
    点按钮 = 直接发送 /命令 文字，无需回调
    """
    keyboard = [
        [InlineKeyboardButton("🔍 搜索", callback_data="noop"),
         InlineKeyboardButton("📥 下载", callback_data="noop")],
        [InlineKeyboardButton("🔄 刷新库", callback_data="noop"),
         InlineKeyboardButton("💾 磁盘", callback_data="noop")],
        [InlineKeyboardButton("📈 站点", callback_data="noop"),
         InlineKeyboardButton("🧹 清理", callback_data="noop")],
        [InlineKeyboardButton("🔑 订阅", callback_data="noop"),
         InlineKeyboardButton("🦾 重启", callback_data="noop")]
    ]
    return InlineKeyboardMarkup(keyboard)

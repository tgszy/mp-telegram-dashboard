from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler

def build_menu():
    btn = [
        [InlineKeyboardButton("🔍 搜索", callback_data="cmd_search"),
         InlineKeyboardButton("📥 下载", callback_data="cmd_down")],
        [InlineKeyboardButton("🔄 刷新库", callback_data="cmd_refresh"),
         InlineKeyboardButton("💾 磁盘", callback_data="cmd_disk")],
        [InlineKeyboardButton("📈 站点", callback_data="cmd_site"),
         InlineKeyboardButton("🧹 清理", callback_data="cmd_clean")],
        [InlineKeyboardButton("🔑 订阅", callback_data="cmd_sub"),
         InlineKeyboardButton("🦾 重启", callback_data="cmd

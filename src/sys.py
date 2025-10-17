
from telegram.ext import CommandHandler

def reboot(update, context):
    update.message.reply_text("🦾 系统重启指令已发送")

def update(update, context):
    update.message.reply_text("⬆️ 正在拉取最新镜像并重启")

reboot_handler = CommandHandler("reboot", reboot)
update_handler = CommandHandler("update", update)

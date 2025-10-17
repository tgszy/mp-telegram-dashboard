from telegram import Update
from telegram.ext import CallbackContext
import os

def reboot(update: Update, context: CallbackContext):
    update.message.reply_text("🔄 正在重启 MoviePilot ...")
    os.system("systemctl restart moviepilot")

def update(update: Update, context: CallbackContext):
    update.message.reply_text("⬆️ 正在拉取最新镜像并重启 ...")
    os.system("docker pull your-mp-image && docker restart moviepilottest")

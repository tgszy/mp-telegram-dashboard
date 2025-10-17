from telegram.ext import CommandHandler

def down(update, context):
    update.message.reply_text("📥 当前下载任务模拟：\n1. 蜘蛛侠 23.4 %\n2. 繁花 100 %")

down_handler = CommandHandler("down", down)

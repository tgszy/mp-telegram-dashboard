from telegram.ext import CommandHandler

def sub(add, update, context):
    update.message.reply_text("📺 订阅列表模拟：繁花、 westworld")

sub_handler = CommandHandler("sub", sub)

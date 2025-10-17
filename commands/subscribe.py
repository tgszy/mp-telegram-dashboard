from telegram import Update
from telegram.ext import CallbackContext

def handle(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("用法：/sub add 名称  或  /sub list")
        return
    cmd = context.args[0]
    if cmd == "list":
        update.message.reply_text("📜 当前订阅：\n- 繁花\n- 庆余年2")
    else:
        update.message.reply_text("✅ 订阅已添加")

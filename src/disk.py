from telegram.ext import CommandHandler

def disk(update, context):
    update.message.reply_text("💾 磁盘剩余：/media 832 GB / 1.2 TB")

disk_handler = CommandHandler("disk", disk)

from app.plugins import _PluginBase
from app.utils.telegram import TelegramUtils
from telegram.ext import CommandHandler
from .commands import (
    search, download, subscribe, emby, disk, site, sys, keyboard
)

class DashboardPlugin(_PluginBase):
    plugin_name = "Telegram 仪表盘 (多群版)"
    plugin_desc = "支持多人/多群/多频道、白名单、快捷按钮的 TG 控制台"
    plugin_version = "2.0"
    plugin_author = "you"

    # 权限级别 1=所有人 2=白名单 3=管理员
    auth_level = 2

    def init_command(self) -> TelegramUtils:
        utils = TelegramUtils()
        cfg = self.get_config()
        if not cfg:
            return utils

        # 根据开关注册命令
        if cfg.get("enable_search"):
            utils.add_handler(CommandHandler("search", search.handle))
        if cfg.get("enable_download"):
            utils.add_handler(CommandHandler("down", download.handle))
        if cfg.get("enable_sub"):
            utils.add_handler(CommandHandler("sub", subscribe.handle))
        if cfg.get("enable_refresh"):
            utils.add_handler(CommandHandler("refresh", emby.handle))
        if cfg.get("enable_disk"):
            utils.add_handler(CommandHandler("disk", disk.handle))
        if cfg.get("enable_site"):
            utils.add_handler(CommandHandler("site", site.handle))
        if cfg.get("enable_sys"):
            utils.add_handler(CommandHandler("reboot", sys.reboot))
            utils.add_handler(CommandHandler("update", sys.update))

        # 快捷按钮回调
        if cfg.get("enable_keyboard"):
            keyboard.install(utils, cfg)
        return utils

    def get_config_vars(self):
        return {
            "bot_token": {
                "title": "Bot Token（留空用全局）",
                "type": "password",
                "placeholder": "123456:ABC..."
            },
            "token_help": {
                "title": "如何查询 Token",
                "type": "static",
                "value": "1. 在 Telegram 搜 @BotFather\n2. 发送 /mybots → 选 Bot → 复制 Token"
            },
            "admin_ids": {
                "title": "管理员白名单（一行一个）",
                "type": "textarea",
                "placeholder": "123456789\n987654321"
            },
            "user_ids": {
                "title": "用户白名单（留空=不限）",
                "type": "textarea",
                "placeholder": "111222333"
            },
            "id_help": {
                "title": "如何查自己 ID",
                "type": "static",
                "value": "搜 @userinfobot → Start → 复制数字"
            },
            "group_ids": {
                "title": "允许群组 ID（-100xxx）",
                "type": "textarea",
                "placeholder": "-1001862438527"
            },
            "channel_ids": {
                "title": "允许频道 ID（-100xxx）",
                "type": "textarea",
                "placeholder": "-1001777888999"
            },
            "enable_search":  {"title": "搜索命令", "type": "toggle", "default": True},
            "enable_download": {"title": "下载管理", "type": "toggle", "default": True},
            "enable_sub": {"title": "订阅管理", "type": "toggle", "default": True},
            "enable_refresh": {"title": "刷新媒体库", "type": "toggle", "default": True},
            "enable_disk": {"title": "磁盘空间", "type": "toggle", "default": True},
            "enable_site": {"title": "站点数据", "type": "toggle", "default": True},
            "enable_sys": {"title": "系统控制", "type": "toggle", "default": False},
            "enable_keyboard": {"title": "快捷按钮", "type": "toggle", "default": True}
        }

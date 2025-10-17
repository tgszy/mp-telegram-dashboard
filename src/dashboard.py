from app.plugins import _PluginBase
from app.utils.telegram import TelegramUtils
from .commands import ALL_HANDLERS, build_menu
from telegram.ext import CommandHandler

class TelegramDashboard(_PluginBase):
    plugin_name = "Telegram 仪表盘"
    plugin_desc = "多群/多频道控制 & 快捷按钮"
    plugin_version = "2.0"
    plugin_author = "you"
    plugin_config_prefix = "tgdb_"
    plugin_auth_level = 2          # 管理员可用

    def init_plugin(self, config=None):
        if not self.get_state():
            return
        utils = TelegramUtils()
        # 注册命令
        for h in ALL_HANDLERS:
            utils.add_handler(h)
        # 注入按钮
        utils.add_handler(build_menu())
        return utils

    def get_fields(self):
        return [
            {
                "title": "基础",
                "type": "row",
                "content": [
                    {"title": "Bot Token", "name": "bot_token", "type": "password", "placeholder": "留空用全局"},
                    {"title": "🔍 查 Token 方法", "name": "token_help", "type": "static",
                     "content": "1. 在 Telegram 搜 @BotFather → /mybots → 复制 API Token"}
                ]
            },
            {
                "title": "身份白名单",
                "type": "row",
                "content": [
                    {"title": "管理员 ID（一行一个）", "name": "admin_ids", "type": "textarea", "placeholder": "987654321"},
                    {"title": "用户 ID（留空=不限）", "name": "user_ids", "type": "textarea", "placeholder": "123456789"},
                    {"title": "👤 查自己 ID", "name": "id_help", "type": "static",
                     "content": "搜 @userinfobot → Start → 复制数字"}
                ]
            },
            {
                "title": "群/频道 ID",
                "type": "row",
                "content": [
                    {"title": "允许群组 ID", "name": "group_ids", "type": "textarea", "placeholder": "-1001862438527"},
                    {"title": "允许频道 ID", "name": "channel_ids", "type": "textarea", "placeholder": "-1001666888999"}
                ]
            },
            {
                "title": "功能开关",
                "type": "row",
                "content": [
                    {"title": "搜索", "name": "enable_search", "type": "switch", "default": True},
                    {"title": "下载", "name": "enable_down", "type": "switch", "default": True},
                    {"title": "订阅", "name": "enable_sub", "type": "switch", "default": True},
                    {"title": "刷新库", "name": "enable_refresh", "type": "switch", "default": True},
                    {"title": "磁盘", "name": "enable_disk", "type": "switch", "default": True},
                    {"title": "站点", "name": "enable_site", "type": "switch", "default": True},
                    {"title": "系统", "name": "enable_sys", "type": "switch", "default": True},
                    {"title": "快捷按钮", "name": "show_keyboard", "type": "switch", "default": True}
                ]
            }
        ]

from .search import search_handler
from .download import down_handler
from .subscribe import sub_handler
from .emby import refresh_handler
from .disk import disk_handler
from .site import site_handler
from .sys import reboot_handler, update_handler
from .keyboard import build_menu

ALL_HANDLERS = [
    search_handler, down_handler, sub_handler,
    refresh_handler, disk_handler, site_handler,
    reboot_handler, update_handler
]

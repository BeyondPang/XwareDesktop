# -*- coding: utf-8 -*-

LOGIN_PAGE = "http://yuancheng.xunlei.com/login.html"

XWARED_LOCK = "/tmp/xware_xwared.lock"
XWARED_SOCKET = "/tmp/xware_xwared.socket"

ETM_LOCK = "/tmp/xware_ETM.lock"

FRONTEND_LOCK = "/tmp/xware_frontend.lock"
FRONTEND_SOCKET = ("/tmp/xware_frontend.socket", "AF_UNIX")

CONFIG_FILE = "/opt/xware_desktop/settings.ini"

MOUNTS_FILE = "/opt/xware_desktop/mounts"
MOUNTS_FILE_HEADER = "# This file is automatically generated by Xware Desktop. Manually modifying this file via a text editor is not advised."
MOUNTS_DIR = "/opt/xware_desktop/mount_points/"

ETM_MOUNTS_DIR = "/tmp/thunder/volumes/" # the last slash is needed
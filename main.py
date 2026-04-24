"""
School Management System — Entry Point.

Launches the login/splash window which, on successful authentication,
opens the main application window.
"""

import sys
import os

# Fix for Qt plugin/platform errors
try:
    import PySide6
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, "plugins")
    os.environ["QT_PLUGIN_PATH"] = plugin_path
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(plugin_path, "platforms")
except Exception:
    pass

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from app.views.login_window import LoginWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    sys.exit(app.exec())
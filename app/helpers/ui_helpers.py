"""
UI Helper Functions.

Manages frameless-window behaviour: drag, maximize/restore,
custom resize grips, and title-bar button wiring.
"""

from PySide6.QtCore import Qt, QEvent, QPoint
from PySide6.QtGui import QColor, QCursor
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from app.core import Settings
from app.widgets import CustomGrip


# Global maximised state tracker
_is_maximized = False


class UiHelpers:
    """Static helpers for frameless window management.

    All methods receive the *window* (MainWindow instance) as the
    first argument — they are called as ``UiHelpers.method(self)``.
    """

    # ------------------------------------------------------------------
    # Maximize / Restore toggle
    # ------------------------------------------------------------------

    @staticmethod
    def maximize_restore(window):
        global _is_maximized

        def _apply_ui():
            if not _is_maximized:
                window.resize(window.width() + 1, window.height() + 1)
                window.ui.margins_app.setContentsMargins(10, 10, 10, 10)
                window.ui.maximize_restore_app_btn.setToolTip("Restore")
                window.ui.maximize_restore_app_btn.setStyleSheet(
                    "background-image: url(:/icons_svg/images/icons_svg/icon_maximize.svg);"
                )
                window.ui.bg_app.setStyleSheet(
                    "#bg_app { border-radius: 10px; border: 2px solid rgb(30, 32, 33); }"
                )
                window.left_grip.show()
                window.right_grip.show()
                window.top_grip.show()
                window.bottom_grip.show()
            else:
                window.ui.margins_app.setContentsMargins(0, 0, 0, 0)
                window.ui.maximize_restore_app_btn.setToolTip("Restore")
                window.ui.maximize_restore_app_btn.setStyleSheet(
                    "background-image: url(:/icons_svg/images/icons_svg/icon_restore.svg);"
                )
                window.ui.bg_app.setStyleSheet(
                    "#bg_app { border-radius: 0px; border: none; }"
                )
                window.left_grip.hide()
                window.right_grip.hide()
                window.top_grip.hide()
                window.bottom_grip.hide()

        if window.isMaximized():
            _is_maximized = False
            window.showNormal()
            _apply_ui()
        else:
            _is_maximized = True
            window.showMaximized()
            _apply_ui()

    # ------------------------------------------------------------------
    # Initial UI definitions (called once during MainWindow.__init__)
    # ------------------------------------------------------------------

    @staticmethod
    def set_ui_definitions(window):
        settings = Settings()

        # Frameless + transparent
        window.setWindowFlag(Qt.FramelessWindowHint)
        window.setAttribute(Qt.WA_TranslucentBackground)

        # --- Drag / Move ---
        def move_window(event):
            if window.isMaximized():
                UiHelpers.maximize_restore(window)
                cx = window.pos().x()
                cy = event.globalPos().y() - QCursor.pos().y()
                window.move(cx, cy)
            if event.buttons() == Qt.LeftButton:
                window.move(window.pos() + event.globalPos() - window.dragPos)
                window.dragPos = event.globalPos()
                event.accept()

        window.ui.logo_top.mouseMoveEvent = move_window
        window.ui.logo.mouseMoveEvent = move_window
        window.ui.title_bar.mouseMoveEvent = move_window

        # --- Double-click maximize ---
        def dbl_maximize(event):
            if event.type() == QEvent.MouseButtonDblClick:
                UiHelpers.maximize_restore(window)

        window.ui.title_bar.mouseDoubleClickEvent = dbl_maximize

        # --- Window buttons ---
        window.ui.minimize_app_btn.clicked.connect(window.showMinimized)
        window.ui.maximize_restore_app_btn.clicked.connect(
            lambda: UiHelpers.maximize_restore(window)
        )
        window.ui.close_app_btn.clicked.connect(window.close)

        # --- Size defaults ---
        window.setWindowTitle(settings["app_name"])
        window.resize(settings["startup_size"][0], settings["startup_size"][1])
        window.setMinimumSize(settings["minimum_size"][0], settings["minimum_size"][1])

        # --- Drop shadow ---
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 80))
        window.ui.stylesheet.setGraphicsEffect(shadow)

        # --- Custom resize grips ---
        window.left_grip = CustomGrip(window, Qt.LeftEdge, True)
        window.right_grip = CustomGrip(window, Qt.RightEdge, True)
        window.top_grip = CustomGrip(window, Qt.TopEdge, True)
        window.bottom_grip = CustomGrip(window, Qt.BottomEdge, True)

    # ------------------------------------------------------------------
    # Resize grips (called from MainWindow.resizeEvent)
    # ------------------------------------------------------------------

    @staticmethod
    def resize_grips(window):
        window.left_grip.setGeometry(0, 10, 10, window.height())
        window.right_grip.setGeometry(window.width() - 10, 10, 10, window.height())
        window.top_grip.setGeometry(0, 0, window.width(), 10)
        window.bottom_grip.setGeometry(0, window.height() - 10, window.width(), 10)

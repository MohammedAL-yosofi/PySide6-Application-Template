"""
Main Window UI definition.

Layout:  left-menu (50px)  |  sidebar (240 px)  |  right-content (title bar + stacked pages).
Navigation buttons and pages are added dynamically in main_window.py.
"""

from PySide6.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PySide6.QtGui import QFont, QPixmap, QCursor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QPushButton, QStackedWidget, QScrollArea, QSpacerItem, QSizePolicy,
)

from app.ui import resources_rc  # noqa: F401  — registers Qt resources


class Ui_MainWindow:
    """Defines the structural layout for the main application window."""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 720)

        # === Central widget with global stylesheet ===
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName("stylesheet")
        self.stylesheet.setStyleSheet(_MAIN_STYLE)

        self.margins_app = QVBoxLayout(self.stylesheet)
        self.margins_app.setSpacing(0)
        self.margins_app.setObjectName("margins_app")
        self.margins_app.setContentsMargins(10, 10, 10, 10)

        # --- Background frame ---
        self.bg_app = QFrame(self.stylesheet)
        self.bg_app.setObjectName("bg_app")
        self.bg_app.setStyleSheet("#bg_app { border-radius: 10px; }")
        self.bg_app.setFrameShape(QFrame.NoFrame)
        self.bg_app.setLineWidth(0)

        self.base_layout = QVBoxLayout(self.bg_app)
        self.base_layout.setSpacing(0)
        self.base_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(0)

        # ============================================================
        #  LEFT ICON MENU  (50 px)
        # ============================================================
        self.left_menu = QFrame(self.bg_app)
        self.left_menu.setObjectName("left_menu")
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setLineWidth(0)

        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setSpacing(0)
        self.left_menu_layout.setContentsMargins(0, 5, 0, 0)

        # Logo
        self.logo_top = QLabel(self.left_menu)
        self.logo_top.setObjectName("logo_top")
        self.logo_top.setMinimumSize(QSize(40, 40))
        self.logo_top.setMaximumSize(QSize(40, 40))
        pixmap_logo = QPixmap(":/images_svg/images/images_svg/logo_home.png")
        if not pixmap_logo.isNull():
            scaled_logo = pixmap_logo.scaled(
                self.logo_top.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.logo_top.setPixmap(scaled_logo)
        self.logo_top.setAlignment(Qt.AlignCenter)
        self.logo_top.setScaledContents(False)
        self.left_menu_layout.addWidget(self.logo_top, 0, Qt.AlignCenter)

        # Top menus (buttons added dynamically)
        self.top_menus = QFrame(self.left_menu)
        self.top_menus.setObjectName("top_menus")
        self.top_menus.setMinimumSize(QSize(0, 50))
        self.top_menus.setFrameShape(QFrame.NoFrame)
        self.top_menus_layout = QVBoxLayout(self.top_menus)
        self.top_menus_layout.setSpacing(5)
        self.top_menus_layout.setContentsMargins(5, 5, 5, 5)
        self.left_menu_layout.addWidget(self.top_menus)

        # Spacer
        self.left_menu_layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Bottom menus (buttons added dynamically)
        self.bottom_menus = QFrame(self.left_menu)
        self.bottom_menus.setObjectName("bottom_menus")
        self.bottom_menus.setMinimumSize(QSize(0, 50))
        self.bottom_menus.setFrameShape(QFrame.NoFrame)
        self.bottom_menus_layout = QVBoxLayout(self.bottom_menus)
        self.bottom_menus_layout.setSpacing(5)
        self.bottom_menus_layout.setContentsMargins(5, 5, 5, 5)
        self.left_menu_layout.addWidget(self.bottom_menus)

        self.main_layout.addWidget(self.left_menu)

        # ============================================================
        #  SIDEBAR  (240 px)
        # ============================================================
        self.sidebar = QFrame(self.bg_app)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setMinimumSize(QSize(240, 0))
        self.sidebar.setMaximumSize(QSize(240, 16777215))
        self.sidebar.setFrameShape(QFrame.NoFrame)

        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setSpacing(0)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)

        # -- Sidebar header (logo + title) --
        self.sidebar_header = QFrame(self.sidebar)
        self.sidebar_header.setObjectName("sidebar_header")
        self.sidebar_header.setMinimumSize(QSize(0, 60))
        self.sidebar_header.setMaximumSize(QSize(16777215, 60))
        self.sidebar_header.setFrameShape(QFrame.NoFrame)

        self.header_layout = QHBoxLayout(self.sidebar_header)
        self.header_layout.setContentsMargins(5, 5, 5, 5)
        self.header_layout.setSpacing(10)

        self.logo = QLabel(self.sidebar_header)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(35, 35))
        self.logo.setMaximumSize(QSize(35, 35))
        pixmap = QPixmap(":/images_svg/images/images_svg/logo_home.png")
        if not pixmap.isNull():
            scaled = pixmap.scaled(
                self.logo.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.logo.setPixmap(scaled)
        self.logo.setAlignment(Qt.AlignCenter)

        self.header_layout.addWidget(self.logo)

        self.app_title = QLabel(self.sidebar_header)
        self.app_title.setObjectName("app_title")
        self.header_layout.addWidget(self.app_title)

        self.sidebar_layout.addWidget(self.sidebar_header)

        # -- Navigation section label --
        self.nav_section_label = QLabel(self.sidebar)
        self.nav_section_label.setObjectName("nav_section_label")
        self.nav_section_label.setStyleSheet(
            "padding: 12px 15px 6px 15px; color: #4a5568; "
            'font: 700 8pt "Segoe UI"; letter-spacing: 1px;'
        )
        self.sidebar_layout.addWidget(self.nav_section_label)

        # -- Navigation scroll area --
        self.nav_scroll = QScrollArea(self.sidebar)
        self.nav_scroll.setObjectName("nav_scroll")
        self.nav_scroll.setFrameShape(QFrame.NoFrame)
        self.nav_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nav_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nav_scroll.setWidgetResizable(True)

        self.nav_container = QWidget()
        self.nav_container.setObjectName("nav_container")

        self.nav_wrapper_layout = QVBoxLayout(self.nav_container)
        self.nav_wrapper_layout.setContentsMargins(10, 2, 10, 10)
        self.nav_wrapper_layout.setSpacing(0)

        # Nav buttons frame — buttons are added dynamically here
        self.nav_frame = QFrame(self.nav_container)
        self.nav_frame.setObjectName("nav_frame")
        self.nav_frame.setFrameShape(QFrame.NoFrame)

        self.nav_layout = QVBoxLayout(self.nav_frame)
        self.nav_layout.setContentsMargins(0, 0, 0, 0)
        self.nav_layout.setSpacing(4)

        self.nav_wrapper_layout.addWidget(self.nav_frame, 0, Qt.AlignTop)

        self.nav_scroll.setWidget(self.nav_container)
        self.sidebar_layout.addWidget(self.nav_scroll)

        # -- Sidebar footer --
        self.sidebar_footer = QFrame(self.sidebar)
        self.sidebar_footer.setObjectName("sidebar_footer")
        self.sidebar_footer.setMinimumSize(QSize(0, 45))
        self.sidebar_footer.setMaximumSize(QSize(16777215, 45))
        self.sidebar_footer.setFrameShape(QFrame.NoFrame)

        self.footer_layout = QVBoxLayout(self.sidebar_footer)
        self.footer_layout.setContentsMargins(15, 5, 15, 10)

        self.footer_label = QLabel(self.sidebar_footer)
        self.footer_label.setObjectName("footer_label")
        self.footer_layout.addWidget(self.footer_label)

        self.sidebar_layout.addWidget(self.sidebar_footer)

        self.main_layout.addWidget(self.sidebar)

        # ============================================================
        #  RIGHT CONTENT
        # ============================================================
        self.right_content = QFrame(self.bg_app)
        self.right_content.setObjectName("right_content")
        _font = QFont()
        _font.setFamily("Segoe UI")
        _font.setPointSize(9)
        self.right_content.setFont(_font)
        self.right_content.setFrameShape(QFrame.NoFrame)
        self.right_content.setLineWidth(0)

        self.right_layout = QVBoxLayout(self.right_content)
        self.right_layout.setSpacing(0)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        # -- Top bar (title + window buttons) --
        self.top_bar = QFrame(self.right_content)
        self.top_bar.setObjectName("top_bar")
        self.top_bar.setMinimumSize(QSize(0, 45))
        self.top_bar.setMaximumSize(QSize(16777215, 45))
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setLineWidth(0)

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setSpacing(0)
        self.top_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Title bar label (draggable area)
        self.title_bar = QLabel(self.top_bar)
        self.title_bar.setObjectName("title_bar")
        self.title_bar.setLineWidth(0)
        self.top_bar_layout.addWidget(self.title_bar)

        # Window control buttons
        self.top_btns = QFrame(self.top_bar)
        self.top_btns.setObjectName("top_btns")
        self.top_btns.setMaximumSize(QSize(100, 16777215))
        self.top_btns.setFrameShape(QFrame.NoFrame)
        self.top_btns.setLineWidth(0)

        self.top_btn_layout = QHBoxLayout(self.top_btns)
        self.top_btn_layout.setSpacing(4)
        self.top_btn_layout.setContentsMargins(0, 0, 0, 0)

        # Minimize
        self.minimize_app_btn = QPushButton(self.top_btns)
        self.minimize_app_btn.setObjectName("minimize_app_btn")
        self.minimize_app_btn.setMinimumSize(QSize(28, 28))
        self.minimize_app_btn.setMaximumSize(QSize(28, 28))
        self.minimize_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_app_btn.setStyleSheet(
            "background-image: url(:/icons_svg/images/icons_svg/icon_minimize.svg);"
        )
        self.minimize_app_btn.setIconSize(QSize(20, 20))
        self.top_btn_layout.addWidget(self.minimize_app_btn)

        # Maximize / Restore
        self.maximize_restore_app_btn = QPushButton(self.top_btns)
        self.maximize_restore_app_btn.setObjectName("maximize_restore_app_btn")
        self.maximize_restore_app_btn.setMinimumSize(QSize(28, 28))
        self.maximize_restore_app_btn.setMaximumSize(QSize(28, 28))
        self.maximize_restore_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_restore_app_btn.setStyleSheet(
            "background-image: url(:/icons_svg/images/icons_svg/icon_maximize.svg);"
        )
        self.maximize_restore_app_btn.setIconSize(QSize(20, 20))
        self.top_btn_layout.addWidget(self.maximize_restore_app_btn)

        # Close
        self.close_app_btn = QPushButton(self.top_btns)
        self.close_app_btn.setObjectName("close_app_btn")
        self.close_app_btn.setMinimumSize(QSize(28, 28))
        self.close_app_btn.setMaximumSize(QSize(28, 28))
        self.close_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_app_btn.setStyleSheet(
            "background-image: url(:/icons_svg/images/icons_svg/icon_close.svg);"
        )
        self.close_app_btn.setIconSize(QSize(20, 20))
        self.top_btn_layout.addWidget(self.close_app_btn)

        self.top_btn_layout.addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.top_bar_layout.addWidget(self.top_btns)
        self.right_layout.addWidget(self.top_bar)

        # -- Content area (stacked pages) --
        self.content = QFrame(self.right_content)
        self.content.setObjectName("content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setLineWidth(0)

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setObjectName("content_layout")

        self.app_pages = QStackedWidget(self.content)
        self.app_pages.setObjectName("app_pages")
        self.app_pages.setStyleSheet("background-color: transparent;")
        # Pages are added dynamically in main_window.py

        self.content_layout.addWidget(self.app_pages)
        self.right_layout.addWidget(self.content)

        self.main_layout.addWidget(self.right_content)

        # ============================================================
        #  FINALISE
        # ============================================================
        self.base_layout.addLayout(self.main_layout)
        self.margins_app.addWidget(self.bg_app)
        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)
        self.app_pages.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    # ----------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.app_title.setText(
            QCoreApplication.translate("MainWindow", "School MS", None)
        )
        self.nav_section_label.setText(
            QCoreApplication.translate("MainWindow", "NAVIGATION", None)
        )
        self.footer_label.setText(
            QCoreApplication.translate("MainWindow", "v1.0.0", None)
        )
        self.title_bar.setText("")
        self.minimize_app_btn.setToolTip(
            QCoreApplication.translate("MainWindow", "Minimize", None)
        )
        self.minimize_app_btn.setText("")
        self.maximize_restore_app_btn.setToolTip(
            QCoreApplication.translate("MainWindow", "Maximize", None)
        )
        self.maximize_restore_app_btn.setText("")
        self.close_app_btn.setToolTip(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        self.close_app_btn.setText("")


# =====================================================================
#  STYLESHEET LOADER
# =====================================================================

import os as _os

# Directory containing the component CSS files
_STYLES_DIR = _os.path.join(_os.path.dirname(__file__), "styles")

# CSS files loaded in order (later files can override earlier ones)
_CSS_FILES = [
    "global.css",
    "left_menu.css",
    "sidebar.css",
    "right_content.css",
    "scrollbars.css",
]


def _load_main_style() -> str:
    """Read and concatenate all component CSS files into one stylesheet."""
    parts: list[str] = []
    for name in _CSS_FILES:
        path = _os.path.join(_STYLES_DIR, name)
        with open(path, "r", encoding="utf-8") as f:
            parts.append(f.read())
    return "\n".join(parts)


_MAIN_STYLE = _load_main_style()


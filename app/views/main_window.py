"""
Main Application Window.

Sets up the sidebar navigation, content pages, and window controls.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QButtonGroup

from app.core import IconManager, Settings
from app.ui.ui_main import Ui_MainWindow
from app.widgets import NavButton
from app.views.pages import DashboardPage, HomePage, AboutPage, SettingsPage
from app.helpers.ui_helpers import UiHelpers


# Navigation items:  (FontAwesome icon name, label text)
_NAV_ITEMS = [
    ("fa5s.tachometer-alt", "Dashboard"),
    ("fa5s.home", "Home"),
    ("fa5s.info-circle", "About"),
    ("fa5s.cog", "Settings"),
]


class MainWindow(QMainWindow):
    """Primary application window with sidebar navigation."""

    def __init__(self):
        super().__init__()

        # UI setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Core services
        self.settings = Settings()
        self.icons = IconManager()

        # Build navigation and pages
        self._setup_navigation()
        self._setup_pages()

        # Window management (frameless, grips, drag, buttons)
        UiHelpers.set_ui_definitions(self)

        # Default page
        self._navigate_to(0)

    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------

    def _setup_navigation(self):
        """Create sidebar nav buttons with mutual-exclusion via QButtonGroup."""
        self.nav_buttons: list[NavButton] = []
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        for idx, (icon_name, label) in enumerate(_NAV_ITEMS):
            icon = self.icons.get_icon(icon_name, color="#8b98a5")
            btn = NavButton(icon, label)
            btn.clicked.connect(lambda _checked, i=idx: self._navigate_to(i))
            self.button_group.addButton(btn, idx)
            self.ui.nav_layout.addWidget(btn)
            self.nav_buttons.append(btn)

    def _setup_pages(self):
        """Add content pages to the stacked widget."""
        self.pages = [
            DashboardPage(),
            HomePage(),
            AboutPage(),
            SettingsPage(),
        ]
        for page in self.pages:
            self.ui.app_pages.addWidget(page)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def _navigate_to(self, index: int):
        """Switch the visible page and highlight the active nav button."""
        self.ui.app_pages.setCurrentIndex(index)
        self.nav_buttons[index].setChecked(True)

    # ------------------------------------------------------------------
    # Window events
    # ------------------------------------------------------------------

    def resizeEvent(self, event):
        UiHelpers.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

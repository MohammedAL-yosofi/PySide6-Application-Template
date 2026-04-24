"""
Navigation Sidebar Button Widget.

A styled QPushButton with icon + text for sidebar navigation.
Supports active/hover/pressed states via Qt stylesheets.
"""

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QPushButton


# Stylesheet for NavButton states
_NAV_BUTTON_STYLE = """
NavButton {
    background-color: transparent;
    border: none;
    border-radius: 8px;
    color: #8b98a5;
    font: 500 10pt "Segoe UI";
    text-align: left;
    padding: 0 15px;
}
NavButton:hover {
    background-color: #1a2942;
    color: #e2e8f0;
}
NavButton:checked {
    background-color: rgba(44, 123, 229, 0.15);
    color: #ffffff;
    border-left: 3px solid #2c7be5;
    padding-left: 12px;
}
NavButton:pressed {
    background-color: rgba(44, 123, 229, 0.25);
}
"""


class NavButton(QPushButton):
    """
    Sidebar navigation button with icon and text label.

    Use setCheckable(True) + QButtonGroup for mutual exclusion.
    The :checked pseudo-state highlights the active page.
    """

    def __init__(self, icon: QIcon, text: str, parent=None):
        super().__init__(parent)
        self.setText(f"  {text}")
        if icon:
            self.setIcon(icon)
            self.setIconSize(QSize(18, 18))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setCheckable(True)
        self.setFixedHeight(45)
        self.setStyleSheet(_NAV_BUTTON_STYLE)

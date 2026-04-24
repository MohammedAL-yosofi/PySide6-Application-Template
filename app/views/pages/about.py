"""About page — placeholder."""

import qtawesome as qta
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class AboutPage(QWidget):
    """About content page."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("about_page")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)

        icon_label = QLabel()
        icon_label.setPixmap(
            qta.icon("fa5s.info-circle", color="#2c7be5").pixmap(64, 64)
        )
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("padding: 0;")

        title = QLabel("About")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font: 700 24pt "Segoe UI"; color: #e2e8f0; padding: 0;')

        subtitle = QLabel("Application information will appear here.")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet('font: 10pt "Segoe UI"; color: #4a5568; padding: 0;')

        layout.addWidget(icon_label)
        layout.addWidget(title)
        layout.addWidget(subtitle)

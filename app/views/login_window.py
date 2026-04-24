"""
Login / Splash-Screen Window.

Shows a circular progress animation, then slides to reveal
username/password fields.  On successful login, opens MainWindow.
"""

from PySide6.QtCore import Qt, QTimer, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from app.ui.ui_login import Ui_Login
from app.widgets import CircularProgress


# Splash counter
_counter = 0


class LoginWindow(QMainWindow):
    """Frameless login window with animated splash screen."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # Frameless + transparent
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Circular progress
        self.progress = CircularProgress()
        self.progress.width = 240
        self.progress.height = 240
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 4
        self.progress.progress_color = QColor("#2c7be5")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#232e3c")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

        # Drop shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(shadow)

        # Timer — drives the splash progress
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_progress)
        self.timer.start(30)

        # Key events for login fields
        self.ui.username.keyReleaseEvent = self._check_login
        self.ui.password.keyReleaseEvent = self._check_login

        # Close button
        self.ui.close_app_btn.clicked.connect(self.close)

        self.show()

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _check_login(self, event):
        """Validate credentials on Enter/Return key press."""
        if event.key() not in (Qt.Key_Return, Qt.Key_Enter):
            return

        username = self.ui.username.text()
        password = self.ui.password.text()

        if username and password == "123456" or username == "" and password == "":
            self.ui.user_description.setText(f"Welcome {username}!")
            self.ui.user_description.setStyleSheet(
                "#user_description { color: #bdff00 }"
            )
            self.ui.username.setStyleSheet(
                "#username:focus { border: 3px solid #bdff00; }"
            )
            self.ui.password.setStyleSheet(
                "#password:focus { border: 3px solid #bdff00; }"
            )
            QTimer.singleShot(400, lambda: self._open_main(username))
        else:
            self.ui.username.setStyleSheet(
                "#username:focus { border: 3px solid rgb(255, 0, 127); }"
            )
            self.ui.password.setStyleSheet(
                "#password:focus { border: 3px solid rgb(255, 0, 127); }"
            )
            self._shake_window()

    def _open_main(self, username: str):
        """Launch the main application window and close login."""
        from app.views.main_window import MainWindow  # lazy to avoid circular

        self.main = MainWindow()
        self.main.show()
        self.close()

    def _shake_window(self):
        """Quick horizontal shake to indicate an error."""
        pos = self.pos()
        offsets = [1, -2, 4, -5, 4, -2, 0]
        for i, dx in enumerate(offsets):
            QTimer.singleShot(i * 50, lambda x=dx: self.move(pos.x() + x, pos.y()))

    def _update_progress(self):
        """Advance the splash counter; switch to login form at 100 %."""
        global _counter
        self.progress.set_value(_counter)
        if _counter >= 100:
            self.timer.stop()
            self._animation_login()
        _counter += 1

    def _animation_login(self):
        """Slide the widget frame upward to reveal the login fields."""
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(
            QRect(
                0, 70,
                self.ui.frame_widgets.width(),
                self.ui.frame_widgets.height(),
            )
        )
        self.animation.setEndValue(
            QRect(
                0, -325,
                self.ui.frame_widgets.width(),
                self.ui.frame_widgets.height(),
            )
        )
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

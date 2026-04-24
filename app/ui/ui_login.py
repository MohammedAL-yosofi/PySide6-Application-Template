"""
Login / Splash-Screen UI definition.

Defines the layout for the login window: circular progress area,
logo, username/password fields, and close button.
"""

from PySide6.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFrame, QLabel,
    QLineEdit, QPushButton, QSpacerItem, QSizePolicy,
)

from app.ui import resources_rc  # noqa: F401  — registers Qt resources


class Ui_Login:
    """UI layout for the login/splash window."""

    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(300, 420)
        Login.setMinimumSize(QSize(300, 420))
        Login.setMaximumSize(QSize(300, 420))
        Login.setStyleSheet(_LOGIN_STYLE)

        # --- Central widget ---
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # --- Background frame ---
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName("bg")
        self.bg.setFrameShape(QFrame.NoFrame)

        # --- Frame widgets (animated slider) ---
        self.frame_widgets = QFrame(self.bg)
        self.frame_widgets.setObjectName("frame_widgets")
        self.frame_widgets.setGeometry(QRect(0, 70, 280, 720))
        self.frame_widgets.setMinimumSize(QSize(280, 720))
        self.frame_widgets.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)

        # Preloader (circular progress host)
        self.preloader = QFrame(self.frame_widgets)
        self.preloader.setObjectName("preloader")
        self.preloader.setMinimumSize(QSize(240, 240))
        self.preloader.setMaximumSize(QSize(260, 260))
        self.preloader.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2.addWidget(self.preloader)

        # Spacer
        self.verticalLayout_2.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Logo image
        self.logo = QLabel(self.frame_widgets)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(0, 260))
        self.logo.setStyleSheet(
            "#logo { border-radius: 10px; background-position: center; "
            "background-repeat: no-repeat; }"
        )
        pixmap = QPixmap(":/images_svg/images/images_svg/logo_home.png")
        if not pixmap.isNull():
            scaled = pixmap.scaled(
                self.logo.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation,
            )
            self.logo.setPixmap(scaled)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2.addWidget(self.logo)
       

        # close button (positioned absolutely)

        self.close_app_btn = QPushButton(self.bg)
        self.close_app_btn.setObjectName("close_app_btn")
        self.close_app_btn.setGeometry(QRect(242, 10, 28, 28))
        self.close_app_btn.setMinimumSize(QSize(28, 28))
        self.close_app_btn.setMaximumSize(QSize(28, 28))
        self.close_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_app_btn.setIconSize(QSize(20, 20))

        # User description label
        self.user_description = QLabel(self.frame_widgets)
        self.user_description.setObjectName("user_description")
        self.user_description.setStyleSheet("background: transparent;")
        self.verticalLayout_2.addWidget(self.user_description)

        # Username field
        self.username = QLineEdit(self.frame_widgets)
        self.username.setObjectName("username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_2.addWidget(self.username)

        # Password field
        self.password = QLineEdit(self.frame_widgets)
        self.password.setObjectName("password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setMaximumSize(QSize(16777215, 40))
        self.password.setEchoMode(QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.password)

        # Finalise
        self.verticalLayout.addWidget(self.bg)
        Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(
            QCoreApplication.translate("Login", "School Management System", None)
        )
        self.user_description.setText(
            QCoreApplication.translate("Login", "Login (pass: 123456):", None)
        )
        self.username.setPlaceholderText(
            QCoreApplication.translate("Login", "Username", None)
        )
        self.password.setPlaceholderText(
            QCoreApplication.translate("Login", "Password", None)
        )
        self.close_app_btn.setToolTip(
            QCoreApplication.translate("Login", "Close", None)
        )


# ---------------------------------------------------------------------------
# Stylesheet
# ---------------------------------------------------------------------------

_LOGIN_STYLE = """
#bg {
    background-color: #121e2d;
    border-radius: 10px;
}
#close_app_btn {
    background-image: url(:/icons_svg/images/icons_svg/icon_close.svg);
    background-position: center;
    background-repeat: no-repeat;
    border: none;
    background-color: transparent;
    border-radius: 8px;
}
#close_app_btn:hover  { background-color: rgb(255, 0, 127); }
#close_app_btn:pressed { background-color: rgb(172, 229, 0); }

QLabel {
    color: rgb(121, 121, 121);
    padding-left: 10px;
    padding-top: 20px;
}
.QLineEdit {
    border: 1.5px solid #232e3c;
    border-radius: 15px;
    background-color: #121e2d;
    color: rgb(121, 121, 121);
    padding-left: 10px;
    padding-right: 10px;
    background-repeat: none;
    background-position: left center;
}
.QLineEdit:hover {
    color: rgb(230, 230, 230);
    border: 1.5px solid rgb(62, 63, 66);
}
.QLineEdit:focus {
    color: rgb(230, 230, 230);
    border: 1.5px solid #2c7be5;
}
"""

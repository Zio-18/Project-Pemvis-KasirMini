import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from database.db import init_database


def main():

    init_database()

    app = QApplication(sys.argv)

    with open("assets/style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
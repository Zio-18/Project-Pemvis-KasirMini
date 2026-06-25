from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QHBoxLayout,
    QStackedWidget
)

from ui.dashboard_page import DashboardPage
from ui.product_page import ProductPage
from ui.cashier_page import CashierPage
from ui.history_page import HistoryPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CashFlow")
        self.resize(1200, 700)

        self.create_menu()
        self.create_statusbar()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItems([
            "Dashboard",
            "Produk",
            "Kasir",
            "Riwayat"
        ])

        # Stack halaman
        self.stack = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.product_page = ProductPage()
        self.cashier_page = CashierPage()
        self.history_page = HistoryPage()

        # Refresh otomatis setelah transaksi berhasil
        self.cashier_page.transaction_finished.connect(
            self.dashboard_page.load_dashboard
        )

        self.cashier_page.transaction_finished.connect(
            self.product_page.load_data
        )

        self.cashier_page.transaction_finished.connect(
            self.history_page.load_data
        )

        # Tambahkan halaman
        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.product_page)
        self.stack.addWidget(self.cashier_page)
        self.stack.addWidget(self.history_page)

        # Ganti halaman
        self.sidebar.currentRowChanged.connect(
            self.change_page
        )

        self.sidebar.setCurrentRow(0)

        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.stack, 5)

        central_widget.setLayout(layout)

    # ===============================
    # GANTI HALAMAN + REFRESH DATA
    # ===============================
    def change_page(self, index):

        self.stack.setCurrentIndex(index)

        if index == 0:
            self.dashboard_page.load_dashboard()

        elif index == 1:
            self.product_page.load_data()

        elif index == 3:
            self.history_page.load_data()

    # ===============================
    # MENU
    # ===============================
    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        menu.addMenu("Help")

        file_menu.addAction("Exit", self.close)

    # ===============================
    # STATUS BAR
    # ===============================
    def create_statusbar(self):

        self.statusBar().showMessage(
            "Sultan Kusuma Jaya | Hilya Fitri | Muhammad Zia Ul Haq"
        )
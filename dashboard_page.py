from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame
)
from PySide6.QtCore import Qt

from models.product_model import ProductModel
from models.transaction_model import TransactionModel


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(20)

        title = QLabel("Dashboard CashFlow")
        title.setObjectName("title")

        subtitle = QLabel(
            "Ringkasan informasi produk, stok, transaksi, dan pendapatan."
        )
        subtitle.setObjectName("subtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        grid = QGridLayout()
        grid.setSpacing(20)

        self.total_produk = self.create_card()
        self.total_stok = self.create_card()
        self.total_transaksi = self.create_card()
        self.pendapatan = self.create_card()

        grid.addWidget(self.total_produk, 0, 0)
        grid.addWidget(self.total_stok, 0, 1)
        grid.addWidget(self.total_transaksi, 1, 0)
        grid.addWidget(self.pendapatan, 1, 1)

        layout.addLayout(grid)

        self.setLayout(layout)

        self.load_dashboard()

    def create_card(self):

        card = QLabel()
        card.setObjectName("dashboardCard")
        card.setMinimumHeight(180)
        card.setAlignment(Qt.AlignCenter)

        return card

    def load_dashboard(self):

        self.total_produk.setText(f"""
<div align="center">
<p style="font-size:38px;">📦</p>
<p style="font-size:16px;color:#666;">Total Produk</p>
<h1>{ProductModel.total_products()}</h1>
</div>
""")

        self.total_stok.setText(f"""
<div align="center">
<p style="font-size:38px;">📚</p>
<p style="font-size:16px;color:#666;">Total Stok</p>
<h1>{ProductModel.total_stock()}</h1>
</div>
""")

        self.total_transaksi.setText(f"""
<div align="center">
<p style="font-size:38px;">🧾</p>
<p style="font-size:16px;color:#666;">Total Transaksi</p>
<h1>{TransactionModel.get_total_transactions()}</h1>
</div>
""")

        self.pendapatan.setText(f"""
<div align="center">
<p style="font-size:38px;">💰</p>
<p style="font-size:16px;color:#666;">Pendapatan</p>
<h1>Rp {TransactionModel.get_total_income():,.0f}</h1>
</div>
""")
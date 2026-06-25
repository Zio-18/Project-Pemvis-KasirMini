from datetime import datetime
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHeaderView

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QSpinBox,
    QLineEdit,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem
)

from models.product_model import ProductModel
from models.transaction_model import TransactionModel


class CashierPage(QWidget):

    transaction_finished = Signal()

    def __init__(self):
        super().__init__()

        self.cart = []

        self.init_ui()
        self.load_products()

    def init_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Kasir")
        title.setObjectName("title")

        layout.addWidget(title)

        top = QHBoxLayout()

        top.setSpacing(15)

        self.product_combo = QComboBox()

        self.qty_input = QSpinBox()

        self.qty_input.setMinimum(1)
        self.qty_input.setMaximum(999)
        self.qty_input.setValue(1)

        btn_add = QPushButton("Tambah")

        self.product_combo.setMinimumWidth(600)
        self.qty_input.setMinimumWidth(120)
        btn_add.setMinimumWidth(200)

        btn_add.clicked.connect(self.add_to_cart)

        top.addWidget(self.product_combo, 6)   # Produk lebih lebar
        top.addWidget(self.qty_input, 2)       # Qty sedang
        top.addWidget(btn_add, 3)              # Tombol besar

        layout.addLayout(top)

        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Produk",
            "Qty",
            "Harga",
            "Subtotal"
        ])

        layout.addWidget(self.table)

        self.total_label = QLabel(
            "Total : Rp 0"
        )

        layout.addWidget(self.total_label)

        payment_layout = QHBoxLayout()

        self.payment_input = QLineEdit()
        self.payment_input.setPlaceholderText(
            "Jumlah pembayaran"
        )

        payment_layout.addWidget(
            self.payment_input
        )

        btn_pay = QPushButton(
            "Bayar"
        )

        btn_pay.clicked.connect(
            self.process_payment
        )

        payment_layout.addWidget(btn_pay)

        layout.addLayout(payment_layout)

        self.setLayout(layout)

    def load_products(self):

        self.product_combo.clear()

        products = ProductModel.get_all()

        for p in products:

            self.product_combo.addItem(
                f"{p[2]} | Stok:{p[5]}",
                p[0]
            )

    def add_to_cart(self):

        if self.qty_input.value() <= 0:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Jumlah harus lebih dari 0"
            )
            return

        product_id = self.product_combo.currentData()

        product = ProductModel.get_by_id(
            product_id
        )

        qty = self.qty_input.value()

        if qty > product[5]:

            QMessageBox.warning(
                self,
                "Error",
                "Stok tidak mencukupi"
            )
            return

        subtotal = qty * product[4]

        self.cart.append({
            "id": product[0],
            "name": product[2],
            "price": product[4],
            "qty": qty,
            "subtotal": subtotal
        })

        self.refresh_cart()

    def refresh_cart(self):

        self.table.setRowCount(
            len(self.cart)
        )

        total = 0

        for row, item in enumerate(self.cart):

            self.table.setItem(
                row, 0,
                QTableWidgetItem(
                    str(item["id"])
                )
            )

            self.table.setItem(
                row, 1,
                QTableWidgetItem(
                    item["name"]
                )
            )

            self.table.setItem(
                row, 2,
                QTableWidgetItem(
                    str(item["qty"])
                )
            )

            self.table.setItem(
                row, 3,
                QTableWidgetItem(
                    str(item["price"])
                )
            )

            self.table.setItem(
                row, 4,
                QTableWidgetItem(
                    str(item["subtotal"])
                )
            )

            total += item["subtotal"]

        self.total_label.setText(
            f"Total : Rp {total:,.0f}"
        )

    def process_payment(self):

        if len(self.cart) == 0:

            QMessageBox.warning(
                self,
                "Error",
                "Keranjang kosong"
            )

            return

        total = sum(
            item["subtotal"]
            for item in self.cart
        )

        try:
            payment = float(
                self.payment_input.text()
            )
        except:
            QMessageBox.warning(
                self,
                "Error",
                "Pembayaran tidak valid"
            )
            return

        if payment < total:

            QMessageBox.warning(
                self,
                "Error",
                "Uang kurang"
            )
            return

        change = payment - total

        transaction_id = (
            TransactionModel
            .create_transaction(
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                total,
                payment,
                change
            )
        )

        for item in self.cart:

            TransactionModel.create_detail(
                transaction_id,
                item["id"],
                item["qty"],
                item["price"],
                item["subtotal"]
            )

            ProductModel.reduce_stock(
                item["id"],
                item["qty"]
            )

        QMessageBox.information(
            self,
            "Sukses",
            f"""
Transaksi berhasil

Total :
Rp {total:,.0f}

Bayar :
Rp {payment:,.0f}

Kembalian :
Rp {change:,.0f}
"""
        )

        self.cart.clear()

        self.table.setRowCount(0)

        self.payment_input.clear()

        self.total_label.setText(
            "Total : Rp 0"
        )

        self.load_products()

        self.transaction_finished.emit()
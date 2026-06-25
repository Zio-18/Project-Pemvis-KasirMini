from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from models.product_model import ProductModel
from ui.dialogs.product_dialog import ProductDialog


class ProductPage(QWidget):

    def __init__(self):
        super().__init__()

        self.selected_id = None

        self.init_ui()
        self.load_data()

    def init_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Manajemen Produk")
        title.setObjectName("title")

        layout.addWidget(title)

        top_layout = QHBoxLayout()

        top_layout.setSpacing(12)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Cari produk..."
        )

        btn_add = QPushButton("Tambah")
        btn_edit = QPushButton("Edit")
        btn_delete = QPushButton("Hapus")

        btn_add.clicked.connect(self.add_product)
        btn_edit.clicked.connect(self.edit_product)
        btn_delete.clicked.connect(self.delete_product)

        self.search_input.textChanged.connect(
            self.search_data
        )
        
        self.search_input.setMinimumWidth(500)

        btn_add.setMinimumWidth(130)
        btn_edit.setMinimumWidth(110)
        btn_delete.setMinimumWidth(110)

        top_layout.addWidget(self.search_input, 7)
        top_layout.addWidget(btn_add, 1)
        top_layout.addWidget(btn_edit, 1)
        top_layout.addWidget(btn_delete, 1)

        layout.addLayout(top_layout)

        self.table = QTableWidget()

        self.table.verticalHeader().setDefaultSectionSize(25)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setSelectionMode(
            QTableWidget.SingleSelection
        )

        self.table.setShowGrid(False)

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Kode",
            "Nama",
            "Kategori",
            "Harga",
            "Stok"
        ])

        self.table.cellClicked.connect(
            self.select_row
        )

        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_data(self):

        data = ProductModel.get_all()

        self.table.setRowCount(len(data))

        for row, product in enumerate(data):

            for col, value in enumerate(product):

                item = QTableWidgetItem(str(value))

                item.setTextAlignment(Qt.AlignCenter)

                self.table.setItem(
                    row,
                    col,
                    item
                )

    def search_data(self):

        keyword = self.search_input.text()

        data = ProductModel.search(keyword)

        self.table.setRowCount(len(data))

        for row, product in enumerate(data):

            for col, value in enumerate(product):

                item = QTableWidgetItem(str(value))

                item.setTextAlignment(Qt.AlignCenter)

                self.table.setItem(
                    row,
                    col,
                    item
                )

    def select_row(self, row, column):

        self.selected_id = int(
            self.table.item(row, 0).text()
        )

    def add_product(self):

        dialog = ProductDialog()

        if dialog.exec():

            ProductModel.insert(
                dialog.get_data()
            )

            self.load_data()

    def edit_product(self):

        if not self.selected_id:

            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data terlebih dahulu"
            )
            return

        row = self.table.currentRow()

        data = []

        for col in range(6):

            item = self.table.item(row, col)

            if item:
                data.append(item.text())
            else:
                data.append("")

        dialog = ProductDialog(data)

        if dialog.exec():

            ProductModel.update(
                self.selected_id,
                dialog.get_data()
            )

            self.load_data()

    def delete_product(self):

        if not self.selected_id:

            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data terlebih dahulu"
            )
            return

        confirm = QMessageBox.question(
            self,
            "Konfirmasi",
            "Hapus produk ini?"
        )

        if confirm == QMessageBox.Yes:

            ProductModel.delete(
                self.selected_id
            )

            self.load_data()

            self.selected_id = None
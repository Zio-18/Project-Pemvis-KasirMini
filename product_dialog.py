from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class ProductDialog(QDialog):

    def __init__(self, data=None):
        super().__init__()

        self.setWindowTitle("Form Produk")
        self.resize(400, 250)

        layout = QFormLayout()

        self.code_input = QLineEdit()
        self.name_input = QLineEdit()
        self.category_input = QLineEdit()
        self.price_input = QLineEdit()
        self.stock_input = QLineEdit()

        layout.addRow("Kode", self.code_input)
        layout.addRow("Nama", self.name_input)
        layout.addRow("Kategori", self.category_input)
        layout.addRow("Harga", self.price_input)
        layout.addRow("Stok", self.stock_input)

        self.btn_save = QPushButton("Simpan")
        self.btn_save.clicked.connect(self.validate)

        layout.addRow(self.btn_save)

        self.setLayout(layout)

        if data:
            self.code_input.setText(data[1])
            self.name_input.setText(data[2])
            self.category_input.setText(data[3])
            self.price_input.setText(str(data[4]))
            self.stock_input.setText(str(data[5]))

    def validate(self):

        if self.code_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Kode produk wajib diisi"
            )
            return

        if self.name_input.text() == "":
            QMessageBox.warning(
                self,
                "Error",
                "Nama produk wajib diisi"
            )
            return

        try:
            float(self.price_input.text())
            int(self.stock_input.text())
        except:
            QMessageBox.warning(
                self,
                "Error",
                "Harga/Stok tidak valid"
            )
            return

        self.accept()

    def get_data(self):
        return (
            self.code_input.text(),
            self.name_input.text(),
            self.category_input.text(),
            float(self.price_input.text()),
            int(self.stock_input.text())
        )
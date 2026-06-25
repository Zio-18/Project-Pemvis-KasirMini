from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from models.transaction_model import (
    TransactionModel
)

from utils.export_csv import (
    export_transaction_csv
)

from utils.export_pdf import (
    export_transaction_pdf
)


class HistoryPage(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.load_data()

    def init_ui(self):

        layout = QVBoxLayout()

        title = QLabel(
            "Riwayat Transaksi"
        )

        title.setObjectName("title")

        layout.addWidget(title)

        top = QHBoxLayout()

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Cari tanggal transaksi..."
        )

        self.search_input.textChanged.connect(
            self.search_data
        )

        btn_csv = QPushButton(
            "Export CSV"
        )

        btn_pdf = QPushButton(
            "Export PDF"
        )

        btn_csv.clicked.connect(
            self.export_csv
        )

        btn_pdf.clicked.connect(
            self.export_pdf
        )

        top.addWidget(self.search_input)
        top.addWidget(btn_csv)
        top.addWidget(btn_pdf)

        layout.addLayout(top)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Tanggal",
            "Total",
            "Bayar",
            "Kembalian"
        ])

        self.table.horizontalHeader()\
            .setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_data(self):

        data = (
            TransactionModel
            .get_all_transactions()
        )

        self.show_data(data)

    def show_data(self, data):

        self.table.setRowCount(
            len(data)
        )

        for row, item in enumerate(data):

            for col, value in enumerate(item):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )

    def search_data(self):

        keyword = (
            self.search_input.text()
        )

        data = (
            TransactionModel
            .search_transaction(
                keyword
            )
        )

        self.show_data(data)

    def export_csv(self):

        data = (
            TransactionModel
            .get_all_transactions()
        )

        file_name, _ = (
            QFileDialog
            .getSaveFileName(
                self,
                "Export CSV",
                "",
                "CSV Files (*.csv)"
            )
        )

        if file_name:

            export_transaction_csv(
                data,
                file_name
            )

    def export_pdf(self):

        data = (
            TransactionModel
            .get_all_transactions()
        )

        file_name, _ = (
            QFileDialog
            .getSaveFileName(
                self,
                "Export PDF",
                "",
                "PDF Files (*.pdf)"
            )
        )

        if file_name:

            export_transaction_pdf(
                data,
                file_name
            )
from reportlab.platypus import (
    SimpleDocTemplate,
    Table
)


def export_transaction_pdf(
        data,
        filename):

    pdf = SimpleDocTemplate(filename)

    table_data = [[
        "ID",
        "Tanggal",
        "Total",
        "Bayar",
        "Kembalian"
    ]]

    for row in data:
        table_data.append(list(row))

    table = Table(table_data)

    pdf.build([table])
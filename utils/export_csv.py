import csv


def export_transaction_csv(data, filename):

    with open(
            filename,
            "w",
            newline="",
            encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Tanggal",
            "Total",
            "Bayar",
            "Kembalian"
        ])

        for row in data:
            writer.writerow(row)
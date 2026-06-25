from database.db import get_connection


class TransactionModel:

    @staticmethod
    def create_transaction(
            transaction_date,
            total,
            payment,
            change_amount):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions(
            transaction_date,
            total,
            payment,
            change_amount
        )
        VALUES(?,?,?,?)
        """, (
            transaction_date,
            total,
            payment,
            change_amount
        ))

        transaction_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return transaction_id

    @staticmethod
    def create_detail(
            transaction_id,
            product_id,
            quantity,
            price,
            subtotal):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transaction_details(
            transaction_id,
            product_id,
            quantity,
            price,
            subtotal
        )
        VALUES(?,?,?,?,?)
        """, (
            transaction_id,
            product_id,
            quantity,
            price,
            subtotal
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_transactions():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM transactions
        ORDER BY id DESC
        """)

        data = cursor.fetchall()

        conn.close()

        return data


    @staticmethod
    def search_transaction(keyword):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM transactions
        WHERE transaction_date LIKE ?
        """, (f"%{keyword}%",))

        data = cursor.fetchall()

        conn.close()

        return data


    @staticmethod
    def get_total_income():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT IFNULL(SUM(total),0)
        FROM transactions
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total


    @staticmethod
    def get_total_transactions():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM transactions
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total
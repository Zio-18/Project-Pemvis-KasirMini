from database.db import get_connection


class ProductModel:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM products
        ORDER BY id DESC
        """)

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def search(keyword):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM products
        WHERE
            code LIKE ?
            OR name LIKE ?
            OR category LIKE ?
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        data = cursor.fetchall()

        conn.close()

        return data

    @staticmethod
    def insert(data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO products
        (
            code,
            name,
            category,
            price,
            stock
        )
        VALUES(?,?,?,?,?)
        """, data)

        conn.commit()
        conn.close()

    @staticmethod
    def update(product_id, data):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE products
        SET
            code=?,
            name=?,
            category=?,
            price=?,
            stock=?
        WHERE id=?
        """, (
            *data,
            product_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete(product_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM products
        WHERE id=?
        """, (product_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(product_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM products
        WHERE id=?
        """, (product_id,))

        data = cursor.fetchone()

        conn.close()

        return data


    @staticmethod
    def reduce_stock(product_id, qty):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE products
        SET stock = stock - ?
        WHERE id=?
        """, (qty, product_id))

        conn.commit()
        conn.close()
    
    @staticmethod
    def total_products():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM products
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total


    @staticmethod
    def total_stock():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT IFNULL(
            SUM(stock),0
        )
        FROM products
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total
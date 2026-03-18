from app import mysql

def insert_url(original_url, short_code, description):
    with mysql.cursor() as cursor:
        sql = """
        INSERT INTO urls (original_url, short_code, description)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (original_url, short_code, description))
    mysql.commit()


def get_by_original(original_url):
    with mysql.cursor() as cursor:
        cursor.execute("SELECT * FROM urls WHERE original_url=%s", (original_url,))
        return cursor.fetchone()


def get_by_code(code):
    with mysql.cursor() as cursor:
        cursor.execute("SELECT * FROM urls WHERE short_code=%s", (code,))
        return cursor.fetchone()


def get_all():
    with mysql.cursor() as cursor:
        cursor.execute("SELECT * FROM urls ORDER BY created_at DESC")
        return cursor.fetchall()
import mysql.connector
from nameko.extensions import DependencyProvider

class DatabaseWrapper:
    def __init__(self, connection):
        self.connection = connection

    def query(self, sql, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute(self, sql, params=None):
        cursor = self.connection.cursor()
        cursor.execute(sql, params or ())
        self.connection.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id

class Database(DependencyProvider):
    def setup(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # ganti sesuai konfigurasi Anda
            database="soa_project_2025"
        )

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection)

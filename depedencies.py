import mysql.connector
import time
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
        retries = 5
        for i in range(retries):
            try:
                self.connection = mysql.connector.connect(
                    host="mysql",       # sesuai nama service docker-compose
                    user="root",
                    password="root",
                    database="soa_project_2025"
                )
                print("✅ Berhasil konek ke database!")
                break
            except mysql.connector.Error as e:
                print(f"❌ Gagal koneksi DB: {e}, percobaan ke-{i+1}")
                time.sleep(3)
        else:
            raise Exception("Tidak bisa konek ke database setelah beberapa percobaan.")

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection)

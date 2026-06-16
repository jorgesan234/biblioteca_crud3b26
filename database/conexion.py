import psycopg2
class Conexion:
    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host="localhost",
            database="biblioteca_3b26",
            user="postgres",
            password="12345",
            port=5432
        )
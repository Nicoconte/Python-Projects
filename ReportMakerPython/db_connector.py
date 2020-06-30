import mysql.connector

class db_connector:
    def get_connection(self):
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="databasepiranha"
            )
            print("Conexion exitosa")

            return mydb

        except:
            print("No se pudo conectar con la base")
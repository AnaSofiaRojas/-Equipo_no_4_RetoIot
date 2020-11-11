import mysql.connector
from mysql.connector import Error
import numpy as np
import datetime

def insertVariablesIntoUser(id_usuario, nombre, apellido, edad):
        mySql_query = """INSERT INTO usuario (id_usuario, nombre, apellido, edad)
                            VALUES
                            (%s, %s, %s, %s) """

        recordTuple = (id_usuario, nombre, apellido, edad)
        cursor.execute(mySql_query, recordTuple)
        connection.commit()

def insertVariblesIntoTable(id_datos, oxigeno, ritmo, covid, fecha, usuario):

        mySql_insert_query = """INSERT INTO datos (id_datos, oxigeno, ritmo, covid, fecha, usuario) 
                                   VALUES 
                                   (%s, %s, %s, %s, %s, %s) """
        recordTuple = (id_datos, oxigeno, ritmo, covid, fecha, usuario)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()


if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Reto_iot',
                                             user='root',
                                             password='Engrapadora50*')

        cursor = connection.cursor()
        nombres = ["Ivan", "Sofia", "Lia", "Juan", "Javier"]
        apellidos = ["Manzano", "Rojas", "Nuñez", "Hormaza", "Corona"]

        for j in range(5):
            edad = np.random.randint(18, 30)
            insertVariablesIntoUser(j + 1, nombres[j], apellidos[j], edad)

        for i in range(5000):
            date = datetime.datetime.now()
            oxygen = np.random.randint(80, 100)
            rythm = np.random.randint(50, 100)
            if oxygen < 90 and rythm < 60:
                covid = 1
            else:
                covid = 0

            if i < 1000:
                insertVariblesIntoTable(i + 1, oxygen, rythm, covid, date, 1)
            if 1000 < i < 2000:
                insertVariblesIntoTable(i + 1, oxygen, rythm, covid, date, 2)
            if 2000 < i < 3000:
                insertVariblesIntoTable(i + 1, oxygen, rythm, covid, date, 3)
            if 3000 < i < 4000:
                insertVariblesIntoTable(i + 1, oxygen, rythm, covid, date, 4)
            else:
                insertVariblesIntoTable(i + 1, oxygen, rythm, covid, date, 5)

        cursor.close()
        connection.close()
        print("Record inserted successfully into tables")

    except mysql.connector.Error as error:

        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
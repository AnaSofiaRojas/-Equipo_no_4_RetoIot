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

def insertVariblesIntoTable(id_datos,id_usuario, oxigeno, ritmo, covid, fecha):

        mySql_insert_query = """INSERT INTO datos (id_datos,id_usuario,oxigeno, ritmo, covid, fecha) 
                                   VALUES 
                                   (%s, %s, %s, %s, %s, %s) """
        recordTuple = (id_datos,id_usuario, oxigeno, ritmo, covid, fecha)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()


if __name__ == '__main__':

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='reto',
                                             user='root',
                                             password='liamichelle23')

        cursor = connection.cursor()
        nombres = ["Ivan", "Sofia", "Lia", "Juan", "Javier"]
        apellidos = ["Manzano", "Rojas", "Nuñez", "Hormaza", "Corona"]

        for i in range(5):
            edad = np.random.randint(18, 30)
            insertVariablesIntoUser(i + 1, nombres[i], apellidos[i], edad)
            for j in range(1000):
                date = datetime.datetime.now()
                oxygen = np.random.randint(80, 100)
                rythm = np.random.randint(50, 100)
                if oxygen < 90 and rythm < 60:
                    covid =1
                else:
                    covid=0

                insertVariblesIntoTable(j + 1,i+1,oxygen, rythm, covid, date)
                

        #for i in range(5000):
        #    date = datetime.datetime.now()
        #    oxygen = np.random.randint(80, 100)
        #    rythm = np.random.randint(50, 100)
        #    if oxygen < 90 and rythm < 60:
        #        covid = 1
        #    else:
        #        covid = 0

        #    if (1000 >= i):
        #        insertVariblesIntoTable(i + 1,1,oxygen, rythm, covid, date)

        #    elif (1000 < i) and (2000 >= i):
        #        insertVariblesIntoTable(i + 1,2, oxygen, rythm, covid, date)

        #    elif (i >2000) and (i <= 3000):
        #        insertVariblesIntoTable(i + 1,3, oxygen, rythm, covid, date)

        #    elif (i >3000) and (i <= 4000):
        #        insertVariblesIntoTable(i + 1,4, oxygen, rythm, covid, date)

        #    else:
        #        insertVariblesIntoTable(i + 1,5, oxygen, rythm, covid, date)

        cursor.close()
        connection.close()
        print("Record inserted successfully into tables")

    except mysql.connector.Error as error:

        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
# Ejemplo de conexion con Python a MySQL, insercion y lectura

import pymysql, getpass

# Abrir conexión a la base de datos

user = input (" usuario: ")
pswd = getpass.getpass('Password:')
user = "'" + user + "'"
pswd = "'" + pswd + "'"

try:
    connection = pymysql.connect(
                unix_socket="/opt/lampp/var/mysql/mysql.sock",
                host='localhost', # o localhost si tu levantaste el servidor
                user= user,
                passwd= pswd,
                db='python',
                charset='utf8mb4',                        #devolver tablas como diccionario
                cursorclass=pymysql.cursors.DictCursor)   #devolver tablas como diccionario

    nombre = input ("Ingrese Nombre : ")
    mail = input ("Ingresa mail : ")

    with connection.cursor() as cursor:
        sql = "INSERT INTO test (name, email) VALUES ('" + nombre + "', '" + mail  + "');"
        cursor.execute(sql)
        print("Ingresado")
        connection.commit()
        sql = "SELECT * FROM test where name='" + nombre  + "';"
        cursor.execute(sql)
        x= cursor.fetchall()
        for row in x:
            #print("{0} {1} {2}".format(row[0], row[1], row[2]))
            print(row["id"], row["email"])

        cursor.execute("SELECT * FROM test WHERE id IN (1, 2, 3)")

#        rows = cursor.fetchall()

#        for row in rows:
#            print("{0} {1} {2}".format(row[0], row[1], row[2]))

        print("La consulta afectó a {} filas".format(cursor.rowcount))
    
except:
    connection.rollback()
finally:
    connection.close()
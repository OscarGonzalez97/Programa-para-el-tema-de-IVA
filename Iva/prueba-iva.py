import psycopg2
#from psycopg2 import Error
try:
    connection = psycopg2.connect(user = "oscar",
                                  password = "",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "prueba")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    create_table_query = "CREATE TABLE perros (id_perro INT PRIMARY KEY     NOT NULL, raza           TEXT, price         INT);"
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

import psycopg2
try:
    connection = psycopg2.connect(user = "oscar",
                                  password = "",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Manejador_iva")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")
    #Insert credito
    postgres_insert_query = " INSERT INTO "+ impuesto +" (monto, mes, anho) VALUES (%s,%s, %s)"
    record_to_insert = (aCargar, mes, anho)
    #insert debito
    # postgres_insert_query = " INSERT INTO "+ impuesto +" (monto, mes, anho, tipo) VALUES (%s,%s, %s, %s)"
    # record_to_insert = (aCargar, mes, anho,2)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into table: ", impuesto)

except (Exception, psycopg2.Error) as error :
    print(error.pgerror)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

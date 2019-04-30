import psycopg2
try:
    connection = psycopg2.connect(user = "oscar",
                                  password = "",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "prueba")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    #Funciona
    #Insert
    postgres_insert_query = " INSERT INTO iva10 (monto, mes, anho) VALUES (%s,%s, %s)"
    record_to_insert = (123, 'abril', 2019)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into gatos table")




except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
'''    import psycopg2
    try:
    connection = psycopg2.connect(user = "oscar",
                                  password = "",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "prueba")
       cursor = connection.cursor()
       postgres_insert_query = """ INSERT INTO perros (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
       record_to_insert = (5, 'One Plus 6', 950)
       cursor.execute(postgres_insert_query, record_to_insert)
       connection.commit()
       count = cursor.rowcount
       print (count, "Record inserted successfully into mobile table")
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")'''

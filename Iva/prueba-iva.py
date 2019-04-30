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
    #Insert para ingresar datos
    '''postgres_insert_query = " INSERT INTO iva10 (monto, mes, anho) VALUES (%s,%s, %s)"
    record_to_insert = (1000, 'abril', 2019)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into iva10 table")'''

    #Select para mostrar resultado
    mes='abril'
    anho=2019
    postgres_select_query="SELECT * FROM iva10 WHERE mes='"+mes+"' AND anho="+str(anho)
    cursor.execute(postgres_select_query)
    print("Selecting rows from iva10 table using cursor.fetchall")
    iva10_record = cursor.fetchall()

    print("Print each row and it's columns values")
    totalImpuesto=0
    for row in iva10_record:
        print("monto = ", row[0])
        totalImpuesto=totalImpuesto+row[0]
    print("Total Impuesto= ", totalImpuesto)
    aPagar=totalImpuesto*11-totalImpuesto
    print("APagar=", aPagar)

    #Delete para borrar datos (solo borrara montos)
    # Update single record now
    sql_delete_query = "Delete from iva10 where monto = %s AND mes=%s AND anho=%s"
    record_to_delete = (123, 'abril', 2019)
    cursor.execute(sql_delete_query, record_to_delete)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")

except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

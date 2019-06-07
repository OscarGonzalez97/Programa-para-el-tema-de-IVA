import psycopg2

def ingresa_entero(stringOpcion):
    '''Para solucionar el tema de que la persona ingrese algo no valido, mientras no sea un numero positivo o cero no va salir de esta excepcion'''
    ban2=True
    while ban2:
        try:
            opcion=int(input(stringOpcion))
            if opcion >= 0:
                ban2=False
            else:
                print("Elija un entero positivo")

        except:
            print("Opcion no valida.")
            print("\n")
    return opcion

def insert(impuesto,aCargar, mes, anho):
    '''Aqui se hara la conexion con la base de datos y se insertara un dato con el mes y anho correspondiente'''
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

def select_total(impuesto,mes, anho):
    '''Aqui se hara la conexion con la base de datos y traera el monto total del impuesto tanto credito como debito de ese impuesto'''
    try:
        connection = psycopg2.connect(user = "oscar",
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "Manejador_iva")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
        #Select para mostrar resultado credito
        postgres_select_query="SELECT * FROM "+impuesto+" WHERE mes='"+mes+"' AND anho="+str(anho)+" AND tipo=1"
        cursor.execute(postgres_select_query)
        iva_record = cursor.fetchall()

        totalImpuestoDB=0
        for row in iva_record:
            #print("monto = ", row[1])
            totalImpuestoDB=totalImpuestoDB+row[1]

        return(totalImpuestoDB)

    except (Exception, psycopg2.Error) as error :
        print(error.pgerror)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")

def eliminaDB(impuesto, monto, mes, anho):
    '''Aqui se hara la conexion con la base de datos y se eliminara un dato de la DB'''
    try:
        connection = psycopg2.connect(user = "oscar",
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "Manejador_iva")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
        #ATENCION
        postgres_select_query="SELECT "+impuesto+"_id FROM "+impuesto+" WHERE monto="+str(monto)+" LIMIT 1"
        cursor.execute(postgres_select_query)
        iva_record = cursor.fetchall()
        sql_delete_query = "DELETE FROM "+impuesto+" WHERE "+impuesto+"_id=%s"
        record_to_delete = (iva_record)
        cursor.execute(sql_delete_query, record_to_delete)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error :
        print(error.pgerror)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def select_mes(impuesto, mes, anho):
    '''Aqui se hara la conexion con la base de datos se traera una consulta y se imprimira 1 a 1'''
    try:
        connection = psycopg2.connect(user = "oscar",
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "Manejador_iva")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
        #Select para mostrar resultados credito
        postgres_select_query="SELECT * FROM "+impuesto+" WHERE mes='"+mes+"' AND anho="+str(anho)+" AND tipo=1"
        cursor.execute(postgres_select_query)
        iva_record = cursor.fetchall()
        print("\nCargado mes de "+ mes +" credito de "+impuesto+": \n")
        for row in iva_record:
            print("monto = ", row[1])
        #Select para mostrar resultados debito
        postgres_select_query="SELECT * FROM "+impuesto+" WHERE mes='"+mes+"' AND anho="+str(anho)+" AND tipo=2"
        cursor.execute(postgres_select_query)
        iva_record = cursor.fetchall()
        print("\nCargado mes de "+ mes +" debito de "+impuesto+": \n")
        for row in iva_record:
            print("monto = ", row[1])

    except (Exception, psycopg2.Error) as error :
        print(error.pgerror)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")

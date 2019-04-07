def ingresa_entero(stringOpcion):
    '''Para solucionar el tema de que la persona ingrese algo no valido, mientras no sea un numero no va salir de esta excepcion'''
    ban2=True
    while ban2:
        try:
            opcion=int(input(stringOpcion))
            #print("Ingresaste ", opcion)
            ban2=False
        except:
            print("Opcion no valida.")
            print("\n")
    return opcion

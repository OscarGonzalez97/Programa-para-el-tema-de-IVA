from iva10 import Iva10
from iva5 import Iva5
from exenta import Exenta

#Creo los objetos que son los tipos de impuesto
iva10=Iva10()
iva5=Iva5()
exenta=Exenta()

ban=True
#Solo va salir de esta parte cuando el operador ingrese la opcion 0
while ban:
    #Lo que hacemos aca es simplemente imprimir todas las opciones con print
    print("..:: Bienvenido al manejador de IVA para pequeños contribuyentes ::..")
    print("Elija la opcion que desea realizar: ")
    print("1- Cargar dato Iva 10%\n2- Cargar dato Iva 5%\n3- Cargar dato Exenta")
    print("4-Imprimir 5 últimos cargados de cada opción\n5-Eliminar valor\n6-Mostrar resultado para declaración\n0-SALIR")

    #Para solucionar el tema de que la persona ingrese algo no valido, mientras no sea un numero no va salir de esta excepcion
    ban2=True
    while ban2:
        try:
            opcion=int(input(">"))
            print("Ingresaste ", opcion)
            ban2=False
        except:
            print("opcion no valida perro")
            print("\n")
    #Una vez que tiene un int empieza a evaluar que opcion eligio si es 0 sale y si es una opcion no valida avisa
    if opcion == 1:
        print("VA cargar dato iva10")
        print("\n")
    elif opcion == 2:
        print("Va cargar dato iva 5")
        print("\n")
    elif opcion == 3:
        print("Va cargar dato Exenta")
        print("\n")
    elif opcion == 4:
        print("Va Imprimir 5 ultimos cargados")
        print("\n")
    elif opcion == 5:
        print("Eliminar valor")
        print("\n")
    elif opcion == 6:
        print("Mostrar resultados para declaracion")
        print("\n")
    elif opcion == 0:
        print("Apreto salid gg")
        print("\n")
        ban= False
    else:
        print("Ingrese una opcion valida")
        print("\n")

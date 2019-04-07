from iva10 import Iva10
from iva5 import Iva5
from exenta import Exenta
from funciones_utiles import *


def elimina_valor():
    ban=True
    print("\tDe que impuesto desea eliminar un valor?")
    print("\t1-Iva 10%")
    print("\t2-Iva 5%")
    print("\t3-Exenta")
    while ban:

        opcion=ingresa_entero(">")

        if opcion == 1:
            iva10.elimina()
            ban=False

        elif opcion == 2:
            iva5.elimina()
            ban=False

        elif opcion ==3:
            exenta.elimina()
            ban=False

        else:
            print("Ingrese una opcion valida")


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

    opcion=ingresa_entero(">")
    #Una vez que tiene un int empieza a evaluar que opcion eligio si es 0 sale y si es una opcion no valida avisa
    if opcion == 1:
        iva10.carga_dato()
        print("\n")

    elif opcion == 2:
        #print("Va cargar dato iva 5")
        iva5.carga_dato()
        print("\n")

    elif opcion == 3:
        #print("Va cargar dato Exenta")
        exenta.carga_dato()
        print("\n")

    elif opcion == 4:
        #print("Va Imprimir 5 ultimos cargados")
        iva10.imprimir_ultimos()
        iva5.imprimir_ultimos()
        exenta.imprimir_ultimos()
        print("\n")

    elif opcion == 5:
        #print("Eliminar valor")
        elimina_valor()
        print("\n")

    elif opcion == 6:
        print("Mostrar resultados para declaracion")
        iva10.imprimir()
        iva5.imprimir()
        exenta.imprimir()
        print("\n")

    elif opcion == 0:
        print("Saliendo...")
        print("\n")
        ban= False

    else:
        print("Ingrese una opcion valida")
        print("\n")

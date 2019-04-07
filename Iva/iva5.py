from impuesto import Impuesto
from funciones_utiles import *
#import psycopg2

class Iva5 (Impuesto):
    def carga_dato(self):
        '''Aqui se cargara el dato del Iva5, se agregara a lista de ultimos cargados,
        se sumara al total de Iva5 y se calculara lo que hay que cargar en el sistema'''
        archivoIva5=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasIva5.txt","a")
        aCargar= ingresa_entero("Carga Iva5> ")
        archivoIva5.write(str(aCargar))
        archivoIva5.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= (self.totalImpuesto*21) - self.totalImpuesto
        archivoIva5.write(str(self.cargarMarangatu))
        archivoIva5.write("\n")
        archivoIva5.close()

    def imprimir(self):
        '''Simplemente imprime en pantalla los resultados de Iva5 Total y el monto a cargar en el sistema Marangatu'''
        print("Iva 5 Total= ", self.totalImpuesto)
        print("Resultado a cargar Iva 5= ", self.cargarMarangatu)

    def elimina(self):
        '''Aqui se elimina un valor especifico, se resta del Iva5 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Iva5 a eliminar> ")
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= (self.totalImpuesto*21) - self.totalImpuesto

    def imprimir_ultimos(self):
        '''En esta funcion se imprime los ultimos resultados de Iva5 cargado'''
        print("Ultimos numeros cargados", self.ultimosNumeros[0:5])

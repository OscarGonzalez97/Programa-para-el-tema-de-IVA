from impuesto import Impuesto
from funciones_utiles import *
class Iva10 (Impuesto):
    def carga_dato(self):
        '''Aqui se cargara el dato del Iva10, se agregara a lista de ultimos cargados,
        se sumara al total de Iva10 y se calculara lo que hay que cargar en el sistema'''
        archivoIva10=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasIva10.txt","a")
        aCargar= ingresa_entero("Carga Iva10> ")
        archivoIva10.write(str(aCargar))
        archivoIva10.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto
        archivoIva10.write(str(self.cargarMarangatu))
        archivoIva10.write("\n")
        archivoIva10.close()

    def imprimir(self):
        '''Simplemente imprime en pantalla los resultados de Iva10 Total y el monto a cargar en el sistema Marangatu'''
        #print("Iva 10 Cargado | ")
        #print("\t      ",self.totalImpuesto,"|")
        print("Iva10Total= ", self.totalImpuesto)
        #print("\n")
        #print("Resultado a cargar | ")
        #print("\t      ",self.cargarMarangatu, "|")
        print("A cargar en sistema Iva 10:", self.cargarMarangatu)

    def elimina(self):
        '''Aqui se elimina un valor especifico, se resta del Iva10 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Iva 10 a eliminar> ")
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto

    def imprimir_ultimos(self):
        '''En esta funcion se imprime los ultimos resultados de Iva10 cargado'''
        print("Ultimos numeros cargados", self.ultimosNumeros[0:5])

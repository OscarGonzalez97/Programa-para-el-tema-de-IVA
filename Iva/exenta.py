from impuesto import Impuesto
from funciones_utiles import *

class Exenta (Impuesto):
    def carga_dato(self):
        '''Aqui se cargara el dato de Exenta, se agregara a lista de ultimos cargados,
        se sumara al total de Exenta y se calculara lo que hay que cargar en el sistema'''
        archivoExenta=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasExentas.txt","a")
        aCargar= ingresa_entero("Carga Exenta> ")
        archivoExenta.write(str(aCargar))
        archivoExenta.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= self.totalImpuesto
        archivoExenta.write(str(self.cargarMarangatu))
        archivoExenta.write("\n")
        archivoExenta.close()

    def imprimir(self):
        '''Simplemente imprime en pantalla los resultados de Exenta Total y el monto a cargar en el sistema Marangatu'''
        print("ExentaTotal= ", self.totalImpuesto)
        print("Resultado a cargar en exentas = ", self.cargarMarangatu)

    def elimina(self):
        '''Aqui se elimina un valor especifico, se resta del Exenta Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Exenta a eliminar> ")
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= self.totalImpuesto

    def imprimir_ultimos(self):
        '''En esta funcion se imprime los ultimos resultados Exenta cargado'''
        print("Ultimos numeros cargados", self.ultimosNumeros[0:5])

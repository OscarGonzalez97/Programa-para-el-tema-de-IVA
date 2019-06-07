from impuesto import Impuesto
from funciones_utiles import *

class Iva5 (Impuesto):
    impuesto='iva5'
    def carga_dato(self,mes,anho):
        '''Aqui se cargara el dato del Iva5, se agregara a lista de ultimos cargados,
        se sumara al total de Iva5 y se calculara lo que hay que cargar en el sistema'''

        aCargar= ingresa_entero("Carga Iva5> ")
        insert(self.impuesto ,aCargar, mes, anho)

        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)


    def imprimir(self,mes,anho):
        '''Simplemente imprime en pantalla los resultados de Iva5 Total y el monto a cargar en el sistema Marangatu'''
        totalImpuestoBD=select_total(self.impuesto, mes, anho)
        print("Iva5TotalBD=", totalImpuestoBD)
        totalACargarBD=totalImpuestoBD*20
        print("A cargar en sistema Iva 5 DB:", totalACargarBD)

    def elimina(self,mes,anho):
        '''Aqui se elimina un valor especifico, se resta del Iva5 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Iva5 a eliminar> ")
        eliminaDB(self.impuesto, aEliminar, mes, anho)
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)


    def imprimir_ultimos(self,mes,anho):
        '''En esta funcion se imprime los ultimos resultados de Iva5 cargado'''
        print("Ultimos numeros cargados iva5", self.ultimosNumeros[0:5])

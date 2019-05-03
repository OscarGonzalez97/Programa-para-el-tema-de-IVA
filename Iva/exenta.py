from impuesto import Impuesto
from funciones_utiles import *

class Exenta (Impuesto):
    impuesto='exenta'
    def carga_dato(self,mes,anho):
        '''Aqui se cargara el dato de Exenta, se agregara a lista de ultimos cargados,
        se sumara al total de Exenta y se calculara lo que hay que cargar en el sistema'''
        #archivoExenta=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasExentas.txt","a")
        aCargar= ingresa_entero("Carga Exenta> ")
        #Funcion que te lleva al insert de la base de datos
        insert(self.impuesto ,aCargar, mes, anho)
        #archivoExenta.write(str(aCargar))
        #archivoExenta.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        #self.totalImpuesto= self.totalImpuesto + aCargar
        #self.cargarMarangatu= self.totalImpuesto
        #archivoExenta.write(str(self.cargarMarangatu))
        #archivoExenta.write("\n")
        #archivoExenta.close()

    def imprimir(self, mes, anho):
        '''Simplemente imprime en pantalla los resultados de Exenta Total y el monto a cargar en el sistema Marangatu'''
        totalImpuestoBD=select_query(self.impuesto, mes, anho)
        #print("ExentaTotal= ", self.totalImpuesto)
        print("ExentaTotalBD=", totalImpuestoBD)
        totalACargarBD=totalImpuestoBD
        print("A cargar en sistema Exenta DB:", totalACargarBD)
        #print("Resultado a cargar en exentas = ", self.cargarMarangatu)

    def elimina(self ,mes, anho):
        '''Aqui se elimina un valor especifico, se resta del Exenta Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Exenta a eliminar> ")
        eliminaDB(self.impuesto, aEliminar, mes, anho)
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        #self.totalImpuesto= self.totalImpuesto - aEliminar
        #self.cargarMarangatu= self.totalImpuesto

    def imprimir_ultimos(self, mes, anho):
        '''En esta funcion se imprime los ultimos resultados Exenta cargado'''
        print("Ultimos numeros cargados exenta", self.ultimosNumeros[0:5])

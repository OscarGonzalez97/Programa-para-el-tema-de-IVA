from impuesto import Impuesto
from funciones_utiles import *

class Iva5 (Impuesto):
    impuesto='iva5'
    def carga_dato(self,mes,anho):
        '''Aqui se cargara el dato del Iva5, se agregara a lista de ultimos cargados,
        se sumara al total de Iva5 y se calculara lo que hay que cargar en el sistema'''
        #archivoIva5=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasIva5.txt","a")
        aCargar= ingresa_entero("Carga Iva5> ")
        #Funcion que te lleva al insert de la base de datos
        insert(self.impuesto ,aCargar, mes, anho)
        #archivoIva5.write(str(aCargar))
        #archivoIva5.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        #self.totalImpuesto= self.totalImpuesto + aCargar
        #self.cargarMarangatu= (self.totalImpuesto*21) - self.totalImpuesto
        #archivoIva5.write(str(self.totalImpuesto))
        #archivoIva5.write("\n")
        #archivoIva5.close()

    def imprimir(self,mes,anho):
        '''Simplemente imprime en pantalla los resultados de Iva5 Total y el monto a cargar en el sistema Marangatu'''
        totalImpuestoBD=select_query(self.impuesto, mes, anho)
        #print("Iva 5 Total= ", self.totalImpuesto)
        print("Iva5TotalBD=", totalImpuestoBD)
        totalACargarBD=totalImpuestoBD*20
        print("A cargar en sistema Iva 5 DB:", totalACargarBD)
        #print("Resultado a cargar Iva 5= ", self.cargarMarangatu)

    def elimina(self,mes,anho):
        '''Aqui se elimina un valor especifico, se resta del Iva5 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Iva5 a eliminar> ")
        eliminaDB(self.impuesto, aEliminar, mes, anho)
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        #self.totalImpuesto= self.totalImpuesto - aEliminar
        #self.cargarMarangatu= (self.totalImpuesto*21) - self.totalImpuesto

    def imprimir_ultimos(self,mes,anho):
        '''En esta funcion se imprime los ultimos resultados de Iva5 cargado'''
        print("Ultimos numeros cargados iva5", self.ultimosNumeros[0:5])

from impuesto import Impuesto
from funciones_utiles import *

class Iva10 (Impuesto):
    impuesto='iva10'
    def carga_dato(self,mes,anho):
        '''Aqui se cargara el dato del Iva10, se agregara a lista de ultimos cargados,
        se sumara al total de Iva10 y se calculara lo que hay que cargar en el sistema'''
        archivoIva10=open("/home/oscarg/Downloads/xfacturas electronicas/abril/FacturasIva10.txt","a")
        aCargar= ingresa_entero("Carga Iva10> ")
        #Funcion que te lleva al insert de la base de datos
        insert(self.impuesto ,aCargar, mes, anho)
        archivoIva10.write(str(aCargar))
        archivoIva10.write("\t")
        if len(self.ultimosNumeros) < 6:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto
        archivoIva10.write(str(self.totalImpuesto))
        archivoIva10.write("\n")
        archivoIva10.close()

    def imprimir(self,mes,anho):
        '''Simplemente imprime en pantalla los resultados de Iva10 Total y el monto a cargar en el sistema Marangatu'''
        totalImpuestoBD=select_query(self.impuesto, mes, anho)
        print("Iva10Total= ", self.totalImpuesto)
        print("Iva10TotalBD=", totalImpuestoBD)
        #Aqui se calcula lo que se va pagar
        totalACargarBD=totalImpuestoBD*10
        print("A cargar en sistema Iva 10:", self.cargarMarangatu)
        print("A cargar en sistema Iva 10 DB:", totalACargarBD)

    def elimina(self,mes,anho):
        '''Aqui se elimina un valor especifico, se resta del Iva10 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= ingresa_entero("Carga Iva 10 a eliminar> ")
        eliminaDB(self.impuesto, aEliminar, mes, anho)
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto

    def imprimir_ultimos(self,mes,anho):
        '''En esta funcion se imprime los ultimos resultados de Iva10 cargado'''
        print("Ultimos numeros cargados", self.ultimosNumeros[0:5])

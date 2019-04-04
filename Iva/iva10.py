from impuesto import Impuesto

class Iva10 (Impuesto):
    def carga_dato(self):
        '''Aqui se cargara el dato del Iva10, se agregara a lista de ultimos cargados,
        se sumara al total de Iva10 y se calculara lo que hay que cargar en el sistema'''
        aCargar= int(input("Carga Iva10> "))
        if len(self.ultimosNumeros) < 5:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto
    def imprimir(self):
        '''Simplemente imprime en pantalla los resultados de Iva10 Total y el monto a cargar en el sistema Marangatu'''
        print("Ultimos numeros cargados", self.ultimosNumeros) #esto no va aca
        print("Iva10Total= ", self.totalImpuesto)
        print("Resultado a cargar = ", self.cargarMarangatu)
    def elimina(self):
        '''Aqui se elimina un valor especifico, se resta del Iva10 Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= int(input("Carga Iva10 a eliminar> "))
        for numeroEliminar in self.ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= (self.totalImpuesto*11) - self.totalImpuesto

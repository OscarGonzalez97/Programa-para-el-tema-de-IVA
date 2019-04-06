from impuesto import Impuesto

class Exenta (Impuesto):
    def carga_dato(self):
        '''Aqui se cargara el dato de Exenta, se agregara a lista de ultimos cargados,
        se sumara al total de Exenta y se calculara lo que hay que cargar en el sistema'''
        archivoExenta=open("/home/oscarg/Downloads/xfacturas electronicas/marzo/FacturasExentas.txt","a")
        aCargar= int(input("Carga Exenta> "))
        archivoExenta.write(str(aCargar))
        archivoExenta.write("\t")
        if len(self.ultimosNumeros) < 5:
            self.ultimosNumeros.append(aCargar)
        self.totalImpuesto= self.totalImpuesto + aCargar
        self.cargarMarangatu= self.totalImpuesto
        archivoExenta.write(str(self.cargarMarangatu))
        archivoIva10.write("\n")
        archivoExenta.close()

    def imprimir(self):
        '''Simplemente imprime en pantalla los resultados de Exenta Total y el monto a cargar en el sistema Marangatu'''
        print("Ultimos numeros cargados", self.ultimosNumeros) #esto no va aca
        print("ExentaTotal= ", self.totalImpuesto)
        print("Resultado a cargar = ", self.cargarMarangatu)

    def elimina(self):
        '''Aqui se elimina un valor especifico, se resta del Exenta Total, se borra de la lista de ultimos cargados (si esta ahi)
        y se modifica el monto a cargar en Marangatu'''
        aEliminar= int(input("Carga Exenta a eliminar> "))
        for numeroEliminar in ultimosNumeros:
            if(numeroEliminar==aEliminar):
                self.ultimosNumeros.remove(aEliminar)
        self.totalImpuesto= self.totalImpuesto - aEliminar
        self.cargarMarangatu= self.totalImpuesto

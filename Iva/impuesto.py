from funciones_utiles import *

class Impuesto():

    def __init__(self):
        #Aqui estaran los ultimos 5 numeros cargados (pueden ser mas)
        self.ultimosNumeros=[]
        #Este sera la suma de los IVA y con este se calculara la variable de abajo
        self.totalImpuesto=0
        #Esto va ser lo que al final se va cargar en el sistema Marangatu
        self.cargarMarangatu=0

    def muestra_mes(self, mes, anho):
        '''Se mostrara los resultados de todo el mes'''
        select_mes(self.impuesto, mes, anho)

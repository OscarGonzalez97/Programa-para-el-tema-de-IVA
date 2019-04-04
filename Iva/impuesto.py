class Impuesto():

    def __init__(self):
        #Aqui estaran los ultimos 5 numeros cargados (pueden ser mas)
        self.ultimosNumeros=[]
        #Este sera la suma de los IVA y con este se calculara la variable de abajo
        self.totalImpuesto=0
        #Esto va ser lo que al final se va cargar en el sistema Marangatu
        self.cargarMarangatu=0

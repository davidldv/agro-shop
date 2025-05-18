from model.producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion

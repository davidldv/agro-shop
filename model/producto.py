from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def obtener_info(self):
        pass

# Define el contrato que todas las subclases deben implementar: obtener_info()
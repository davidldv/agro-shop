from model.producto_control import ProductoControl
from datetime import date

class Fertilizante(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion  # str o date

    def obtener_info(self):
        return {
            "tipo": "Fertilizante",
            "nombre": self.nombre,
            "precio": self.precio,
            "registro_ica": self.registro_ica,
            "frecuencia": self.frecuencia_aplicacion,
            "ultima_aplicacion": self.fecha_ultima_aplicacion
        }

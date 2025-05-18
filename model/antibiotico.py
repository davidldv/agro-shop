from model.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre, precio, dosis, tipo_animal):
        super().__init__(nombre, precio)
        self.dosis = dosis  # valor entre 400 y 600
        self.tipo_animal = tipo_animal  # bovino, caprino o porcino

    def obtener_info(self):
        return {
            "tipo": "Antibiótico",
            "nombre": self.nombre,
            "precio": self.precio,
            "dosis": self.dosis,
            "tipo_animal": self.tipo_animal
        }

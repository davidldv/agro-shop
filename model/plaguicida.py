from model.producto_control import ProductoControl

class Plaguicida(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia  # en días

    def obtener_info(self):
        return {
            "tipo": "Plaguicida",
            "nombre": self.nombre,
            "precio": self.precio,
            "registro_ica": self.registro_ica,
            "frecuencia": self.frecuencia_aplicacion,
            "periodo_carencia": self.periodo_carencia
        }

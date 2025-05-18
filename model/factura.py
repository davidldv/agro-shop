from datetime import datetime

class Factura:
    def __init__(self, productos):
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.productos = productos
        self.valor_total = sum(p.precio for p in productos)

    def obtener_resumen(self):
        return {
            "fecha": self.fecha,
            "valor_total": self.valor_total,
            "productos": [p.obtener_info() for p in self.productos]
        }

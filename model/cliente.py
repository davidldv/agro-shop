class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = [] 

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def obtener_facturas(self):
        return self.facturas

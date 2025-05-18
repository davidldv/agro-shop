import json
import os
from model.cliente import Cliente
from model.factura import Factura
from model.fertilizante import Fertilizante
from model.plaguicida import Plaguicida
from model.antibiotico import Antibiotico

class TiendaAgroController:
    def __init__(self, data_file="data/datos.json"):
        self.clientes = []
        self.data_file = data_file
        self._cargar_datos()

    # ----------------------------------------
    def registrar_cliente(self, nombre, cedula):
        if not self._buscar_cliente(cedula):
            cliente = Cliente(nombre, cedula)
            self.clientes.append(cliente)
            self._guardar_datos()
            return True
        return False

    def agregar_factura_a_cliente(self, cedula, productos):
        cliente = self._buscar_cliente(cedula)
        if cliente:
            factura = Factura(productos)
            cliente.agregar_factura(factura)
            self._guardar_datos()
            return factura
        return None

    def buscar_por_cedula(self, cedula):
        cliente = self._buscar_cliente(cedula)
        if cliente:
            return [f.obtener_resumen() for f in cliente.obtener_facturas()]
        return []

    # ----------------------------------------
    def crear_producto(self, tipo, **kwargs):
        if tipo == "fertilizante":
            return Fertilizante(**kwargs)
        elif tipo == "plaguicida":
            return Plaguicida(**kwargs)
        elif tipo == "antibiotico":
            return Antibiotico(**kwargs)
        else:
            raise ValueError("Tipo de producto no válido")

    # ----------------------------------------
    def _buscar_cliente(self, cedula):
        return next((c for c in self.clientes if c.cedula == cedula), None)

    # ----------------------------------------
    def _guardar_datos(self):
        data = []
        for cliente in self.clientes:
            data.append({
                "nombre": cliente.nombre,
                "cedula": cliente.cedula,
                "facturas": [
                    {
                        "fecha": f.fecha,
                        "valor_total": f.valor_total,
                        "productos": [p.obtener_info() for p in f.productos]
                    }
                    for f in cliente.facturas
                ]
            })

        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def _cargar_datos(self):
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, 'r') as f:
                contenido = f.read().strip()
                if not contenido:
                    return
                data = json.loads(contenido)
                for c_data in data:
                    cliente = Cliente(c_data["nombre"], c_data["cedula"])
                    for f_data in c_data["facturas"]:
                        productos = []
                        for p in f_data["productos"]:
                            tipo = p["tipo"].lower()
                            if tipo == "fertilizante":
                                prod = Fertilizante(
                                    nombre=p["nombre"],
                                    precio=p["precio"],
                                    registro_ica=p["registro_ica"],
                                    frecuencia_aplicacion=p["frecuencia"],
                                    fecha_ultima_aplicacion=p["ultima_aplicacion"]
                                )
                            elif tipo == "plaguicida":
                                prod = Plaguicida(
                                    nombre=p["nombre"],
                                    precio=p["precio"],
                                    registro_ica=p["registro_ica"],
                                    frecuencia_aplicacion=p["frecuencia"],
                                    periodo_carencia=p["periodo_carencia"]
                                )
                            elif tipo == "antibiótico":
                                prod = Antibiotico(
                                    nombre=p["nombre"],
                                    precio=p["precio"],
                                    dosis=p["dosis"],
                                    tipo_animal=p["tipo_animal"]
                                )
                            else:
                                continue
                            productos.append(prod)
                        factura = Factura(productos)
                        factura.fecha = f_data["fecha"]
                        cliente.agregar_factura(factura)
                    self.clientes.append(cliente)
        except Exception as e:
            print(f"[ERROR al cargar datos]: {e}")

import unittest
from model.cliente import Cliente
from model.fertilizante import Fertilizante
from model.plaguicida import Plaguicida
from model.antibiotico import Antibiotico
from model.factura import Factura
from controller.controller import TiendaAgroController

class TestModelo(unittest.TestCase):

    def test_crear_cliente(self):
        cliente = Cliente("Juan", "123")
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.cedula, "123")
        self.assertEqual(cliente.facturas, [])

    def test_crear_fertilizante(self):
        fert = Fertilizante("NPK", 10000, "ICA123", "15 días", "2024-05-01")
        info = fert.obtener_info()
        self.assertEqual(info["tipo"], "Fertilizante")
        self.assertEqual(info["nombre"], "NPK")

    def test_crear_plaguicida(self):
        plag = Plaguicida("Insecticida X", 8000, "ICA456", "30 días", 15)
        self.assertEqual(plag.periodo_carencia, 15)

    def test_crear_antibiotico(self):
        anti = Antibiotico("Penicilina", 5000, 450, "bovino")
        self.assertEqual(anti.tipo_animal, "bovino")

    def test_factura_valor_total(self):
        a = Antibiotico("Med A", 5000, 500, "porcino")
        f = Fertilizante("Fert A", 7000, "ICA789", "20 días", "2024-04-01")
        factura = Factura([a, f])
        self.assertEqual(factura.valor_total, 12000)

    def test_registro_y_busqueda_en_controller(self):
        ctrl = TiendaAgroController(data_file="data/test_datos.json")  # Evitar tocar datos reales
        ctrl.clientes = []  # Limpiar lista para pruebas

        ctrl.registrar_cliente("Ana", "321")
        fert = Fertilizante("FertB", 10000, "ICA000", "Cada mes", "2024-03-01")
        factura = ctrl.agregar_factura_a_cliente("321", [fert])
        self.assertIsNotNone(factura)
        facturas = ctrl.buscar_por_cedula("321")
        self.assertEqual(len(facturas), 1)
        self.assertEqual(facturas[0]["valor_total"], 10000)

if __name__ == "__main__":
    unittest.main()

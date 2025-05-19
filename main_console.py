from controller.controller import TiendaAgroController

def main():
    ctrl = TiendaAgroController()

    while True:
        print("\nTIENDA AGRÍCOLA 🛒")
        print("1. Registrar cliente")
        print("2. Crear factura")
        print("3. Buscar facturas por cédula")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            cedula = input("Cédula del cliente: ")
            if ctrl.registrar_cliente(nombre, cedula):
                print("Cliente registrado.")
            else:
                print("El cliente ya existe.")

        elif opcion == "2":
            cedula = input("Cédula del cliente: ")
            productos = []

            while True:
                print("\nAgregar producto a la factura")
                print("a. Fertilizante")
                print("b. Plaguicida")
                print("c. Antibiótico")
                print("x. Finalizar factura")
                tipo = input("Tipo de producto: ")

                if tipo == "a":
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    registro_ica = input("Registro ICA: ")
                    frecuencia = input("Frecuencia de aplicación: ")
                    ultima_aplicacion = input("Fecha última aplicación: ")
                    p = ctrl.crear_producto(
                        "fertilizante",
                        nombre=nombre,
                        precio=precio,
                        registro_ica=registro_ica,
                        frecuencia_aplicacion=frecuencia,
                        fecha_ultima_aplicacion=ultima_aplicacion
                    )
                    productos.append(p)

                elif tipo == "b":
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    registro_ica = input("Registro ICA: ")
                    frecuencia = input("Frecuencia de aplicación: ")
                    carencia = int(input("Periodo de carencia (días): "))
                    p = ctrl.crear_producto(
                        "plaguicida",
                        nombre=nombre,
                        precio=precio,
                        registro_ica=registro_ica,
                        frecuencia_aplicacion=frecuencia,
                        periodo_carencia=carencia
                    )
                    productos.append(p)

                elif tipo == "c":
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    dosis = int(input("Dosis (400-600Kg): "))
                    animal = input("Tipo de animal (bovino, caprino, porcino): ")
                    p = ctrl.crear_producto(
                        "antibiotico",
                        nombre=nombre,
                        precio=precio,
                        dosis=dosis,
                        tipo_animal=animal
                    )
                    productos.append(p)

                elif tipo == "x":
                    break

            if productos:
                factura = ctrl.agregar_factura_a_cliente(cedula, productos)
                if factura:
                    print("Factura registrada con éxito.")
                    print(f"Total: ${factura.valor_total} Fecha: {factura.fecha}")
                else:
                    print("Cliente no encontrado.")

        elif opcion == "3":
            cedula = input("Cédula del cliente: ")
            facturas = ctrl.buscar_por_cedula(cedula)
            if not facturas:
                print("No se encontraron facturas.")
            else:
                for i, f in enumerate(facturas, start=1):
                    print(f"\nFactura #{i} - Fecha: {f['fecha']} - Total: ${f['valor_total']}")
                    for prod in f["productos"]:
                        print(" -", prod)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

import tkinter as tk
from view.ui_cliente import ClienteForm
from view.ui_factura import FacturaForm
from view.ui_consulta import ConsultaForm
from controller.controller import TiendaAgroController

def iniciar_gui():
    controller = TiendaAgroController()

    root = tk.Tk()
    root.title("Tienda Agrícola - Sistema de Facturación")
    root.geometry("400x250")

    tk.Label(root, text="Menú Principal", font=("Helvetica", 16)).pack(pady=10)

    tk.Button(root, text="Registrar Cliente", width=30,
              command=lambda: ClienteForm(root, controller)).pack(pady=5)

    tk.Button(root, text="Crear Factura", width=30,
              command=lambda: FacturaForm(root, controller)).pack(pady=5)

    tk.Button(root, text="Buscar Facturas por Cédula", width=30,
              command=lambda: ConsultaForm(root, controller)).pack(pady=5)

    tk.Button(root, text="Salir", width=30, command=root.destroy).pack(pady=15)

    root.mainloop()

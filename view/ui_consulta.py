import tkinter as tk
from tkinter import ttk, messagebox

class ConsultaForm(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.title("Consultar Facturas por Cédula")
        self.geometry("700x500")
        self.controller = controller

        # Entrada de cédula
        tk.Label(self, text="Cédula del Cliente:").pack(pady=5)
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.pack()

        tk.Button(self, text="Buscar", command=self.buscar_facturas).pack(pady=10)

        # Tabla de facturas
        self.tree_facturas = ttk.Treeview(self, columns=("Fecha", "Total"), show="headings", height=5)
        self.tree_facturas.heading("Fecha", text="Fecha")
        self.tree_facturas.heading("Total", text="Valor Total")
        self.tree_facturas.pack(pady=10, fill="x")

        # Tabla de productos de la factura seleccionada
        self.tree_productos = ttk.Treeview(self, columns=("Tipo", "Nombre", "Precio"), show="headings", height=8)
        for col in ("Tipo", "Nombre", "Precio"):
            self.tree_productos.heading(col, text=col)
        self.tree_productos.pack(pady=10, fill="x")

        self.tree_facturas.bind("<<TreeviewSelect>>", self.mostrar_detalle)

        self.facturas_encontradas = []

    def buscar_facturas(self):
        cedula = self.entry_cedula.get()
        self.tree_facturas.delete(*self.tree_facturas.get_children())
        self.tree_productos.delete(*self.tree_productos.get_children())

        facturas = self.controller.buscar_por_cedula(cedula)
        if not facturas:
            messagebox.showinfo("Sin resultados", "No se encontraron facturas para esa cédula.")
            return

        self.facturas_encontradas = facturas
        for i, f in enumerate(facturas):
            self.tree_facturas.insert("", "end", iid=i, values=(f["fecha"], f["valor_total"]))

    def mostrar_detalle(self, event):
        selected = self.tree_facturas.focus()
        if not selected:
            return

        self.tree_productos.delete(*self.tree_productos.get_children())
        index = int(selected)
        productos = self.facturas_encontradas[index]["productos"]

        for p in productos:
            self.tree_productos.insert("", "end", values=(p["tipo"], p["nombre"], p["precio"]))

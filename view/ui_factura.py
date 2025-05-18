import tkinter as tk
from tkinter import ttk, messagebox

class FacturaForm(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.title("Crear Factura")
        self.geometry("600x500")
        self.controller = controller
        self.productos = []

        # Cédula del cliente
        tk.Label(self, text="Cédula del Cliente:").pack(pady=5)
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.pack()

        # Selección de tipo de producto
        tk.Label(self, text="Tipo de Producto:").pack(pady=5)
        self.tipo_var = tk.StringVar()
        tipo_menu = ttk.Combobox(self, textvariable=self.tipo_var, state="readonly")
        tipo_menu["values"] = ["Fertilizante", "Plaguicida", "Antibiótico"]
        tipo_menu.pack()
        tipo_menu.bind("<<ComboboxSelected>>", self.mostrar_formulario)

        # Marco donde se insertará el formulario dinámico
        self.formulario_frame = tk.Frame(self)
        self.formulario_frame.pack(pady=10, fill="both", expand=True)

        # Tabla para productos añadidos
        self.tree = ttk.Treeview(self, columns=("Tipo", "Nombre", "Precio"), show='headings', height=5)
        for col in ("Tipo", "Nombre", "Precio"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        # Botón para registrar factura
        tk.Button(self, text="Registrar Factura", command=self.registrar_factura).pack(pady=10)

    def mostrar_formulario(self, event=None):
        for widget in self.formulario_frame.winfo_children():
            widget.destroy()

        tipo = self.tipo_var.get()
        campos = []

        if tipo == "Fertilizante":
            campos = ["Nombre", "Precio", "Registro ICA", "Frecuencia", "Fecha Última Aplicación"]
        elif tipo == "Plaguicida":
            campos = ["Nombre", "Precio", "Registro ICA", "Frecuencia", "Periodo Carencia"]
        elif tipo == "Antibiótico":
            campos = ["Nombre", "Precio", "Dosis", "Tipo de Animal"]

        self.entradas = {}
        for campo in campos:
            tk.Label(self.formulario_frame, text=campo + ":").pack()
            entry = tk.Entry(self.formulario_frame)
            entry.pack()
            self.entradas[campo] = entry

        tk.Button(self.formulario_frame, text="Agregar Producto", command=self.agregar_producto).pack(pady=10)

    def agregar_producto(self):
        tipo = self.tipo_var.get().lower()
        try:
            if tipo == "fertilizante":
                prod = self.controller.crear_producto(
                    "fertilizante",
                    nombre=self.entradas["Nombre"].get(),
                    precio=float(self.entradas["Precio"].get()),
                    registro_ica=self.entradas["Registro ICA"].get(),
                    frecuencia_aplicacion=self.entradas["Frecuencia"].get(),
                    fecha_ultima_aplicacion=self.entradas["Fecha Última Aplicación"].get()
                )
            elif tipo == "plaguicida":
                prod = self.controller.crear_producto(
                    "plaguicida",
                    nombre=self.entradas["Nombre"].get(),
                    precio=float(self.entradas["Precio"].get()),
                    registro_ica=self.entradas["Registro ICA"].get(),
                    frecuencia_aplicacion=self.entradas["Frecuencia"].get(),
                    periodo_carencia=int(self.entradas["Periodo Carencia"].get())
                )
            elif tipo == "antibiotico":
                prod = self.controller.crear_producto(
                    "antibiotico",
                    nombre=self.entradas["Nombre"].get(),
                    precio=float(self.entradas["Precio"].get()),
                    dosis=int(self.entradas["Dosis"].get()),
                    tipo_animal=self.entradas["Tipo de Animal"].get()
                )
            else:
                raise ValueError("Tipo no válido")

            self.productos.append(prod)
            self.tree.insert("", "end", values=(tipo.capitalize(), prod.nombre, prod.precio))
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def registrar_factura(self):
        cedula = self.entry_cedula.get()
        if not cedula or not self.productos:
            messagebox.showwarning("Faltan datos", "Debes ingresar la cédula y al menos un producto.")
            return

        factura = self.controller.agregar_factura_a_cliente(cedula, self.productos)
        if factura:
            messagebox.showinfo("Éxito", f"Factura registrada. Total: ${factura.valor_total}")
            self.destroy()
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

import tkinter as tk
from tkinter import messagebox

class ClienteForm(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.title("Registrar Cliente")
        self.geometry("300x200")
        self.controller = controller

        tk.Label(self, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Cédula:").pack(pady=5)
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.pack()

        tk.Button(self, text="Registrar", command=self.registrar).pack(pady=15)

    def registrar(self):
        nombre = self.entry_nombre.get()
        cedula = self.entry_cedula.get()
        if nombre and cedula:
            if self.controller.registrar_cliente(nombre, cedula):
                messagebox.showinfo("Éxito", "Cliente registrado.")
                self.destroy()
            else:
                messagebox.showwarning("Duplicado", "El cliente ya existe.")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

import tkinter as tk
from tkinter import messagebox

# Colores (mismos de lab7.1): verde, negro y oro
NEGRO = "#0A0A0A"
VERDE = "#0B6B2E"
VERDE_CLARO = "#1FA855"
ORO = "#D4AF37"
CAMPO = "#161616"


class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        # PERSONALIZAR 1 (hecho): título de la ventana
        self.ventana.title("Registro de usuarios - Tienda de Videojuegos")
        # PERSONALIZAR 2 (hecho): dimensiones
        self.ventana.geometry("420x460")
        # PERSONALIZAR 3 (hecho): color de fondo
        self.ventana.configure(bg=NEGRO)
        self.ventana.resizable(False, False)

        # Mantiene la ventana asociada a la principal.
        self.ventana.transient(root)
        self.ventana.grab_set()

        # PERSONALIZAR 4 (hecho): título
        self.titulo = tk.Label(
            self.ventana, text="CREAR CUENTA", font=("Arial", 19, "bold"),
            bg=NEGRO, fg=ORO
        )
        self.titulo.pack(pady=18)

        # PERSONALIZAR 5 (hecho): etiquetas
        self.lbl_nombre = tk.Label(
            self.ventana, text="Nombre completo:", bg=NEGRO, fg=ORO, font=("Arial", 10)
        )
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(
            self.ventana, width=35, font=("Arial", 10), bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana, text="Correo electrónico:", bg=NEGRO, fg=ORO, font=("Arial", 10)
        )
        self.lbl_email.pack()
        self.entry_email = tk.Entry(
            self.ventana, width=35, font=("Arial", 10), bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana, text="Contraseña:", bg=NEGRO, fg=ORO, font=("Arial", 10)
        )
        self.lbl_password.pack()
        self.entry_password = tk.Entry(
            self.ventana, width=35, show="*", font=("Arial", 10), bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana, text="Confirmar contraseña:", bg=NEGRO, fg=ORO, font=("Arial", 10)
        )
        self.lbl_confirmar.pack()
        self.entry_confirmar = tk.Entry(
            self.ventana, width=35, show="*", font=("Arial", 10), bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_confirmar.pack(pady=4)

        # PERSONALIZAR 6 (hecho): botón de registro
        self.btn_guardar = tk.Button(
            self.ventana, text="Registrar usuario", width=22, bg=VERDE,
            fg=ORO, font=("Arial", 10, "bold"), cursor="hand2", relief="flat",
            activebackground=VERDE_CLARO, activeforeground=NEGRO,
            highlightthickness=2, highlightbackground=ORO
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana, text="Cancelar", width=22, command=self.cerrar, cursor="hand2", bg=NEGRO, fg=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()
        confirmar = self.entry_confirmar.get().strip()
        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()

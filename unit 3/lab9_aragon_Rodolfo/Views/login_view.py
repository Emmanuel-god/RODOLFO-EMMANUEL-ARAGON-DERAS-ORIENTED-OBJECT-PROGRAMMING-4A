import tkinter as tk
from tkinter import messagebox

NEGRO = "#0A0A0A"
VERDE = "#0B6B2E"
VERDE_CLARO = "#1FA855"
ORO = "#D4AF37"
CAMPO = "#161616"


class LoginView:

    def __init__(self, root):
        self.root = root
        # PERSONALIZAR 1 (hecho): título de la ventana
        self.root.title("Acceso al Sistema - Tienda de Videojuegos")
        # PERSONALIZAR 2 (hecho): tamaño de la ventana
        self.root.geometry("420x380")
        # PERSONALIZAR 3 (hecho): color de fondo
        self.root.configure(bg=NEGRO)
        self.root.resizable(False, False)

        # PERSONALIZAR 4 (hecho): título
        self.titulo = tk.Label(
            root, text="INICIAR SESIÓN", font=("Arial", 20, "bold"),
            bg=NEGRO, fg=ORO
        )
        self.titulo.pack(pady=20)

        # PERSONALIZAR 5 (hecho): etiquetas
        self.lbl_email = tk.Label(
            root, text="Correo electrónico:", font=("Arial", 11), bg=NEGRO, fg=ORO
        )
        self.lbl_email.pack()

        # PERSONALIZAR 6 (hecho): campos de texto
        self.entry_email = tk.Entry(
            root, width=35, font=("Arial", 11), bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root, text="Contraseña:", font=("Arial", 11), bg=NEGRO, fg=ORO
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root, width=35, font=("Arial", 11), show="*", bg=CAMPO, fg=ORO, insertbackground=ORO,
            relief="flat", highlightthickness=2, highlightbackground=VERDE, highlightcolor=ORO
        )
        self.entry_password.pack(pady=5)

        # PERSONALIZAR 7 (hecho): botón de ingreso
        self.btn_login = tk.Button(
            root, text="Entrar", width=20, bg=VERDE, fg=ORO,
            font=("Arial", 11, "bold"), cursor="hand2", relief="flat",
            activebackground=VERDE_CLARO, activeforeground=NEGRO,
            highlightthickness=2, highlightbackground=ORO
        )
        self.btn_login.pack(pady=15)

        # PERSONALIZAR 8 (hecho): botón para abrir el registro
        self.btn_register = tk.Button(
            root, text="Crear cuenta", width=20, bg=NEGRO, fg=ORO,
            font=("Arial", 10), cursor="hand2", relief="flat",
            activebackground=NEGRO, activeforeground=VERDE_CLARO,
            highlightthickness=2, highlightbackground=VERDE
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()
        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)

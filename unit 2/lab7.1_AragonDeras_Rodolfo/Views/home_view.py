import tkinter as tk

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("400x250")
        self.root.configure(bg="#0A0A0A")

        lbl_mensaje = tk.Label(
            self.root, 
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}", 
            font=("Helvetica", 12),
            bg="#0A0A0A",
            fg="#D4AF37",
            justify="center"
        )
        lbl_mensaje.pack(expand=True)
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

NEGRO = "#0A0A0A"
VERDE = "#0B6B2E"
VERDE_CLARO = "#1FA855"
ORO = "#D4AF37"
CAMPO = "#161616"

FORMATOS = ("CSV", "TXT", "JSON", "PDF")
EXTENSIONES = {
    "CSV": ("Archivo CSV", "*.csv"),
    "TXT": ("Archivo de texto", "*.txt"),
    "JSON": ("Archivo JSON", "*.json"),
    "PDF": ("Documento PDF", "*.pdf"),
}


class InventoryView:
    """Panel de inventario con el área de controles para exportar el reporte."""

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Inventario - Tienda de Videojuegos")
        self.ventana.geometry("720x460")
        self.ventana.configure(bg=NEGRO)
        self.ventana.transient(root)

        self.titulo = tk.Label(
            self.ventana, text="INVENTARIO DE PRODUCTOS", font=("Arial", 18, "bold"),
            bg=NEGRO, fg=ORO
        )
        self.titulo.pack(pady=12)

        # ---- Tabla de productos ----
        estilo = ttk.Style(self.ventana)
        estilo.theme_use("clam")
        estilo.configure(
            "Treeview", background=CAMPO, fieldbackground=CAMPO, foreground=ORO,
            rowheight=24, bordercolor=VERDE
        )
        estilo.configure("Treeview.Heading", background=VERDE, foreground=ORO,
                         font=("Arial", 10, "bold"))
        estilo.map("Treeview", background=[("selected", VERDE)])
        estilo.configure(
            "TCombobox", fieldbackground=CAMPO, background=VERDE, foreground=ORO,
            arrowcolor=ORO
        )

        columnas = ("id", "nombre", "categoria", "precio", "stock")
        self.tabla = ttk.Treeview(
            self.ventana, columns=columnas, show="headings", height=11
        )
        anchos = {"id": 50, "nombre": 310, "categoria": 110, "precio": 90, "stock": 70}
        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, width=anchos[col], anchor="w")
        self.tabla.pack(padx=15, fill="x")

        # ---- Área de controles (Paso 1) ----
        self.marco_controles = tk.Frame(self.ventana, bg=NEGRO)
        self.marco_controles.pack(pady=15)

        self.lbl_formato = tk.Label(
            self.marco_controles, text="Formato:", font=("Arial", 11), bg=NEGRO, fg=ORO
        )
        self.lbl_formato.grid(row=0, column=0, padx=6)

        # Combobox de solo lectura con los formatos de exportación.
        self.combo_formato = ttk.Combobox(
            self.marco_controles, values=FORMATOS, state="readonly", width=10,
            font=("Arial", 11)
        )
        self.combo_formato.current(0)
        self.combo_formato.grid(row=0, column=1, padx=6)

        # Botón que el Controlador vincula a generar_reporte().
        self.btn_exportar = tk.Button(
            self.marco_controles, text="Exportar Reporte", width=20, bg=VERDE, fg=ORO,
            font=("Arial", 11, "bold"), cursor="hand2", relief="flat",
            activebackground=VERDE_CLARO, activeforeground=NEGRO,
            highlightthickness=2, highlightbackground=ORO
        )
        self.btn_exportar.grid(row=0, column=2, padx=12)

    # ---------- Datos ----------
    def obtener_formato(self):
        return self.combo_formato.get()

    def mostrar_productos(self, productos):
        self.tabla.delete(*self.tabla.get_children())
        for p in productos:
            self.tabla.insert(
                "", tk.END,
                values=(p["id"], p["nombre"], p["categoria"], f"${p['precio']:,.2f}", p["stock"])
            )

    # ---------- Diálogos ----------
    def pedir_ruta_guardado(self, formato):
        descripcion, patron = EXTENSIONES[formato]
        return filedialog.asksaveasfilename(
            parent=self.ventana,
            title="Guardar reporte",
            initialfile="reporte_productos",
            defaultextension=patron.lstrip("*"),
            filetypes=[(descripcion, patron)],
        )

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()

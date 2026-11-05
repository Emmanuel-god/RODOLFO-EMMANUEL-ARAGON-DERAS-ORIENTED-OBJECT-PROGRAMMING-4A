from Models.product_model import Product
from exportadores import ExportadorCSV, ExportadorTXT, ExportadorJSON, ExportadorPDF

# Cada formato de la Vista se asocia a su clase hija (solo se instancia la elegida).
EXPORTADORES = {
    "CSV": ExportadorCSV,
    "TXT": ExportadorTXT,
    "JSON": ExportadorJSON,
    "PDF": ExportadorPDF,
}


class InventarioController:

    def __init__(self, vista):
        self.vista = vista
        self.modelo = Product()

        # El botón entrega al método el formato seleccionado en el Combobox.
        self.vista.btn_exportar.config(
            command=lambda: self.generar_reporte(self.vista.obtener_formato())
        )
        self.cargar_productos()

    def cargar_productos(self):
        productos = self.modelo.listar()
        if productos is None:
            self.vista.mostrar_mensaje(
                "Error", "No fue posible consultar los productos. "
                "Verifica la conexión con PostgreSQL y que exista la tabla products.", "error"
            )
            return
        self.vista.mostrar_productos(productos)

    def generar_reporte(self, formato):
        # 1) Datos actuales desde el Modelo.
        productos = self.modelo.listar()
        if productos is None:
            self.vista.mostrar_mensaje(
                "Error", "No fue posible consultar los productos.", "error"
            )
            return
        if not productos:
            self.vista.mostrar_mensaje(
                "Sin datos", "No hay productos para exportar.", "error"
            )
            return

        clase_exportador = EXPORTADORES.get(formato)
        if clase_exportador is None:
            self.vista.mostrar_mensaje(
                "Formato inválido", f"Formato no soportado: {formato}", "error"
            )
            return

        ruta = self.vista.pedir_ruta_guardado(formato)
        if not ruta:  # el usuario canceló el diálogo
            return

        # 2) Polimorfismo: se instancia solo la clase hija y se invoca exportar().
        exportador = clase_exportador()
        try:
            exportador.exportar(productos, ruta)
        except (OSError, RuntimeError) as error:
            self.vista.mostrar_mensaje(
                "Error al exportar", f"No se pudo generar el reporte:\n{error}", "error"
            )
            return

        self.vista.mostrar_mensaje(
            "Reporte generado", f"El reporte {formato} se guardó en:\n{ruta}"
        )

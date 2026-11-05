"""Módulo de exportación (Lab 9) - lógica orientada a objetos.

Exportador es una "interfaz" (clase abstracta); cada formato es una clase hija
que sobrescribe exportar(). El Controlador solo conoce el método exportar(),
no el formato: el polimorfismo decide cómo se escribe el archivo.
"""
import csv
import json
from abc import ABC, abstractmethod
from datetime import date, datetime
from decimal import Decimal


def _a_texto(valor):
    """Convierte cualquier valor de la BD a texto legible (None -> vacío)."""
    return "" if valor is None else str(valor)


def _a_json(valor):
    """Serializa tipos que json no conoce (Decimal, fechas)."""
    if isinstance(valor, Decimal):
        return float(valor)
    if isinstance(valor, (date, datetime)):
        return valor.isoformat()
    return str(valor)


def _normalizar(datos):
    """Devuelve (encabezados, filas) a partir de una lista de dicts o de tuplas."""
    datos = list(datos)
    if not datos:
        return [], []
    if isinstance(datos[0], dict):
        encabezados = list(datos[0].keys())
        filas = [[fila.get(h) for h in encabezados] for fila in datos]
    else:
        encabezados = [f"col{i + 1}" for i in range(len(datos[0]))]
        filas = [list(fila) for fila in datos]
    return encabezados, filas


class Exportador(ABC):
    """Interfaz base: todo exportador debe implementar exportar()."""

    @abstractmethod
    def exportar(self, datos, ruta_archivo):
        raise NotImplementedError(
            f"{self.__class__.__name__} debe sobrescribir el método exportar()."
        )


class ExportadorCSV(Exportador):
    """Usa la librería nativa csv."""

    def exportar(self, datos, ruta_archivo):
        encabezados, filas = _normalizar(datos)
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo)
            if encabezados:
                escritor.writerow(encabezados)
            for fila in filas:
                escritor.writerow([_a_texto(v) for v in fila])


class ExportadorTXT(Exportador):
    """Usa open() para escribir líneas simples."""

    def exportar(self, datos, ruta_archivo):
        encabezados, filas = _normalizar(datos)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            if encabezados:
                archivo.write(" | ".join(encabezados) + "\n")
                archivo.write("-" * 60 + "\n")
            for fila in filas:
                archivo.write(" | ".join(_a_texto(v) for v in fila) + "\n")


class ExportadorJSON(Exportador):
    """Usa la librería nativa json."""

    def exportar(self, datos, ruta_archivo):
        encabezados, filas = _normalizar(datos)
        registros = [dict(zip(encabezados, fila)) for fila in filas]
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(registros, archivo, ensure_ascii=False, indent=4, default=_a_json)


class ExportadorPDF(Exportador):
    """Usa la librería de terceros fpdf (pip install fpdf2)."""

    def exportar(self, datos, ruta_archivo):
        try:
            from fpdf import FPDF
        except ImportError as error:
            raise RuntimeError(
                "Falta la librería fpdf. Instálala con: pip install fpdf2"
            ) from error

        encabezados, filas = _normalizar(datos)

        def limpio(valor):
            # Las fuentes base de fpdf solo admiten latin-1.
            return _a_texto(valor).encode("latin-1", "replace").decode("latin-1")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Reporte de productos", align="C")
        pdf.ln(12)

        if not encabezados:
            pdf.set_font("Helvetica", "", 11)
            pdf.cell(0, 8, "Sin registros.")
        else:
            ancho = 190 / len(encabezados)
            pdf.set_font("Helvetica", "B", 10)
            for encabezado in encabezados:
                pdf.cell(ancho, 8, limpio(encabezado), border=1, align="C")
            pdf.ln()
            pdf.set_font("Helvetica", "", 10)
            for fila in filas:
                for valor in fila:
                    pdf.cell(ancho, 8, limpio(valor)[:25], border=1)
                pdf.ln()

        pdf.output(ruta_archivo)

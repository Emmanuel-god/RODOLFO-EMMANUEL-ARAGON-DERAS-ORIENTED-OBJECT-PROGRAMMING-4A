from tkinter import *
from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractmethod
from datetime import datetime
import os


# =========================
# SUPERCLASE
# =========================
class SmartDevice(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    # NUEVO: segundo comportamiento polimorfico
    @abstractmethod
    def turn_off(self):
        pass


# =========================
# CLASES HIJAS
# =========================
class SmartLight(SmartDevice):

    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
        return f"{self.name} set brightness to 100%"

    def turn_off(self):
        return f"{self.name} set brightness to 0%"


class SmartSpeaker(SmartDevice):

    def __init__(self):
        super().__init__("Google Speaker")

    def turn_on(self):
        return f"{self.name} playing my music"

    def turn_off(self):
        return f"{self.name} music stopped"


class SmartFan(SmartDevice):

    def __init__(self):
        super().__init__("Smart Fan")

    def turn_on(self):
        return f"{self.name} set temperature to 35°C"

    def turn_off(self):
        return f"{self.name} stopped spinning"


# NUEVO: dispositivo extra para probar escalabilidad
class SmartThermostat(SmartDevice):

    def __init__(self):
        super().__init__("Smart Thermostat")

    def turn_on(self):
        return f"{self.name} heating to 22°C"

    def turn_off(self):
        return f"{self.name} climate control off"


# =========================
# GUI
# =========================
class SmartHomeApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Lab 6. Smart Home Controller (polymorphism)")
        self.geometry("450x620")
        self.resizable(False, False)

        # ICONO DE LA VENTANA
        self.load_icon()

        # COLORES
        self.configure(bg="black")

        self.devices = {
            "Speaker": SmartSpeaker(),
            "Light": SmartLight(),
            "Fan": SmartFan(),
            "Thermostat": SmartThermostat()
        }

        self.build_ui()

    def load_icon(self):
        # Busca el PNG en la misma carpeta que este archivo
        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "limpieza-de-la-casa.png"
        )
        try:
            self.icon_img = tk.PhotoImage(file=icon_path)
            self.iconphoto(True, self.icon_img)
        except tk.TclError:
            pass  # si no se encuentra el icono, la app sigue funcionando

    def build_ui(self):

        # HEADER
        title = tk.Label(
            self,
            text="SMART HOME CENTER",
            font=("Arial", 16, "bold"),
            bg="black",
            fg="gold"
        )
        title.pack(pady=20)

        # LABEL FRAME
        group_box = tk.LabelFrame(
            self,
            text="Select Device",
            font=("Arial", 12, "bold"),
            bg="black",
            fg="green",
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20)

        self.selected_device = tk.StringVar(value="Speaker")

        # RADIO BUTTONS
        for device in self.devices.keys():

            rb = tk.Radiobutton(
                group_box,
                text=device,
                variable=self.selected_device,
                value=device,
                bg="black",
                fg="gold",
                selectcolor="green",
                activebackground="black",
                activeforeground="gold"
            )
            rb.pack(anchor="w")

        # BOTONES (Turn On / Turn Off)
        btn_frame = tk.Frame(self, bg="black")
        btn_frame.pack(pady=20)

        btn_action = tk.Button(
            btn_frame,
            text="TURN ON DEVICE",
            command=self.handle_action,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        btn_action.pack(side="left", padx=10)

        # NUEVO: boton Turn Off
        btn_off = tk.Button(
            btn_frame,
            text="TURN OFF DEVICE",
            command=self.handle_turn_off,
            bg="red",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        btn_off.pack(side="left", padx=10)

        # AREA RESULTADOS
        self.lbl_output = tk.Label(
            self,
            text="Select a device and click the button.",
            font=("Arial", 10),
            bg="black",
            fg="gold",
            relief="groove",
            width=45,
            height=4
        )
        self.lbl_output.pack(pady=10)

        # NUEVO: ACTIVITY LOG (Listbox con scrollbar)
        log_frame = tk.LabelFrame(
            self,
            text="Activity Log",
            font=("Arial", 12, "bold"),
            bg="black",
            fg="green",
            padx=10,
            pady=5
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        scrollbar = tk.Scrollbar(log_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.log_list = tk.Listbox(
            log_frame,
            yscrollcommand=scrollbar.set,
            bg="black",
            fg="gold",
            font=("Consolas", 9),
            selectbackground="green",
            height=6
        )
        self.log_list.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.log_list.yview)

    def add_log(self, message):
        # Agrega una linea con hora al Activity Log y baja al final
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_list.insert(tk.END, f"[{timestamp}] {message}")
        self.log_list.yview_moveto(1.0)

    def handle_action(self):

        chosen_device = self.selected_device.get()

        active_device = self.devices[chosen_device]

        # POLIMORFISMO
        result = active_device.turn_on()

        self.lbl_output.config(
            text=result,
            fg="green"
        )

        self.add_log(result)

    # NUEVO: accion de apagar
    def handle_turn_off(self):

        chosen_device = self.selected_device.get()

        active_device = self.devices[chosen_device]

        # POLIMORFISMO
        result = active_device.turn_off()

        self.lbl_output.config(
            text=result,
            fg="red"
        )

        self.add_log(result)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()

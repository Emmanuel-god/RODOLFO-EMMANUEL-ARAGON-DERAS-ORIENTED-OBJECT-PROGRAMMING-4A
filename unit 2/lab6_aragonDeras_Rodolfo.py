from tkinter import *
from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractmethod


# =========================
# SUPERCLASE
# =========================
class SmartDevice(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass


# =========================
# CLASES HIJAS
# =========================
class SmartLight(SmartDevice):

    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
        return f"{self.name} set brightness to 100%"


class SmartSpeaker(SmartDevice):

    def __init__(self):
        super().__init__("Google Speaker")

    def turn_on(self):
        return f"{self.name} playing my music"


class SmartFan(SmartDevice):

    def __init__(self):
        super().__init__("Smart Fan")

    def turn_on(self):
        return f"{self.name} set temperature to 35°C"


# =========================
# GUI
# =========================
class SmartHomeApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Lab 6. Smart Home Controller (polymorphism)")
        self.geometry("450x350")
        self.resizable(False, False)

        # COLORES
        self.configure(bg="black")

        self.devices = {
            "Speaker": SmartSpeaker(),
            "Light": SmartLight(),
            "Fan": SmartFan()
        }

        self.build_ui()

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

        # BOTON
        btn_action = tk.Button(
            self,
            text="TURN ON DEVICE",
            command=self.handle_action,
            bg="green",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        btn_action.pack(pady=20)

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

    def handle_action(self):

        chosen_device = self.selected_device.get()

        active_device = self.devices[chosen_device]

        # POLIMORFISMO
        result = active_device.turn_on()

        self.lbl_output.config(
            text=result,
            fg="green"
        )


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
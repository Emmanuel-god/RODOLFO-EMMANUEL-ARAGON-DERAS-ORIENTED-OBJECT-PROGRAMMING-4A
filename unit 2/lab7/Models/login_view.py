import tkinter as tk
from tkinter import messagebox
from Models.login_model import user
from Views.home_view import Dashboardventana

class LoginVentana:

    def __init__(self, root):
        self.root = root
        self.root.title("inicio de sesion al sistema")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

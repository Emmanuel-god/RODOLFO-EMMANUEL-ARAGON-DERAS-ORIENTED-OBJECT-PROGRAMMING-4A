import tkinter as tk
from Views.login_view import LoginView
from Controller.auth_controller import Authentication

if __name__ == "__main__":
    root = tk.Tk()
    vista = LoginView(root)
    Authentication(vista)
    root.mainloop()

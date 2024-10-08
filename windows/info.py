import tkinter as tk
from customtkinter import *

class infoWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Window 1")
        self.geometry("300x200")

        label = CTkLabel(self, text="This is Window 1")
        label.pack(pady=20)

        button = CTkButton(self, text="Close", command=self.destroy)
        button.pack(pady=20)
import tkinter as tk
from customtkinter import *

class subjectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Horario")
        self.geometry("400x500")
        self.iconbitmap("img\\school.ico")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        WindowWrap = CTkFrame(self, bg_color="red", fg_color="transparent")
        WindowWrap.grid(sticky="nsew")
        WindowWrap.grid_rowconfigure(0, weight=1)
        WindowWrap.grid_rowconfigure(1, weight=1)
        WindowWrap.grid_columnconfigure(0, weight=1)

        TopContainer = CTkFrame(WindowWrap, bg_color="black", fg_color="transparent")
        TopContainer.grid(row=0, sticky="nsew", padx=(20,20), pady=(20, 0))
        TopContainer.grid_rowconfigure(0, weight=1)
        TopContainer.grid_rowconfigure(1, weight=1)
        TopContainer.grid_columnconfigure(0, weight=1)
        TopContainer.grid_columnconfigure(1, weight=1)
        
        asignatura = CTkLabel(TopContainer, text="Lengua", text_color="white", fg_color="black", bg_color="black", font=("Garamond", 24), wraplength=360)
        asignatura.grid(row=0, column=0, sticky="n")

        profesor_title = CTkLabel(TopContainer, text="Profesor: ", text_color="white", fg_color="black", bg_color="black", font=("Garamond", 18), wraplength=350)
        profesor_title.grid(row=1, column=0, sticky="nw")

        profesor_text = CTkLabel(TopContainer, text="Juana María Montesinos Urrutia", text_color="white", fg_color="black", bg_color="black", font=("Garamond", 18), wraplength=350)
        profesor_text.grid(row=1, column=1, sticky="nw")

        MidContainer = CTkFrame(WindowWrap, bg_color="black", fg_color="transparent")
        MidContainer.grid(row=1, sticky="nsew", padx=(20,20), pady=(0, 20))

        MidContainer.grid_rowconfigure(0, weight=1)
        MidContainer.grid_columnconfigure(0, weight=1)
        MidContainer.grid_columnconfigure(1, weight=1)
        MidContainer.grid_columnconfigure(2, weight=1)

        trimestre_1 = CTkLabel(MidContainer, text="1", bg_color="blue", font=("Garamond", 18))
        trimestre_1.grid(row=0, column=0, sticky="nsew")
        trimestre_2 = CTkLabel(MidContainer, text="2", bg_color="blue", font=("Garamond", 18))
        trimestre_2.grid(row=0, column=1, sticky="nsew")
        trimestre_3 = CTkLabel(MidContainer, text="3", bg_color="blue", font=("Garamond", 18))
        trimestre_3.grid(row=0, column=2, sticky="nsew")
        # TopContainer = CTkFrame(WindowWrap, bg_color="transparent", fg_color="transparent")
        # TopContainer.grid(row=0, column=0)

        # # ASIGNATURA
        # asignatura = CTkFrame(TopContainer, fg_color="transparent")
        # asignatura.grid(padx=20, pady=20)

        # asignatura_title = CTkLabel(asignatura, text="Lengua", font=("Impact", 28))
        # asignatura_title.grid(row=0, column=0)

        # # PROFESOR
        # profesor = CTkFrame(TopContainer, fg_color="transparent")
        # profesor.grid(padx=20, pady=20)

        # profesor_title = CTkLabel(profesor, text="Profesor/a: ", font=("Garamond", 18))
        # profesor_title.grid(row=0, column=0)

        # profesor_text = CTkLabel(profesor, text="Juana María Monsanto Montero", font=("Verdana", 16))
        # profesor_text.grid(row=0, column=1)

        
        

if __name__ == "__main__":
    app = subjectWindow()
    app.mainloop()
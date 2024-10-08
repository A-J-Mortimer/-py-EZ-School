import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

from include.dynamicallyGenerate import *

from windows.info import infoWindow
from windows.timetable import timetableWindow


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("550x400")
        self.iconbitmap("draft\\img\\school.ico")
        
        WindowWrap = CTkFrame(self, bg_color="transparent", fg_color="transparent")
        WindowWrap.grid(padx=10, pady=10)

        TopContainer = CTkFrame(WindowWrap, bg_color="transparent", fg_color="transparent")
        TopContainer.grid(row=0, column=0)

        BottomContainer = CTkFrame(WindowWrap, bg_color="transparent", fg_color="transparent")
        BottomContainer.grid(row=1, column=0)

        FooterContainer = CTkFrame(WindowWrap, bg_color="transparent", fg_color="transparent")
        FooterContainer.grid(row=2, column=0)

        # IMAGE LABEL - Top Container
        imgPath = Image.open("draft/img/school.ico")
        img = CTkImage(light_image=imgPath, dark_image=imgPath, size=(90, 90))
        icon = CTkLabel(TopContainer, image=img, text="")
        icon.grid(row=0, column=0, sticky="nsew")

        # GREETINGS LABEL - Top Container
        greetings_text = generateGreetings()
        greeting = CTkLabel(TopContainer, text=greetings_text, font=("Garamond", 18))
        greeting.grid(row=1, column=0, sticky="nsew")

        # INSPIRATIONAL QUOTES LABEL - Top Container
        inspirational_quote = generateQuote()
        quote = CTkLabel(TopContainer, text=inspirational_quote, wraplength=350)
        quote.grid(row=2, column=0, sticky="nsew")

        # BUTTON 1 - Bottom Container
        button_attributes = {
                                "width": 175,
                                "height": 58,
                                "border_width": 2,
                                "fg_color": "#00b6e3",
                                "hover_color": "#3b8ed0",
                                "border_color": "#00b6e3",
                                "font": ("Garamond", 18)
                            }

        button1 = CTkButton(BottomContainer, **button_attributes, text="HORARIO", command=self.open_window2)
        button1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # BUTTON 2 - Bottom Container
        button2 = CTkButton(BottomContainer, **button_attributes, text="INFO", command=self.open_window1)
        button2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # BUTTON 2 - Footer Container
        button2 = CTkButton(FooterContainer, **button_attributes, text="INFO", command=self.open_window1)
        button2.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def open_window1(self):
        window1 = infoWindow()
        window1.mainloop()

    def open_window2(self):
        window2 = timetableWindow()
        window2.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
## This a changed line
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

from include.dynamicallyGenerate import *

from windows.info import infoWindow
from windows.timetable import timetableWindow

from windows.slaves.timetable import *
from windows.slaves.subjects import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        ## DECLARING MASTER WINDOW
        self.title("Main Window")
        self.geometry("1150x500")
        self.iconbitmap("draft\\img\\school.ico")

        ## Creating the 3 columns main grid
        self.left_menu = CTkFrame(self, fg_color="transparent")
        self.left_menu.place(x=0, y=0, relwidth=0.25, relheight=1)
        self.left_menu.rowconfigure((0,1,2,3,4,5), weight=1, uniform="a")
        self.left_menu.columnconfigure((0,1), weight=1, uniform="a")

        self.center_main = CTkFrame(self, fg_color="transparent")
        self.center_main.place(relx=0.25, y=0, relwidth=0.5, relheight=1)
        self.center_main.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform="a")
        self.center_main.columnconfigure((0,1,2,3,4,5), weight=1, uniform="a")

        self.right_menu = CTkFrame(self, fg_color="transparent")
        self.right_menu.place(relx=0.75, y=0, relwidth=0.25, relheight=1)
        self.right_menu.rowconfigure((0,1,2,3,4,5), weight=1)
        self.right_menu.columnconfigure((0,1,2,3), weight=1, uniform="a")

        ## Creating left_menu widgets
        # IMAGE LABEL - Top Container
        left_menu_imgPath = Image.open("draft/img/school.ico")
        left_menu_img = CTkImage(light_image=left_menu_imgPath, dark_image=left_menu_imgPath, size=(95, 95))
        left_menu_icon = CTkLabel(self.left_menu, image=left_menu_img, text="")
        left_menu_icon.grid(row=0, column=0, sticky="nsew", columnspan=2, rowspan=2)

        # GREETINGS LABEL - Top Container
        left_menu_greetings_text = generateGreetings()
        left_menu_greeting = CTkLabel(self.left_menu, text=left_menu_greetings_text, font=("Garamond", 18))
        left_menu_greeting.grid(row=2, column=0, sticky="nsew", columnspan=2)

        # INSPIRATIONAL QUOTES LABEL - Top Container
        left_menu_inspirational_quote = generateQuote()
        left_menu_quote = CTkLabel(self.left_menu, text=left_menu_inspirational_quote, wraplength=220)
        left_menu_quote.grid(row=3, column=0, sticky="nsew", columnspan=2)

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
        
        # Button 1
        left_menu_button1 = CTkButton(self.left_menu, **button_attributes, text="HORARIO", command=self.open_window2)
        left_menu_button1.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

        # BUTTON 2
        left_menu_button2 = CTkButton(self.left_menu, **button_attributes, text="INFO", command=self.open_window1)
        left_menu_button2.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)

        # BUTTON 3
        left_menu_button3 = CTkButton(self.left_menu, **button_attributes, text="INFO", command=self.open_window1)
        left_menu_button3.grid(row=5, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)

        ## Calling center_main widgets from windows.slaves.timetable.py
        generate_table(self.center_main)

        ## Calling right_menu widges from windows.slaves.subjects.py
        generate_subject_info(self, self.right_menu, "Lengua")

    def open_window1(self):
        # window1 = infoWindow()
        # window1.mainloop()
        generate_table(self.center_main)

    def open_window2(self):
        # window2 = timetableWindow()
        # window2.mainloop()
        for widget in self.center_main.winfo_children():
            widget.destroy()

    

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
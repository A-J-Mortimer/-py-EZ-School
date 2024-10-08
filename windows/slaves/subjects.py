import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

from include.core.db_functions import process_text_file
from include.core.datetime_functions import is_today_over_x_date
from include.core.math_functions import *

quarter_info_headings = [
            "Fecha",
            "Tipo",
            "Nota",
            "Media"
        ]


quarter_button_style = {
                        "height": 20,
                        "border_width": 2,
                        "fg_color": "#00b6e3",
                        "hover_color": "#3b8ed0",
                        "border_color": "#00b6e3",
                        "font": ("Garamond", 18)
                    }

quarter_button_active_style = {
                        "height": 20,
                        "border_width": 2,
                        "fg_color": "#344a53",
                        "hover_color": "#344a53",
                        "border_color": "#00b6e3",
                        "font": ("Garamond", 18)
                    }

def generate_subject_info(self, right_menu, subject):
        # print(subject)
        ## Creating right_menu widgets
 
        right_menu_subject = CTkLabel(right_menu, text="ASIGNATURA", font=("Garamond", 18))
        right_menu_subject.grid(row=0, column=0, sticky="nsew", columnspan=4)

        right_menu_teacher_text = CTkLabel(right_menu, text="Antonio José Montesinos Guzmán", font=("Garamond", 14), wraplength=220)
        right_menu_teacher_text.grid(row=1, column=0, sticky="nsew", columnspan=4)

        ## Creating a frame to hold any anything to do with the quarters
        quarter_frame = CTkFrame(right_menu, fg_color="transparent")
        quarter_frame.grid(row=2, column=0, sticky="nsew", columnspan=4)
        quarter_frame.rowconfigure((0,1,2,3,4), weight=1)
        quarter_frame.columnconfigure((0,1,2,3), weight=1, uniform="a")

        right_menu_quarter_title = CTkLabel(quarter_frame, text="TRIMESTRE", font=("Garamond", 18), wraplength=220)
        right_menu_quarter_title.grid(row=2, column=0, sticky="nsew", columnspan=4)

        self.right_menu_quarter_select_1 = CTkButton(quarter_frame, **quarter_button_active_style, text="1", command=lambda:quarter_select_active_button(1))
        self.right_menu_quarter_select_1.grid(row=3, column=0, sticky="nsew", padx=(5), columnspan=1)
        
        self.right_menu_quarter_select_2 = CTkButton(quarter_frame, **quarter_button_style, text="2", command=lambda:quarter_select_active_button(2))
        self.right_menu_quarter_select_2.grid(row=3, column=1, sticky="nsew", padx=(5), columnspan=1)

        self.right_menu_quarter_select_3 = CTkButton(quarter_frame, **quarter_button_style, text="3", command=lambda:quarter_select_active_button(3))
        self.right_menu_quarter_select_3.grid(row=3, column=2, sticky="nsew", padx=(5), columnspan=1)

        self.right_menu_quarter_select_4 = CTkButton(quarter_frame, **quarter_button_style, text="FINAL", command=lambda:quarter_select_active_button(4))
        self.right_menu_quarter_select_4.grid(row=3, column=3, sticky="nsew", padx=(5), columnspan=1)

        ## Create a frame to hold the quarter´s info
        quarter_info_frame = CTkFrame(quarter_frame, fg_color="transparent")
        quarter_info_frame.grid(row=4, column=0, sticky="nsew", columnspan=4)
        quarter_info_frame.rowconfigure((0,1,2,3,4), weight=1)
        quarter_info_frame.columnconfigure((0,1,2,3), weight=1, uniform="a")

        def quarter_delete(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        def quarter_select_active_button(button):
            for i in range(0, 4):
                i+=1
                # print(button, i)
                if i == button:
                    # print("Button pressed = ", button)
                    selected_button = getattr(self, f"right_menu_quarter_select_{i}")
                    selected_button.configure(**quarter_button_active_style)

                    # Destroy current frame and populate with selected info
                    quarter_delete(quarter_info_frame)
                    create_quarter_info(subject, i)
                else:
                    # print("Button not selected = ", i)
                    unselected_button = getattr(self, f"right_menu_quarter_select_{i}")
                    unselected_button.configure(**quarter_button_style)
    

        def create_quarter_info(subject, selection=False):
            if selection == False:
                ## Check if the date is over x, to calculate what´s the running quarter
                if is_today_over_x_date("16/09/2024"):
                    active_quarter = "1"
                elif is_today_over_x_date("03/05/2025"):
                    active_quarter = "2"
                else:
                    active_quarter = "3"
            else:
                 active_quarter = selection
            ## Activate button corresponding to running quarter
            current_quarter = getattr(self, f"right_menu_quarter_select_{active_quarter}")
            current_quarter.configure(**quarter_button_active_style)

            def populate_quarter_headings():
                num_items = len(quarter_info_headings)
                # print(num_items)
                for i in range(0, num_items):
                    # print(quarter_info_headings[i])
                    wraplength_calc = round(222/num_items)
                    label_name = f"quarter_top_label_{i}"
                    self.label_name = CTkLabel(quarter_info_frame, text=quarter_info_headings[i], wraplength=wraplength_calc)
                    self.label_name.grid(row=0, column=i, sticky="ew", columnspan=1)

            def populate_quarter_info(subject):
                process_text_file(subject, "quarter_marks", active_quarter, quarter_info_frame, 1, 222)
                # process_text_file("quarter", "Calificaciones.db", f"subjects/{subject}/Trimestres/1", quarter_info_frame, 1, 222)
                # proccess_text_file("lol.txt", "subjects/test", "quarter_info_frame", "Label", 3, 0, 222)

            def create_quarter_buttons():
                img_path = Image.open("draft/img/buttons/add.png")
                my_image = CTkImage(light_image=img_path,
                                  dark_image=img_path,
                                  size=(30, 30))
                
                button = CTkButton(
                                        quarter_info_frame,
                                        width=30,
                                        text="",
                                        fg_color="transparent",
                                        hover_color="#cbcbcb",
                                        image=my_image,
                                        anchor="center",  # Position the image to the left of the text
                                        command=lambda: print("Button clicked!")
                                    )
                button.grid(pady=(5,0), sticky="ns", columnspan=4)

            populate_quarter_headings()
            populate_quarter_info(subject)
            create_quarter_buttons()


        create_quarter_info("Lengua")
import tkinter as tk
from customtkinter import *

def generate_table(center_main):
    # Create a list of lists to represent the table data
    table_data = [
        ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
        ["08:00 - 09:00", "Lengua", "Literatura", "E. Física", "Inglés", "Valores"],
        ["09:00 - 10:00", "Antropología", "Inglés", "Lengua", "Filosofía", "Literatura"],
        ["10:00 - 11:00", "Matemáticas", "Antropología", "Economía", "Literatura", "Lengua"],
        ["11:00 - 11:30", "Recreo", "Recreo", "Recreo", "Recreo", "Recreo"],
        ["11:30 - 12:30", "Economía", "Economía", "Debate", "Lengua", "Inglés"],
        ["12:30 - 13:30", "Literatura", "Matemáticas", "Inglés", "Economía", "Debate"],
        ["13:30 - 14:30", "E. Física", "Filosofía", "Filosofía", "Matemáticas", "Matemáticas"]
    ]
    # Create a grid layout for the table
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            cell = CTkButton(center_main, text=table_data[i][j], corner_radius=0, fg_color="white", text_color="#333", hover_color="#dbdbdb")
            if i == 0:
                if j == 0:
                    cell.configure(fg_color="", hover_color="", text_color="white")
                elif j != 0:
                    cell.configure(fg_color="#00b6e3", hover_color="#00b6e3", font=("Garamond", 18), text_color="white")
            elif i == 4:
                cell.configure(fg_color="#d9d9d9", hover_color="#d9d9d9", font=("Garamond", 14), text_color="white")
            
            if j ==0:
                if i != 0:
                    cell.configure(fg_color="#d9d9d9", hover_color="#d9d9d9", font=("Lexend", 14), text_color="black")

            if i != 0 and j != 0:
                get_subject_name = cell.cget("text")
                cell.configure(command=lambda subject=get_subject_name: subject_info(subject))
            
            cell.grid(row=i, column=j, sticky="nsew")

def subject_info(subject):
        # if subject == "Lengua":
        #     print("LENGUA!")

        print(subject)
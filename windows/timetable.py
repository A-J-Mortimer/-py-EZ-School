import tkinter as tk
from customtkinter import *

class timetableWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Window 2")
        self.geometry("900x280")
        self.iconbitmap("img\\school.ico")

        
        background_color = "#ebebeb"

        WindowWrap = CTkFrame(self, bg_color=background_color)
        WindowWrap.grid(padx=0, pady=0)

        TopContainer = CTkFrame(WindowWrap)
        TopContainer.grid(row=0, column=0)

        TimeTable_TopContainer = CTkFrame(TopContainer)
        TimeTable_TopContainer.grid(row=0, column=0, sticky="nsew")

        # Create a list of lists to represent the table data
        table_data = [
            ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
            ["08:00 - 09:00", "Lengua", "Literatura", "Educación Física", "Inglés", "Valores"],
            ["09:00 - 10:00", "Antropología", "Inglés", "Lengua", "Filosofía", "Literatura"],
            ["10:00 - 11:00", "Matemáticas", "Antropología", "Economía", "Literatura", "Lengua"],
            ["11:00 - 11:30", "Recreo", "Recreo", "Recreo", "Recreo", "Recreo"],
            ["11:30 - 12:30", "Economía", "Economía", "Debate", "Lengua", "Inglés"],
            ["12:30 - 13:30", "Literatura", "Matemáticas", "Inglés", "Economía", "Debate"],
            ["13:30 - 14:30", "Educación Física", "Filosofía", "Filosofía", "Matemáticas", "Matemáticas"]
        ]

        # Create a grid layout for the table
        for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                cell = CTkButton(TimeTable_TopContainer, text=table_data[i][j], corner_radius=0, fg_color="white", text_color="#333", hover_color="#dbdbdb")
                if i == 0:
                    if j == 0:
                        cell.configure(fg_color=background_color, hover_color=background_color, text_color="white")
                    elif j != 0:
                        cell.configure(fg_color="#00b6e3", hover_color="#00b6e3", font=("Garamond", 18), text_color="white")
                elif i == 4:
                    cell.configure(fg_color="#d9d9d9", hover_color="#d9d9d9", font=("Garamond", 14), text_color="white")
                
                if j ==0:
                    if i != 0:
                        cell.configure(fg_color="#d9d9d9", hover_color="#d9d9d9", font=("Lexend", 14), text_color="black")

                if i != 0 and j != 0:
                    get_subject_name = cell.cget("text")
                    cell.configure(command=lambda subject=get_subject_name: self.subject_info(subject))
                
                cell.grid(row=i, column=j, sticky="nsew")
                
                TimeTable_TopContainer.grid_rowconfigure(i, weight=1)
                TimeTable_TopContainer.grid_columnconfigure(j, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # SubjectInfo_TopContainer = CTkFrame(TopContainer, width=300)
        # SubjectInfo_TopContainer.grid(row=0, column=1, sticky="nsew")

        # profesor_title = CTkLabel(SubjectInfo_TopContainer, text="Profesor/a: ", font=("Garamond", 14),wraplength=300)
        # profesor_title.grid(row=0, column=0, padx=(10,0), pady=(10,0))
        # profesor_text = CTkLabel(SubjectInfo_TopContainer, text="Juan Alberto Guillón Montero", wraplength=300)
        # profesor_text.grid(row=0, column=1, padx=(0,10), pady=(10, 0))
        # # greeting = CTkLabel(SubjectInfo_TopContainer, text="greetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_textgreetings_text", font=("Garamond", 18),wraplength=300)
        # # greeting.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)


    def subject_info(self, subject):
        # if subject == "Lengua":
        #     print("LENGUA!")

        print(subject)


if __name__ == "__main__":
    app = timetableWindow()
    app.mainloop()
import tkinter as tk
from tkinter import ttk
from customtkinter import *

class subjectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Horario")
        win_width = 600
        win_height = 800
        self.geometry(f"{win_width}x{win_height}")
        self.iconbitmap("draft\\img\\school.ico")

        left_panel_width = 0.65
        left_panel = CTkFrame(self, fg_color="red")
        left_panel.place(x=0, y=0, relwidth=left_panel_width, relheight=1)
        left_panel.rowconfigure((0,1,2,3,4,5), weight=1, uniform="a")
        left_panel.columnconfigure((0,1,2), weight=1, uniform="a")

        self.right_panel = CTkFrame(self, fg_color="blue")
        self.right_panel.place(relx=0.65, y=0, relwidth=0.35, relheight=1)
        self.right_panel.rowconfigure((0,1,2,3,4,5), weight=1, uniform="a")
        self.right_panel.columnconfigure((0,1), weight=1, uniform="a")

        def populate_left_panel(subject="Lengua", variable=1):

            db_path = "draft/db"
            subject_path = f"subjects/{subject}/Trimestres/{variable}"
            filename = "Calificaciones.db" 

            construct_path = os.path.join(db_path, subject_path, filename)
            
            def calculate_rows_and_columns():
                rows_columns = []
                if os.path.exists(construct_path):
                    file_path = os.path.join(construct_path)
                    ## Lines == Rows / Words in line == Columns
                    with open(file_path, 'r') as file:
                        count_lines = 0
                        for line in file:
                            words = line.strip().split(',')
                            count_words_per_line = 0
                            count_lines += 1
                            for word in words:
                                count_words_per_line += 1

                        
                        rows_columns.append(count_lines)
                        rows_columns.append(count_words_per_line)
                        # print(count_lines, count_words_per_line)
                        # print(rows_columns)
                        return(rows_columns)

            def construct_left_panel():
                rows_columns = calculate_rows_and_columns()
                rows = rows_columns[0]
                columns = rows_columns[1]

                print(rows, columns)
                
                if os.path.exists(construct_path):
                    file_path = os.path.join(construct_path)
                    ## Lines == Rows / Words in line == Columns
                    with open(file_path, 'r') as file:
                        row = 0
                        for line in file:
                            words = line.strip().split(',')
                            total_words = len(words)
                            
                            column = 0
                            for word in words:
                                left_panel_label = CTkButton(left_panel, text=word, font=("Garamond", 18))
                                left_panel_label.grid(row=row, column=column, sticky="nsew")

                                column += 1
                            
                            row += 1



                # process_text_file(subject, "quarter_marks", variable, left_panel, 1, 130)




            construct_left_panel()


        populate_left_panel()

        # treeview = ttk.Treeview(left_panel, columns=("Fecha", "Nota"), show="headings")
        # treeview.heading("Fecha", text="Fecha")
        # treeview.heading("Nota", text="Nota")
        # # Set the width for each column
        # treeview.column("Fecha", width=75, anchor="center")
        # treeview.column("Nota", width=75, anchor="center")

        # treeview.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = subjectWindow()
    app.mainloop()

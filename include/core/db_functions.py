import os
import tkinter as tk
from customtkinter import *

from include.core.math_functions import *


db_path = "db"

def process_text_file(subject, type, variable, frame=False, starting_row=False, width=False):
    
    if type == "quarter_marks":
        subject_path = f"subjects/{subject}/Trimestres/{variable}"
        filename = "Calificaciones.db"

    construct_path = os.path.join(db_path, subject_path, filename)
    # if folder != False:
    #     construct_path = os.path.join(db_path, folder, filename)
    # else:
    #     construct_path = os.path.join(db_path, filename)
    # print(construct_path)

    if os.path.exists(construct_path):
        file_path = os.path.join(construct_path)
        with open(file_path, 'r') as file:
            i = 0
            quarter_marks = []
            count_marks=0
            addup_marks=0
            average=0
            for line in file:
                words = line.strip().split(',')
                total_words = len(words)
                word_count = 0
                # Get number of columns
                column_count = 0
                for word in words:
                    column_count += 1

                for word in words:
                    label_name = CTkLabel(frame, text=word, wraplength=round(width/column_count))
                    label_name.grid(row=starting_row+i, column=word_count, sticky="ew", columnspan=1)

                    ## Calculate average marks
                    if type == "quarter_marks":
                        ## Marks should always be last data in a file´s line -> word_count == total_words-1
                        if word_count == total_words-1:
                            # print(i, word_count)
                            # print(word)
                            quarter_marks.append(float(word))
                            if i == 0:
                                average = round(quarter_marks[0], 2)
                            elif i >= 1:
                                count_marks = len(quarter_marks)
                                addup_marks = sum(quarter_marks)
                                average = round(addup_marks/count_marks, 2)
                            
                            label_name = CTkLabel(frame, text=average, wraplength=74)
                            label_name.grid(row=starting_row+i, column=word_count+1, sticky="ew", columnspan=1)

                        # label_name = CTkLabel(frame, text="", wraplength=74)
                        # label_name.grid(row=3+i, column=word_count+1, sticky="ew", columnspan=1)


                    word_count += 1
                    # print(f"Line {i}:")
                    # print(f"  {word}")
                i += 1
        # print(quarter_marks)
    
        desired_average = 5
        minimum_mark_for_desired_average = (desired_average * (count_marks + 1)) - addup_marks
        print(minimum_mark_for_desired_average)
        if minimum_mark_for_desired_average < 0:
            minimum_mark_for_desired_average = 0
    
        label_name = CTkLabel(frame, text=f"Para una media de: {desired_average}\nPróxima calificación: {minimum_mark_for_desired_average}", fg_color="#f9f871", corner_radius=10,wraplength=222, height=40)
        # label_name = CTkLabel(frame, text=f"Para un {desired_average} de media, tu próxima nota ha de ser{minimum_mark_for_desired_average}", fg_color="#f9f871", corner_radius=20, wraplength=222)
        label_name.grid(row=starting_row+i+1, column=0, sticky="nsew", columnspan=5, padx=5)
    else:
        print(f"ERROR -> db_functions.py: The db directory ({construct_path}) is non existent.")

# proccess_text_file("lol.txt", "subjects/test")

from tkinter import ttk
import tkinter
import csv
from tkinter import *


def read_csv(file_name):
    file = open(file_name, "r")
    rows = csv.reader(file, delimiter=",")
    return list(rows)
    

   
def main():
    def btn_click():
        print(type(e1.get()))
    
    window = tkinter.Tk()
    window.geometry("700x700")

    frame = ttk.Frame(window, padding=20, borderwidth=5, relief="solid")
    frame.grid()

    e1 = ttk.Entry(frame)
    e1.grid(row=0, column=0, padx=2, pady=15)
    btn = ttk.Button(frame, text="Search", command=btn_click).grid(row=0, column=1, padx=15, pady=15)
    #e1.pack()

    ttk.Label(frame, text="ID", borderwidth=2, relief="solid", width=15).grid(column=0, row=1, padx=2)
    ttk.Label(frame, text="NAME", borderwidth=2, relief="solid", width=15).grid(column=1, row=1, padx=2)
    ttk.Label(frame, text="SURNAME", borderwidth=2, relief="solid", width=15).grid(column=2, row=1, padx=2)
    ttk.Label(frame, text="DEPARTMENT", borderwidth=2, relief="solid", width=15).grid(column=3, row=1, padx=2)
    ttk.Label(frame, text="START DATE", borderwidth=2, relief="solid", width=15).grid(column=4, row=1, padx=2)

    employees = read_csv("/home/jurgen/dev/phone_search/employees.csv")
    row_number = 2
    for employee in employees[1:10]:
        ttk.Label(frame, text=employee[0], borderwidth=2, relief="solid", width=15).grid(column=0, row=row_number, padx=2)
        ttk.Label(frame, text=employee[1], borderwidth=2, relief="solid", width=15).grid(column=1, row=row_number, padx=2)
        ttk.Label(frame, text=employee[2], borderwidth=2, relief="solid", width=15).grid(column=2, row=row_number, padx=2)
        ttk.Label(frame, text=employee[3], borderwidth=2, relief="solid", width=15).grid(column=3, row=row_number, padx=2)
        ttk.Label(frame, text=employee[4], borderwidth=2, relief="solid", width=15).grid(column=4, row=row_number, padx=2)
        row_number += 1

    window.mainloop()



main()
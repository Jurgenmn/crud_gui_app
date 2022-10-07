from tkinter import ttk
import tkinter
import csv
from tkinter import *


parent_frame = None
child_frame = None


def read_csv(file_name):
    file = open(file_name, "r")
    rows = csv.reader(file, delimiter=",")
    return list(rows)

def create_frame(window):
    frame = ttk.Frame(window, padding=20, borderwidth=5, relief="solid") # creating frame and puting it iside the window
    frame.grid()

    return frame

def draw_emp(frame, employees):

    row_number = 2
    for employee in employees:
        ttk.Label(frame, text=employee[0], borderwidth=2, relief="solid", width=15).grid(column=0, row=row_number, padx=2)
        ttk.Label(frame, text=employee[1], borderwidth=2, relief="solid", width=15).grid(column=1, row=row_number, padx=2)
        ttk.Label(frame, text=employee[2], borderwidth=2, relief="solid", width=15).grid(column=2, row=row_number, padx=2)
        ttk.Label(frame, text=employee[3], borderwidth=2, relief="solid", width=15).grid(column=3, row=row_number, padx=2)
        ttk.Label(frame, text=employee[4], borderwidth=2, relief="solid", width=15).grid(column=4, row=row_number, padx=2)
        row_number += 1

    
def draw_frame(window, employees):
    global parent_frame
    global child_frame
    parent_frame = create_frame(window)

    child_frame = create_frame(parent_frame)
    child_frame.grid(row=2, column=0, columnspan=5, padx=15, pady=15)

    e1 = ttk.Entry(parent_frame)  #Putting the entry inside the frame
    e1.grid(row=0, column=0, padx=2, pady=15)

    def btn_click():
        global child_frame
        global parent_frame
        input_value = e1.get()
        result = filter_by_department(input_value)
        child_frame.destroy()
        child_frame.pack_forget()

        child_frame = create_frame(parent_frame)
        child_frame.grid(row=2, column=0, columnspan=5, padx=15, pady=15)
        draw_emp(child_frame, result)


    btn = ttk.Button(parent_frame, text="Search", command=btn_click).grid(row=0, column=1, padx=15, pady=15)

    ttk.Label(parent_frame, text="ID", borderwidth=2, relief="solid", width=15).grid(column=0, row=1, padx=2)
    ttk.Label(parent_frame, text="NAME", borderwidth=2, relief="solid", width=15).grid(column=1, row=1, padx=2)
    ttk.Label(parent_frame, text="SURNAME", borderwidth=2, relief="solid", width=15).grid(column=2, row=1, padx=2)
    ttk.Label(parent_frame, text="DEPARTMENT", borderwidth=2, relief="solid", width=15).grid(column=3, row=1, padx=2)
    ttk.Label(parent_frame, text="START DATE", borderwidth=2, relief="solid", width=15).grid(column=4, row=1, padx=2)

    draw_emp(child_frame, employees)



def filter_by_department(dpt):
    result = []
    employees = read_csv("/home/jurgen/dev/phone_search/employees.csv")
    for employee in employees:
        if employee[3] == dpt:
            result.append(employee)

    return result    

def main():
        
    window = tkinter.Tk()  #Creating the window
    window.geometry("900x900")

    employees = read_csv("/home/jurgen/dev/phone_search/employees.csv")

    draw_frame(window, employees[1:10])

    window.mainloop()



main()
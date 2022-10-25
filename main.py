from tkinter import ttk
import tkinter
import csv
from tkinter import *

# GLOBAL vars
parent_frame = None
child_frame = None
e1 = None
e2 = None
FILE_PATH = './employees.csv'


def read_csv(file_name):
    file = open(file_name, "r")
    rows = csv.reader(file, delimiter=",")
    return list(rows)

def create_frame(window):
    frame = ttk.Frame(window, padding=20, borderwidth=5, relief="solid") # creating frame and puting it iside the window
    frame.grid()

    return frame

def draw_emp(frame, employees):
    ttk.Label(frame, text="ID", borderwidth=2, relief="solid", width=15).grid(column=0, row=2, padx=2)
    ttk.Label(frame, text="NAME", borderwidth=2, relief="solid", width=15).grid(column=1, row=2, padx=2)
    ttk.Label(frame, text="SURNAME", borderwidth=2, relief="solid", width=15).grid(column=2, row=2, padx=2)
    ttk.Label(frame, text="DEPARTMENT", borderwidth=2, relief="solid", width=15).grid(column=3, row=2, padx=2)
    ttk.Label(frame, text="START DATE", borderwidth=2, relief="solid", width=15).grid(column=4, row=2, padx=2)


    row_number = 3
    for employee in employees:
        ttk.Label(frame, text=employee[0], borderwidth=2, relief="solid", width=15).grid(column=0, row=row_number, padx=2)
        ttk.Label(frame, text=employee[1], borderwidth=2, relief="solid", width=15).grid(column=1, row=row_number, padx=2)
        ttk.Label(frame, text=employee[2], borderwidth=2, relief="solid", width=15).grid(column=2, row=row_number, padx=2)
        ttk.Label(frame, text=employee[3], borderwidth=2, relief="solid", width=15).grid(column=3, row=row_number, padx=2)
        ttk.Label(frame, text=employee[4], borderwidth=2, relief="solid", width=15).grid(column=4, row=row_number, padx=2)
        row_number += 1

def update_employee(id, first_name, last_name, department, start_date):
    employees = read_csv(FILE_PATH)
    file = open(FILE_PATH, "w") # open returns a file object so we can modify it
    writer = csv.writer(file, delimiter=",")
    for employee in employees:
        if employee[0] == id:
            employee[1] = first_name
            employee[2] = last_name
            employee[3] = department
            employee[4] = start_date

        writer.writerow(employee)


def draw_frame(window, employees):
    global parent_frame
    global child_frame
    global e1
    global e2

    parent_frame = create_frame(window)
    child_frame = create_frame(parent_frame)
    child_frame.grid(row=3, column=0, columnspan=5, padx=15, pady=15)

    e1 = ttk.Entry(parent_frame, width=15)  #Putting the entry inside the frame
    e1.grid(row=0, column=0, padx=2, pady=15)

    e2 = ttk.Entry(parent_frame, width=15)  #Putting the entry inside the frame for deleting
    e2.grid(row=0, column=3, padx=2, pady=15)
    

    def redraw_frame(employees):
        global child_frame
        global parent_frame
        global e1
        global e2
        child_frame.destroy() #Updating the UI
        child_frame.pack_forget()
        child_frame = create_frame(parent_frame)
        child_frame.grid(row=2, column=0, columnspan=5, padx=15, pady=15)

        e1.delete(0, END)
        e2.delete(0, END)


    def btn_search():
        input_value = e1.get()
        result = filter_by_department(input_value)

        redraw_frame(result)



    def btn_delete():
        input_value = e2.get()
        employees = read_csv(FILE_PATH)
        file = open(FILE_PATH, "w")
        writer = csv.writer(file, delimiter=",")
        for employee in employees:
            if employee[0] != input_value:
                writer.writerow(employee)

        employees = read_csv(FILE_PATH)
        redraw_frame(employees[1: 10])

    def button_home():
        employees = read_csv(FILE_PATH)
        redraw_frame(employees[1:10])

    def button_update():
        global parent_frame
        global child_frame
        
        child_frame.destroy() #Updating the UI
        child_frame.pack_forget()
        child_frame = create_frame(parent_frame)
        child_frame.grid(row=2, column=0, columnspan=5, padx=15, pady=15)
        
        ttk.Label(child_frame, text="ID", borderwidth=2, relief="solid", width=15).grid(column=0, row=0, padx=2)
        ttk.Label(child_frame, text="NAME", borderwidth=2, relief="solid", width=15).grid(column=1, row=0, padx=2)
        ttk.Label(child_frame, text="SURNAME", borderwidth=2, relief="solid", width=15).grid(column=2, row=0, padx=2)
        ttk.Label(child_frame, text="DEPARTMENT", borderwidth=2, relief="solid", width=15).grid(column=3, row=0, padx=2)
        ttk.Label(child_frame, text="START DATE", borderwidth=2, relief="solid", width=15).grid(column=4, row=0, padx=2)

        e_id = ttk.Entry(child_frame, width=15)  #Putting the entry inside the frame for updating
        e_id.grid(row=1, column=0, padx=2, pady=15)

        e_first_name = ttk.Entry(child_frame, width=15)  #Putting the entry inside the frame for updating
        e_first_name.grid(row=1, column=1, padx=2, pady=15)

        e_last_name = ttk.Entry(child_frame, width=15)  #Putting the entry inside the frame for updating
        e_last_name.grid(row=1, column=2, padx=2, pady=15)

        e_department = ttk.Entry(child_frame, width=15)  #Putting the entry inside the frame for updating
        e_department.grid(row=1, column=3, padx=2, pady=15)

        e_start_date = ttk.Entry(child_frame, width=15)  #Putting the entry inside the frame for updating
        e_start_date.grid(row=1, column=4, padx=2, pady=15)

        def btn_submit():
            id = e_id.get()
            first_name = e_first_name.get()
            last_name = e_last_name.get()
            department = e_department.get()
            start_date = e_start_date.get()

            update_employee(id, first_name, last_name, department, start_date)


        btn_submit = ttk.Button(child_frame, text="Submit", command=btn_submit).grid(row=2, column=4, padx=15, pady=15)



    btn_1 = ttk.Button(parent_frame, text="Search", command=btn_search).grid(row=0, column=1, padx=15, pady=15)
    btn_2 = ttk.Button(parent_frame, text="Delete Employee", command=btn_delete).grid(row=0, column=4, padx=15, pady=15)
    btn_home = ttk.Button(parent_frame, text="HOME", command=button_home).grid(row=0, column=2, padx=15, pady=15)
    btn_update = ttk.Button(parent_frame, text="Update", command=button_update).grid(row=1, column=0, padx=15, pady=15)

    
    draw_emp(child_frame, employees)



def filter_by_department(dpt):
    result = []
    employees = read_csv(FILE_PATH)
    for employee in employees:
        if employee[3] == dpt:
            result.append(employee)

    return result    

def main():
        
    window = tkinter.Tk()  #Creating the window
    window.geometry("900x900")

    employees = read_csv(FILE_PATH)

    draw_frame(window, employees[1:10])

    window.mainloop()



main()

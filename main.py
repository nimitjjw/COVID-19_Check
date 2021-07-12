#Code

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import mysql.connector as m

conn = m.connect(user = 'python', password = 'nimitjjw', host='localhost', database = 'covidcheck')   # creating connection
cursor = conn.cursor() 

def insert():
    symlist = [] 
    if var1.get() == 1:
        symlist.append("Fever, Dry Cough, Tiredness")
        check1.deselect()
    if var2.get() == 1:
        symlist.append("Sore Throat")
        check2.deselect()
    if var3.get() == 1:
        symlist.append("Loss of taste or smell")
        check3.deselect()
    if var4.get() == 1:
        symlist.append("Difficulty breathing or shortness of breath")
        check4.deselect()
    if var5.get() == 1:
        symlist.append("Chest pain or pressure")
        check5.deselect()
    if var6.get() == 1:
        symlist.append("Loss of speech or movement")
        check6.deselect()
    if var0.get() == 1:
        gender = "Male"
        var0.set(0)
    if var0.get() == 2:
        gender = "Female"
        var0.set(0)
    if var0.get() == 3:
        gender = "Other"
        var0.set(0)

    sym = ', '.join(symlist)
    syminp = StringVar()
    syminp.set(sym)
    sex = StringVar()
    sex.set(gender)
    
    msg = f'ID: {identity.get()}\n\nName: {naam.get()}\n\nDOB: {day.get()}th {monthname.get()}, {year.get()}\n\nGender: {gender}\n\nSymtoms: {sym}'
    showinfo(
        title = f"{naam.get()}'s Details",
        message = msg
    )
    
    sqlformula = "INSERT INTO data(Id, Name, Gender, Day, Month, Year, Symptoms) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    info = (identity.get(), naam.get(), sex.get(), int(day.get()), monthname.get(), int(year.get()), syminp.get())
    cursor.execute(sqlformula, info)
    conn.commit()
    
    idval.delete(0, END)                  # Reset Entry widget
    nametxt.delete(0, END)
    day.set('')
    monthname.set('')
    year.set('')

    
def delete():
    if identity.get():
        sqlformula = "DELETE FROM data WHERE id = {}".format(identity.get())
        cursor.execute(sqlformula)
        conn.commit()
    
    if var1.get() == 1:
        check1.deselect()
    if var2.get() == 1:
        check2.deselect()
    if var3.get() == 1:
        check3.deselect()
    if var4.get() == 1:
        check4.deselect()
    if var5.get() == 1:
        check5.deselect()
    if var6.get() == 1:
        check6.deselect()
    if var0.get() == 1:
        var0.set(0)
    if var0.get() == 2:
        var0.set(0)
    if var0.get() == 3:
        var0.set(0)
    
    idval.delete(0, END)                  # Reset Entry widget
    nametxt.delete(0, END)
    day.set('')
    monthname.set('')
    year.set('')
    
    final = 'Record succesfully deleted!'
    showinfo(
        title = "Details Deleted",
        message = final      
    )

def display():
    msg = f"SELECT * FROM data WHERE id = {identity.get()}"
    cursor.execute(msg)
    final = cursor.fetchall()
    showinfo(
        title = "Details",
        message = final      
    )

root = tk.Tk()
root.title("COVID-19 Check")
root.geometry("800x550+10+20")

covid = tk.Label(text = "COVID-19 CHECK", font = ("Helvetica", 24))
covid.grid(row = 0, column = 0, columnspan = 4, padx = 250, pady = 30)

#===== NAME =====

emp = tk.Label(text = " ")
emp.grid(row = 1, column = 0, columnspan = 4, padx = 250)

name = tk.Label(text = "Name", font = ("Helvetica", 12))
name.grid(row = 3, column = 0, padx = 20, sticky = NW)

naam = StringVar()
nametxt = tk.Entry(root, bd = 3, textvariable = naam) 
nametxt.grid(row = 3, column = 1, padx = 15, ipadx = 30)

#===== ID =====

iden = tk.Label(text = "Id", font = ("Helvetica", 12))
iden.grid(row = 3, column = 2, padx = 50, sticky = NW)

identity = IntVar()
idval = tk.Entry(root, bd = 3, textvariable = identity) 
idval.grid(row = 3, column = 3, ipadx = 30)

#===== GENDER =====

gender = tk.Label(text = "Gender", font = ("Helvetica", 12))
gender.grid(row = 5, column = 0, padx = 20, sticky = NW, ipady = 50)

var0 = IntVar()
var0.set(0)

male = tk.Radiobutton(text = "Male", font = ("Helvetica", 12), variable = var0, value = 1)
male.grid(row = 5, column = 1, padx = 5)

female = tk.Radiobutton(text = "Female", font = ("Helvetica", 12), variable = var0, value = 2)
female.grid(row = 5, column = 2, padx = 5)

other = tk.Radiobutton(text = "Other", font = ("Helvetica", 12), variable = var0, value = 3)
other.grid(row = 5, column = 3, padx = 5)

#===== DOB =====

dob = tk.Label(text = "DOB", font = ("Helvetica", 12))
dob.grid(row = 7, column = 0, padx = 20, sticky = NW)

day = tk.IntVar()
daychoosen = ttk.Combobox(width = 20, textvariable = day)

dates = []

dates.append("Select the day")

for i in range(1, 32):
    dates.append(i)

daychoosen['values'] = dates
daychoosen.grid(row = 7, column = 1)
daychoosen.current(0)

monthname = tk.StringVar()
monthchoosen = ttk.Combobox(width = 20, textvariable = monthname)
  
# Adding combobox drop down list
monthchoosen['values'] = (' Select the month',' January',' February',' March',' April',' May',' June',' July',' August',
                          ' September',' October',' November',' December')
  
monthchoosen.grid(row = 7, column = 2)
monthchoosen.current(0)

year = tk.IntVar()
yearchoosen = ttk.Combobox(width = 20, textvariable = year)

years = []

years.append("Select the year")

for i in range(1900, 2022):
    years.append(i)

yearchoosen['values'] = years
yearchoosen.grid(row = 7, column = 3, padx = 40)
yearchoosen.current(0)

emp = tk.Label(text = " ")
emp.grid(row = 8, column = 0, columnspan = 4, padx = 250)

#===== SYMTOMS =====

symtoms = tk.Label(text = "Symtoms", font = ("Helvetica", 12))
symtoms.grid(row = 9, column = 0, padx = 20, sticky = NW, ipady = 10)

var1 = IntVar()
check1 = tk.Checkbutton(text = 'Fever, Dry Cough, Tiredness', variable = var1)
check1.grid(row = 9, column = 1)

var2 = IntVar()
check2 = tk.Checkbutton(root, text = 'Sore Throat', variable = var2)
check2.grid(row = 9, column = 2)

var3 = IntVar()
check3 = tk.Checkbutton(root, text = 'Loss of taste or smell', variable = var3)
check3.grid(row = 11, column = 1, sticky = NW, padx = 32)

var4 = IntVar()
check4 = tk.Checkbutton(text = 'Difficulty breathing or shortness of breath', variable = var4)
check4.grid(row = 11, column = 2, columnspan = 2, sticky = NW, padx = 37)

var5 = IntVar()
check5 = tk.Checkbutton(root, text = 'Chest pain or pressure', variable = var5)
check5.grid(row = 13, column = 1, pady = 10, sticky = NW, padx = 32)

var6 = IntVar()
check6 = tk.Checkbutton(root, text = 'Loss of speech or movement', variable = var6)
check6.grid(row = 13, column = 2, columnspan = 2, sticky = NW, padx = 37, pady = 10)

#===== DELETE =====

delete = tk.Button(text = "Delete", font = ("Helvetica", 12), bg = "#B80F0A", command = delete)
delete.grid(row = 15, column = 1, pady = 30, ipadx = 30, sticky = W)

#===== SUBMIT =====

submit = tk.Button(text = "Submit", font = ("Helvetica", 12), bg = "#03AC13", command = insert)
submit.grid(row = 15, column = 2, pady = 30, ipadx = 30, sticky = S, padx = 10)

#===== SHOW =====

show = tk.Button(text = "Show", font = ("Helvetica", 12), bg = "#3090C7", command = display)
show.grid(row = 15, column = 3, pady = 30, ipadx = 30, sticky = E, padx = 30)

root.mainloop()
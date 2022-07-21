# Main Menu
from tkinter import *
from tkinter import messagebox
from os import _exit
import login
import student_data
import book_catalog
import book_issue
import book_return

win=Tk()
frame=Frame(win)
frame.pack()
win.title("Library Management System")     #window title
win.geometry("500x500")
win.configure(bg="dark gray")

label=Label(win,text="LIBRARY MANAGEMENT SYSTEM",bg='light green',borderwidth=5,relief="raised",fg="dark green",font=('Century Schoolbook L',25,'bold'))   #window label
label.pack(expand=True)
bt1=Button(win,text="Administrator Menu",height=3,width=20,font=15,bd=5,command=login.login).pack(expand=True)

bt2=Button(win,text="Student Data",height=3,width=20,bd=5,font=15,command=student_data.stud_data).pack(expand=True)
bt3=Button(win,text="Book Catalog",height=3,width=20,font=15,bd=5,command=book_catalog.book_data).pack(expand=True)
bt4=Button(win,text="Book Issue",height=3,width=20,font=15,bd=5,command=book_issue.book_issue).pack(expand=True)
bt5=Button(win,text="Book Return",height=3,width=20,font=15,bd=5,command=book_return.book_return).pack(expand=True)

def close():
    prompt=messagebox.askquestion("Exit","Do you really want to quit")
    if prompt=='yes':
        _exit(0)          #function for exit command
bt6=Button(win,text="Exit",height=3,width=20,command=close,font=15,bd=5)

win.mainloop()







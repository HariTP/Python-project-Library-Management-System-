# Student Data
from tkinter import *
import tkinter as tk                                      ## Importing required modules
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk     ## for combobox
import mysql.connector
from os import _exit

def stud_data():                   ## Main function to be called in Main Menu
    win_ad=Tk()
    win_ad.title("Student Data")
    win_ad.configure(bg="light blue")
    win_ad.geometry('750x250+290+200')

    Label(win_ad,text="SEARCH STUDENT DATA",bg='light blue',borderwidth=5,relief="raised",fg="dark blue",font=('Century Schoolbook L',25,'bold')).place(x=180,y=10)

    db_change=mysql.connector.connect(host="localhost",password="mysql",user="root",database="library")   ## Connecting to mysql database
    cursor_db=db_change.cursor()
    Label(win_ad,text="Admission Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
    e1=Entry(win_ad,bg="white",bd=3,font=("Roboto",20))
    e1.place(x=350,y=90)
    e1.focus_set()
    def search_stud():
        if (e1.get()=="" or e1.get() is None):
            messagebox.showerror("","Empty value not accepted!!")
            win_ad.lift()
            e1.focus_set()
        else:                        
            adm=int(e1.get())         
            str1="select * from students where admno={}".format(adm)
            cursor_db.execute(str1)
            data=cursor_db.fetchall()
            if data==[]:
                messagebox.showerror("","No Record Found!!")
                win_ad.lift()
                win_ad.focus_force()
                e1.focus_set()
            else:
                win_dat=Tk()
                win_dat.title("Record")
                win_dat.configure(bg="light blue")
                win_dat.geometry('800x180+290+200')
                frm=Frame(win_dat)
                frm.pack(side=tk.LEFT,padx=20)
                tab=ttk.Treeview(frm,columns=(1,2,3,4),show="headings",height="1")
                tab.pack()
                tab.heading(1,text="Admission no")
                tab.heading(2,text="Name")
                tab.heading(3,text="Class")
                tab.heading(4,text="Books to Return")
                for i in data:
                    tab.insert('','end',values=i)
                bt3=Button(win_dat,text="Close",bd=3,bg="light green",width=8,height=1,command=win_dat.destroy).place(x=380,y=140)    

    bt1=Button(win_ad,text="OK",bd=3,bg="light green",width=8,height=2,command=search_stud).place(x=230,y=180)
    bt2=Button(win_ad,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_ad.destroy).place(x=430,y=180)
    win_ad.mainloop()
stud_data()
   

# Book issue
from tkinter import *           ## Importing required modules
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk     ## for combobox
import mysql.connector
from os import _exit

def book_issue():
    win_stud=Tk()
    win_stud.title("Book Issue")
    win_stud.configure(bg="light blue")
    win_stud.geometry('800x390+290+200')

    Label(win_stud,text="BOOK ISSUE",bg='light blue',borderwidth=5,relief="raised",fg="dark blue",font=('Century Schoolbook L',25,'bold')).place(x=200,y=10)

    db_change=mysql.connector.connect(host="localhost",password="mysql",user="root",database="library")   ## Connecting to mysql database
    cursor_db=db_change.cursor()

    Label(win_stud,text="Admission Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
    e1=Entry(win_stud,bg="white",bd=3,font=("Roboto",20))
    e1.place(x=350,y=90)
    Label(win_stud,text="Book No",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=150,y=150)
    e2=Entry(win_stud,bg="white",bd=3,font=("Roboto",20))
    e2.place(x=350,y=150)
    e1.focus_set()
    
    def issue():
        adm=int(e1.get())
        bookno=int(e2.get())    
        try:
            str1="select * from students where admno={}".format(adm)
            cursor_db.execute(str1)
            stud=cursor_db.fetchone()

            str2="select * from books where bookno={}".format(bookno)
            cursor_db.execute(str2)
            book=cursor_db.fetchone()
        except:
            messagebox.showerror("","Invalid entries!!")
            
        if (adm==None or adm=="") or (bookno==None or bookno==""):
            messagebox.showerror("","Empty value not accepted!!")
        elif stud[3]==1:
            messagebox.showerror("","Student already has a book!! \ New book cannot be issued!!")
        elif book[3]==1:
            messagebox.showerror("","Book already issued!!\Please select another book!!")
        else:
            str3="update students set status=1 where admno={}".format(adm)
            cursor_db.execute(str3)
            db_change.commit()
            
            str4="update books set status=1 where bookno={}".format(bookno)
            cursor_db.execute(str4)
            db_change.commit()

            str5="insert into studbook values({},{})".format((adm),(bookno))
            cursor_db.execute(str5)
            db_change.commit()
            messagebox.showinfo("","Book issued successfully!!")
            

    bt1=Button(win_stud,text="OK",bd=3,bg="light green",width=8,height=2,command=issue).place(x=230,y=290)
    bt2=Button(win_stud,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_stud.destroy).place(x=430,y=290)
    win_stud.mainloop()
book_issue()
    

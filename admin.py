# Administrator
from tkinter import *           ## Importing required modules
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk     ## for combobox
import mysql.connector
from os import _exit

def admin():                   ## Main function to be called in Main Menu
    win_ad=Tk()
    win_ad.title("Administrator settings")
    win_ad.configure(bg="light blue")
    win_ad.geometry('500x500')

    Label(win_ad,text="ADMINISTRATOR MENU",bg='light blue',borderwidth=5,relief="raised",fg="dark blue",font=('Century Schoolbook L',25,'bold')).place(x=450,y=10)

    db_change=mysql.connector.connect(host="localhost",password="mysql",user="root",database="library")   ## Connecting to mysql database
    cursor_db=db_change.cursor()

    def add_stud():              ## Function for adding students to mysql database
        win_stud=Tk()
        win_stud.title("Add Student")
        win_stud.configure(bg="light blue")
        win_stud.geometry('800x390+290+200')
        Label(win_stud,text="Addition of Student Data",bg='light blue',font=('Century Schoolbook L',25,'bold')).place(x=200,y=10)
        Label(win_stud,text="Admission Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
        e1=Entry(win_stud,bg="white",bd=3,font=("Roboto",20))
        e1.place(x=350,y=90)
        Label(win_stud,text="Name",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=150,y=150)
        e2=Entry(win_stud,bg="white",bd=3,font=("Roboto",20))
        e2.place(x=350,y=150)
        Label(win_stud,text="Class",bg="light blue",font=('Century Schoolbook L',20,'bold')).place(x=155,y=210)
        e3=ttk.Combobox(win_stud,width=17,font=('Arial',20),value=(11,12))
        e3.place(x=350,y=210)
        e1.focus_set()
        def add():
            if (e1.get()=="" or e1.get() is None) or (e2.get()=="" or e2.get() is None) or (e3.get()=="" or e3.get() is None):
                messagebox.showerror("","Empty value not accepted!!")
                win_ad.lift()
                win_stud.lift()
                win_stud.focus_force()
                e1.focus_set()
            else:
                try:                          ## To check if data type of entries are correct
                    adm=int(e1.get())         
                    cla=int(e3.get())
                    if (e1.get()=="" or e1.get() is None) or (e2.get()=="" or e2.get() is None) or (e3.get()=="" or e3.get() is None):
                        messagebox.showerror("","Empty value not accepted!!")
                        win_ad.lift()
                        win_stud.lift()
                        win_stud.focus_force()
                        e1.focus_set()
                    else:
                        str0="insert into students values({},'{}',{},0)".format(adm,e2.get(),cla)
                        cursor_db.execute(str0)
                        db_change.commit()
                        win_stud.destroy()
                        messagebox.showinfo("","Student data added successfully")
                except:                       ## Executes if data type is wrong
                     messagebox.showerror("","Wrong Data in fields!!")
                     win_ad.lift()
                     win_stud.lift()
                     win_stud.focus_force()
                     e1.focus_set()
        bt1=Button(win_stud,text="OK",bd=3,bg="light green",width=8,height=2,command=add).place(x=230,y=290)
        bt2=Button(win_stud,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_stud.destroy).place(x=430,y=290)
        win_stud.mainloop()
    ## Button calling function add_stud() below    
    bt1=Button(win_ad,text="Add Student",width=40,height=4,bd=5,highlightbackground='black',command=add_stud).place(x=500,y=80)  
    
    def del_stud():              ## Function for adding students to mysql database
        win_stud=Tk()
        win_stud.title("Delete Student")
        win_stud.configure(bg="light blue")
        win_stud.geometry('800x240+290+200')
        Label(win_stud,text="Deletion of Student Data",bg='light blue',font=('Century Schoolbook L',25,'bold')).place(x=200,y=10)
        Label(win_stud,text="Admission Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
        e1=Entry(win_stud,bg="white",bd=3,font=("Roboto",20))
        e1.place(x=350,y=90)
        e1.focus_set()
        def s_del():
            if (e1.get()=="" or e1.get() is None):
                messagebox.showerror("","Empty value not accepted!!")
                win_ad.lift()
                win_stud.lift()
                win_stud.focus_force()
                e1.focus_set()
            else:
                adm=int(e1.get())
                str0="delete from students where admno={}".format(adm)
                cursor_db.execute(str0)
                db_change.commit()
                win_stud.destroy()
                messagebox.showinfo("","Student deleted successfully")
        bt1=Button(win_stud,text="OK",bd=3,bg="light green",width=8,height=2,command=s_del).place(x=230,y=180)
        bt2=Button(win_stud,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_stud.destroy).place(x=430,y=180)
        win_stud.mainloop()
    bt2=Button(win_ad,text="Delete Student",width=40,height=4,bd=5,highlightbackground='black',command=del_stud).place(x=500,y=200)

    def add_book():              ## Function for adding students to mysql database
        win_book=Tk()
        win_book.title("Add Book")
        win_book.configure(bg="light blue")
        win_book.geometry('800x390+290+200')
        Label(win_book,text="Addition of Book Data",bg='light blue',font=('Century Schoolbook L',25,'bold')).place(x=200,y=10)
        Label(win_book,text="Book Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
        e1=Entry(win_book,bg="white",bd=3,font=("Roboto",20))
        e1.place(x=350,y=90)
        Label(win_book,text="Title",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=150,y=150)
        e2=Entry(win_book,bg="white",bd=3,font=("Roboto",20))
        e2.place(x=350,y=150)
        Label(win_book,text="Author",bg="light blue",font=('Century Schoolbook L',20,'bold')).place(x=155,y=210)
        e3=Entry(win_book,bg="white",bd=3,font=("Roboto",20))
        e3.place(x=350,y=210)
        e1.focus_set()
        def add():
             try:
                 book_no=int(e1.get())         
                 auth=e3.get()
                 str0="insert into books values({},'{}','{}',0)".format(book_no,e2.get(),auth)
                 cursor_db.execute(str0)
                 db_change.commit()
                 win_book.destroy()
                 messagebox.showinfo("","Book data added successfully")
             except:
                 messagebox.showerror("","Wrong Data in fields!!")
                 win_ad.lift()
                 win_book.lift()
                 win_book.focus_force()
                 e1.focus_set()
        bt1=Button(win_book,text="OK",bd=3,bg="light green",width=8,height=2,command=add).place(x=230,y=290)
        bt2=Button(win_book,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_book.destroy).place(x=430,y=290)
        win_book.mainloop()
    bt3=Button(win_ad,text="Add Book",width=40,height=4,bd=5,highlightbackground='black',command=add_book).place(x=500,y=320)

    def del_book():              ## Function for adding students to mysql database
        win_book=Tk()
        win_book.title("Delete Book")
        win_book.configure(bg="light blue")
        win_book.geometry('800x240+290+200')
        Label(win_book,text="Deletion of Book Data",bg='light blue',font=('Century Schoolbook L',25,'bold')).place(x=200,y=10)
        Label(win_book,text="Book Number",bg='light blue',font=('Century Schoolbook L',20,'bold')).place(x=50,y=90)
        e1=Entry(win_book,bg="white",bd=3,font=("Roboto",20))
        e1.place(x=350,y=90)
        e1.focus_set()
        def b_del():
             try:
                 book_no=int(e1.get())         
                 str0="delete from books where bookno={}".format(book_no)
                 cursor_db.execute(str0)
                 db_change.commit()
                 win_book.destroy()
                 messagebox.showinfo("","Book data deleted successfully")
             except:
                 messagebox.showerror("","Wrong Data in fields!!")
                 win_ad.lift()
                 win_book.lift()
                 win_book.focus_force()
                 e1.focus_set()
        bt1=Button(win_book,text="OK",bd=3,bg="light green",width=8,height=2,command=b_del).place(x=230,y=180)
        bt2=Button(win_book,text="Cancel",bd=3,bg="light green",width=8,height=2,command=win_book.destroy).place(x=430,y=180)
        win_book.mainloop()
    bt4=Button(win_ad,text="Delete Book",width=40,height=4,bd=5,highlightbackground='black',command=del_book).place(x=500,y=440)

    def pswd_ask():                     
        win_ch=Tk()
        win_ch.title("New Password")
        win_ch.geometry('500x100')
        win_ch.configure(bg="light gray")
        Label(win_ch,text="New Password",bg='light gray',font=("",15,'bold')).place(x=14,y=10)
        e1=Entry(win_ch,bg="light blue",bd=3,font=("Roboto",15))
        e1.place(x=200,y=10)
        def pass_change():
            if e1.get()=="" or e1.get() is None:
                messagebox.showerror("","Password cannot be empty")
                win_ad.lift()
                win_ch.destroy()
            else:
                str2="update auth set passwd='{}'".format(e1.get())
                cursor_db.execute(str2)
                db_change.commit()
                win_ch.destroy()
                messagebox.showinfo("","Password changed successfully!!!")
        bt1=Button(win_ch,text="OK",bd=3,bg="light green",width=8,command=pass_change).place(x=130,y=60)
        bt2=Button(win_ch,text="Cancel",width=8,bd=3,bg="light green",command=win_ch.destroy).place(x=230,y=60)
        win_ch.mainloop()
    bt5=Button(win_ad,text="Change Password",width=40,height=4,bd=5,highlightbackground='black',command=pswd_ask).place(x=500,y=560)    

    def close():
        _exit(0)
    bt6=Button(win_ad,text="Close",bg="light blue",width=20,height=2,bd=5,highlightbackground='black',command=close).place(x=200,y=600)   

    def back():
        win_ad.destroy()
    bt7=Button(win_ad,text="Log Out",bg="light blue",width=20,height=2,bd=5,highlightbackground='black',command=back).place(x=970,y=600)
    
    win_ad.mainloop()    
admin()

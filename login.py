# Login page for administrator
from tkinter import *
from tkinter import messagebox
import mysql.connector 
import admin
def login():
    db_log=mysql.connector.connect(host="localhost",user="root",password="mysql",database="library")   #accessing password stored table from mysql
    cursor_log=db_log.cursor()
    str1="select passwd from auth"
    cursor_log.execute(str1)
    passwd=cursor_log.fetchall()
    login_pass=passwd[0][0]

    win=Tk()                 #window styling
    win.title("Authentication")
    win.configure(bg="light gray")
    win.geometry('450x150')

    Label(win,text="Username",bg="light gray",font=("Roboto",15,'bold')).place(x=12,y=10)   #username and password fields
    Label(win,text="Password",bg='light gray',font=("Roboto",15,'bold')).place(x=14,y=50)
    e1=Entry(win,bg="light blue",bd=3,font=("Roboto",15))
    e1.place(x=150,y=10)
    e2=Entry(win,bg="light blue",bd=3,font=("Roboto",15),show='*')
    e2.place(x=150,y=50)
    def response():                                  
        if e1.get()=="admin" and e2.get()==login_pass:            #uname & pwd check
            win.destroy()
            admin.admin()                                         #entering admin module
        else:                            #incorrect password
            messagebox.showinfo("Error","Incorrect password or username")
            e1.delete(0,'end')
            e2.delete(0,'end')
            win.lift()
            win.focus_force()
            e1.focus_set()
    bt1=Button(win,text="Login",bd=3,bg="light green",width=8,command=response)   #exit and clear options
    bt1.place(x=130,y=100)

    def clear():
        e1.delete(0,'end')
        e2.delete(0,'end')
    bt2=Button(win,text="Clear",width=8,bd=3,bg="light green",command=clear)
    bt2.place(x=230,y=100)
    e1.focus_set()
login()

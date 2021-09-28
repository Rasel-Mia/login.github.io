from tkinter import *
from tkinter import messagebox
import mysql.connector

# ---------------------------------------------------------------Login Function --------------------------------------
def clear():
    emailentry.delete(0, END)
    passentry.delete(0, END)

def close():
    root.destroy()

def next():
    import signup
    signup

def login():
    if email.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter Email And Password", parent=root)
    else:
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="login")
            cur = con.cursor()

            cur.execute("select * from loginpage where email = %s and password = %s",
                        (email.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Email And Password", parent=root)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=root)
                root.destroy()          #Go next page or previous page.
                import crudoperation    #Go next page or previous page.
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=root)

# ------------------------------------------------------------ Login Window -----------------------------------------
root = Tk()
# app title
root.title("Login")
# window size
root.maxsize(width=500, height=500)
root.minsize(width=500, height=500)
# heading label
heading = Label(root, text="Login", font='Courier 20 bold')
heading.place(x=80, y=150)

email= Label(root, text="Email :", font='Courier 10 bold')
email.place(x=80, y=220)

userpass = Label(root, text="Password :", font='Courier 10 bold')
userpass.place(x=80, y=260)
# Entry Box
email = StringVar()
password = StringVar()

emailentry = Entry(root, width=40, textvariable=email)
emailentry.focus()
emailentry.place(x=200, y=223)

passentry = Entry(root, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)
# button login and clear
btn_login = Button(root, text="Login", font='Courier 10 bold', command=login)
btn_login.place(x=200, y=293)

btn_login = Button(root, text="Clear", font='Courier 10 bold', command=clear)
btn_login.place(x=260, y=293)
# signup button
sign_up_btn = Button(root, text="Sign up", command=next)
sign_up_btn.place(x=430, y=10) 

root.mainloop()

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------


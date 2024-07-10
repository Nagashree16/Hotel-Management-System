from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk   # for stylish entry fill we use ttk model
import random
from tkinter import StringVar
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagement


class LoginPage:
    def __init__(self,root):
        self.root=root

        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

#========================== BACKGROUND IMAGE ===============================
        imag1=Image.open(r"sen3.png")
        imag1=imag1.resize((1550,800),Image.LANCZOS)
        self.photoimag1=ImageTk.PhotoImage(imag1)

        lblimg=Label(self.root,image=self.photoimag1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)


# =========================================== FRAME =======================================

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

# ============================================ LOGIN IMG ===================================
        imag2=Image.open(r"loginlogo.png")
        imag2=imag2.resize((100,100),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(imag2)

        lblimg=Label(image=self.photoimag2,bg="black",borderwidth=0)
        lblimg.place(x=730,y=175,width=100,height=100)

# ============================ LABEL NAME ===================================================

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="red",bg="white")
        get_str.place(x=95,y=100)


# =============================== ENTRY FILL WITH LABEL ===================================================

        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="red",bg="white")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="red",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        imag3=Image.open(r"loginlogo1.png")
        imag3=imag3.resize((25,25),Image.LANCZOS)
        self.photoimag3=ImageTk.PhotoImage(imag3)

        lblimg1=Label(image=self.photoimag3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        imag4=Image.open(r"lock.png")
        imag4=imag4.resize((25,25),Image.LANCZOS)
        self.photoimag4=ImageTk.PhotoImage(imag4)

        lblimg2=Label(image=self.photoimag4,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=397,width=25,height=25)

        # ================================ LOGIN BUTTON =================================

        loginbtn=Button(frame,command=self.hotel_login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="white",activebackground="white")
        registerbtn.place(x=15,y=350,width=160)

        passwordbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="white",activebackground="white")
        passwordbtn.place(x=10,y=370,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!.....","all fields required")
        elif self.txtuser.get()=="Admin" and self.txtpass.get()=="hotel":
            messagebox.showinfo("Success","Welcome to Luxury Brand Hotel")
        else:
            messagebox.showerror("Error!..","Invalid username and password")



    def hotel_login(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelManagement(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=LoginPage(root)
    root.mainloop()

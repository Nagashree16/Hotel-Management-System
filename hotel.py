from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
class HotelManagement:
    def __init__(self,root):
        self.root=root

        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

    # ===================== HOTEL OUT LOOK IMAGE (1ST) ========================
        imag1=Image.open(r"boarder.png")
        imag1=imag1.resize((1550,140),Image.LANCZOS)
        self.photoimag1=ImageTk.PhotoImage(imag1)

        lblimg=Label(self.root,image=self.photoimag1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

    # ===================== LOHO (2ST) =========================================
        imag2=Image.open(r"logo2.png")
        imag2=imag2.resize((230,140),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(imag2)

        lblimg1=Label(self.root,image=self.photoimag2,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=230,height=140)

    # ========================TITLE =====================================
        lbl_title=Label(self.root,text="LUXURY BRAND HOTEL",font=("Times new Roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


    # ======================== MAIN FRAME ===============================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

    # ========================== MENU ====================================

        lbl_menu=Label(main_frame,text="MENU",font=("Times new Roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

    # ======================== BUTTON FRAME ===============================

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=42,width=228,height=190)

    
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("Times new Roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_details,width=22,font=("Times new Roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.room_add_details,width=22,font=("Times new Roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("Times new Roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,command=self.logout,text="LOGOUT",width=22,font=("Times new Roman",14,"bold"),bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        # ======================= RIGHT SIDE IMAGE =============================

        imag3=Image.open(r"reception.jpg")
        imag3=imag3.resize((1310,590),Image.LANCZOS)
        self.photoimag3=ImageTk.PhotoImage(imag3)

        lblimg2=Label(main_frame,image=self.photoimag3,bd=4,relief=RIDGE)
        lblimg2.place(x=225,y=0,width=1310,height=590)


        # ========================= DOWN IMG ============================================

        imag4=Image.open(r"building.png")
        imag4=imag4.resize((230,210),Image.LANCZOS)
        self.photoimag4=ImageTk.PhotoImage(imag4)

        lblimg4=Label(main_frame,image=self.photoimag4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=225,width=230,height=210)


        imag5=Image.open(r"food.png")
        imag5=imag5.resize((230,190),Image.LANCZOS)
        self.photoimag5=ImageTk.PhotoImage(imag5)

        lblimg5=Label(main_frame,image=self.photoimag5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_details(self):
        
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)
    def room_add_details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
    def logout(self):
        self.root.destroy()





















if __name__ == "__main__":
    root=Tk()
    obj=HotelManagement(root)
    root.mainloop()

    
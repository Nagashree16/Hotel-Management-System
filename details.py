from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk   # for stylish entry fill we use ttk model
import random
from tkinter import StringVar
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")
# ========================TITLE =====================================
        lbl_title=Label(self.root,text=" DETAILS",font=("Times new Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        imag2=Image.open(r"logo2.png")
        imag2=imag2.resize((230,140),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(imag2)

        lblimg1=Label(self.root,image=self.photoimag2,bd=0,relief=RIDGE)
        lblimg1.place(x=5,y=2,width=200,height=40)


# ======================== LABEL FRAME =========================================

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Adding Details",font=("arial",12,"bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=540,height=350)

# ======================== LABELS AND ENTRYS ======================================

        # Floor
        lbl_floor=Label(labelFrameleft,text="Floor : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelFrameleft,textvariable=self.var_floor,width=20,font=("times new roman",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room Number
        lbl_RoomNo=Label(labelFrameleft,text="Room NO : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelFrameleft,textvariable=self.var_RoomNo,width=20,font=("times new roman",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_RoomType=Label(labelFrameleft,text="Room Type : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelFrameleft,textvariable=self.var_RoomType,width=20,font=("times new roman",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

 #======================== BUTTON =================================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        
        btnAdd=Button(btn_frame,command=self.add_data,relief=RAISED,text="Add",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpd=Button(btn_frame,command=self.update,relief=RAISED,text="Update",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnUpd.grid(row=0,column=1,padx=1)

        btnDet=Button(btn_frame,command=self.delete,relief=RAISED,text="Delete",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnDet.grid(row=0,column=2,padx=1)

        btnRes=Button(btn_frame,command=self.reset,relief=RAISED,text="Re-Set",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnRes.grid(row=0,column=3,padx=1)

#================================= TABLE FRAME AND SEARCH =============================================
 
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=600,y=50,width=600,height=350)






        Scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.table_frame=ttk.Treeview(table_frame,column=("Floor","Room_no","Room_Type"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)

        # pack 

        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)

        Scrollbar_x.config(command=self.table_frame.xview)
        Scrollbar_y.config(command=self.table_frame.yview)

        self.table_frame.heading("Floor",text="Floor")
        self.table_frame.heading("Room_no",text="Room no")
        self.table_frame.heading("Room_Type",text="RoomType")
        
        

        self.table_frame["show"]="headings"
        self.table_frame.column("Floor",width=100)
        self.table_frame.column("Room_no",width=100)
        self.table_frame.column("Room_Type",width=100)

        
        
        self.table_frame.pack(fill=BOTH,expand=1)
        self.table_frame.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

# ================================================ ADDING THE DATA ============================================================================
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get() =="":
                messagebox.showerror("Error!...","All fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into details(Floor,RoomNo,RoomType) values(%s,%s,%s)",(self.var_floor.get(),
                                                                                                   self.var_RoomNo.get(),
                                                                                                   self.var_RoomType.get()
                                                                                                  
                                                                                                  ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                except Exception as err:
                      messagebox.showwarning("Warning!...",f"Some Thing went wrong:{str(err)}",parent=self.root)

# =========================================update===========================================
    def update(self):
                if self.var_floor.get()=="":
                        messagebox.showerror("Error!..","Please enter floor number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                        self.var_floor.get(),
                                                                                                        self.var_RoomType.get(),
                                                                                                        self.var_RoomNo.get(),
                                                                                                                                                        
                                                                                                     ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","New Room Details Updated successfully",parent=self.root)
# ========================================DELETE ===============================================
    def delete(self):
           delete=messagebox.askyesno("Permission","Do You want to delete this room?",parent=self.root)
           if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                  my_cursor=conn.cursor()
                  query="delete from details where RoomNo=%s"
                  value=(self.var_RoomNo.get(),)

                  my_cursor.execute(query,value)
           else:
                  if not delete:
                         return
           conn.commit()
           self.fetch_data()
           conn.close()  
# ======================================== RESET ===============================================
    def reset(self):
                self.var_floor.set("")
                self.var_RoomNo.set("")
                self.var_RoomType.set("")
#========================================= Fetch data==========================================

    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from details")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                      self.table_frame.delete(*self.table_frame.get_children())
                      for i in rows:
                            self.table_frame.insert("",END,values=i)
                      conn.commit()
                conn.close()

# get cursor
    def get_cursor(self,event=""):
                cursor_row=self.table_frame.focus()
                content=self.table_frame.item(cursor_row)
                row=content["values"]
                self.var_floor.set(row[0])
                self.var_RoomNo.set(row[1])
                self.var_RoomType.set(row[2])
                








if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
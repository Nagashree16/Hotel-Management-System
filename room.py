from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk   # for stylish entry fill we use ttk model
import random
from tkinter import StringVar
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")
#  ============================= Variables ==========================
        self.var_contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofromm=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

# ========================TITLE =====================================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Times new Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        imag2=Image.open(r"logo2.png")
        imag2=imag2.resize((230,140),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(imag2)

        lblimg1=Label(self.root,image=self.photoimag2,bd=0,relief=RIDGE)
        lblimg1.place(x=5,y=2,width=200,height=40)

# ======================== LABEL FRAME =========================================

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("arial",12,"bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

# ======================== LABELS AND ENTRYS ======================================

        # customer reference
        lbl_cust_contact=Label(labelFrameleft,text="Customer Contact   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)


        entry_contact=ttk.Entry(labelFrameleft,textvariable=self.var_contact,width=20,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # Fetch Button

        btnFetchData=Button(labelFrameleft,command=self.Fetch_contact,relief=RAISED,text="Fetch Data",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=8)
        btnFetchData.place(x=335,y=4)
        # check in details
        check_in_date=Label(labelFrameleft,text="Check_in Date   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)


        entry_check_in=ttk.Entry(labelFrameleft,textvariable=self.var_check_in,width=26,font=("times new roman",13,"bold"))
        entry_check_in.grid(row=1,column=1)

        # check out details
        check_out_date=Label(labelFrameleft,text="Check_out Date   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)


        entry_check_out=ttk.Entry(labelFrameleft,textvariable=self.var_check_out,width=26,font=("times new roman",13,"bold"))
        entry_check_out.grid(row=2,column=1)


        # Room Type
        room_type=Label(labelFrameleft,text="Room Type   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)
        # conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
        # self.var_roomselected=StringVar()
        # room_num=self.var_roomavailable.get()
        # my_cursor=conn.cursor()
        # my_cursor.execute(f"select RoomType from details where RoomNo Like '%{room_num}%'")
        # id=my_cursor.fetchone()
        # print(id)
        
        # if id:
        #        room_type_value=id[0]
        # else:
        #        room_type_value=""
        # combo_room=ttk.Combobox(labelFrameleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=27,state="read only") 
        # combo_room["value"]=id
        # combo_room.current(0)
        # combo_room.grid(row=3,column=1)
        self.combo_room = ttk.Combobox(labelFrameleft, textvariable=self.var_roomtype, font=("times new roman", 12, "bold"), width=27, state="readonly")
        self.combo_room.grid(row=3, column=1)

        # room available
        room_available=Label(labelFrameleft,text="Available Room   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        room_available.grid(row=4,column=0,sticky=W)


        # entry_room_ava=ttk.Entry(labelFrameleft,textvariable=self.var_roomavailable,width=26,font=("times new roman",13,"bold"))
        # entry_room_ava.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details where status='available'")
        rows=my_cursor.fetchall()
        combo_roomavailable=ttk.Combobox(labelFrameleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=27,state="read only") 
        combo_roomavailable["value"]=rows
        combo_roomavailable.current(0)
        combo_roomavailable.grid(row=4,column=1)
        combo_roomavailable.bind("<<ComboboxSelected>>", self.update_room_type)
        # Meals
        meals=Label(labelFrameleft,text="Meals   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        meals.grid(row=5,column=0,sticky=W)


        # entry_meals=ttk.Entry(labelFrameleft,textvariable=self.var_meal,width=26,font=("times new roman",13,"bold"))
        # entry_meals.grid(row=5,column=1)
        combo_meal=ttk.Combobox(labelFrameleft,textvariable=self.var_meal,font=("times new roman",12,"bold"),width=27,state="read only") 
        combo_meal["value"]=("Breakfast","Lunch","Dinner","No Food Required","All time")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)


        # No of Days
        days=Label(labelFrameleft,text="No of Days   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        days.grid(row=6,column=0,sticky=W)


        entry_days=ttk.Entry(labelFrameleft,textvariable=self.var_noofromm,width=26,font=("times new roman",13,"bold"))
        entry_days.grid(row=6,column=1)

        # Paid Tax
        paid_tax=Label(labelFrameleft,text="Paid Tax   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        paid_tax.grid(row=7,column=0,sticky=W)


        entry_pd_tax=ttk.Entry(labelFrameleft,textvariable=self.var_paidtax,width=26,font=("times new roman",13,"bold"))
        entry_pd_tax.grid(row=7,column=1)

        # Sub Tax
        sub_tax=Label(labelFrameleft,text="Sub Tax   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        sub_tax.grid(row=8,column=0,sticky=W)


        entry_sub_tax=ttk.Entry(labelFrameleft,textvariable=self.var_actualtotal,width=26,font=("times new roman",13,"bold"))
        entry_sub_tax.grid(row=8,column=1)

         # Total Tax
        tot_tax=Label(labelFrameleft,text="Total Tax   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        tot_tax.grid(row=9,column=0,sticky=W)


        entry_tot_tax=ttk.Entry(labelFrameleft,textvariable=self.var_total,width=26,font=("times new roman",13,"bold"))
        entry_tot_tax.grid(row=9,column=1)


# ======================== BILL BUTTON ============================
        btnbill=Button(labelFrameleft,command=self.total,relief=RAISED,text="Bill",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)


# ======================== BUTTON =================================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        
        btnAdd=Button(btn_frame,command=self.add_data,relief=RAISED,text="Add",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpd=Button(btn_frame,command=self.update,relief=RAISED,text="Update",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnUpd.grid(row=0,column=1,padx=1)

        btnDet=Button(btn_frame,command=self.delete,relief=RAISED,text="Delete",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnDet.grid(row=0,column=2,padx=1)

        btnRes=Button(btn_frame,command=self.reset,relief=RAISED,text="Re-Set",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnRes.grid(row=0,column=3,padx=1)

# ================================ Right Side Image=====================================================
        imag3=Image.open(r"D:\HOTEL MANAGEMENT\Bed.png")
        imag3=imag3.resize((380,300),Image.LANCZOS)
        self.photoimag3=ImageTk.PhotoImage(imag3)

        lblimg1=Label(self.root,image=self.photoimag3,bd=0,relief=RIDGE)
        lblimg1.place(x=900,y=55,width=380,height=300)

#================================= TABLE FRAME AND SEARCH =============================================
 
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=280,width=850,height=260)

        labsearchby=Label(table_frame,text="Search by ",font=("times new roman",12,"bold"),bg='red',fg='white')
        labsearchby.grid(row=0,column=0,sticky=W,padx=3)

        self.search_var=StringVar()

        combo_sea=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=20,state="readonly") 
        combo_sea["value"]=("Contact","Room")
        combo_sea.current(0)
        combo_sea.grid(row=0,column=1,padx=3)

        self.txt_search=StringVar()
        entry_sea=ttk.Entry(table_frame,textvariable=self.txt_search,width=26,font=("times new roman",13,"bold"))
        entry_sea.grid(row=0,column=2,padx=3)

        btnsea=Button(table_frame,command=self.search,relief=RAISED,text="Search",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnsea.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,command=self.fetch_data,relief=RAISED,text="Show all",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnshowall.grid(row=0,column=4,padx=1)

# =============================== SHOW DATA TABLE ==============================================

        details_table=LabelFrame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("Contact","Check_in_Date","Check_out_Date","Room_Type","Room_available","Meal","NoOfDays"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)

        # pack 

        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)

        Scrollbar_x.config(command=self.room_table.xview)
        Scrollbar_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("Check_in_Date",text="Chech-in")
        self.room_table.heading("Check_out_Date",text="Check-out")
        self.room_table.heading("Room_Type",text="Room Type")
        self.room_table.heading("Room_available",text="Room available")
        self.room_table.heading("Meal",text="Meals")
        self.room_table.heading("NoOfDays",text="No Of Days")
        

        self.room_table["show"]="headings"
        self.room_table.column("Contact",width=100)
        self.room_table.column("Check_in_Date",width=100)
        self.room_table.column("Check_out_Date",width=100)
        self.room_table.column("Room_Type",width=100)
        self.room_table.column("Room_available",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("NoOfDays",width=100)
        
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

# ================================================ ADDING THE DATA ============================================================================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_check_in.get() =="":
                messagebox.showerror("Error!...","All fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                                   self.var_check_in.get(),
                                                                                                   self.var_check_out.get(),
                                                                                                   self.var_roomtype.get(),
                                                                                                   self.var_roomavailable.get(),
                                                                                                   self.var_meal.get(),
                                                                                                   self.var_noofromm.get()
                                                                                                  ))
                        room_no=self.var_roomavailable.get()
                        my_cursor.execute(f"update details set status='not available' where RoomNo LIKE '%{room_no}%'")
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Room Booked Successfully",parent=self.root)
                except Exception as err:
                      messagebox.showwarning("Warning!...","This Room is Already Booked",parent=self.root)
#========================================= Fetch data==========================================

    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from room")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                      self.room_table.delete(*self.room_table.get_children())
                      for i in rows:
                            self.room_table.insert("",END,values=i)
                      conn.commit()
                conn.close()


# get cursor
    def get_cursor(self,event=""):
                cursor_row=self.room_table.focus()
                content=self.room_table.item(cursor_row)
                row=content["values"]
                self.var_contact.set(row[0])
                self.var_check_in.set(row[1])
                self.var_check_out.set(row[2])
                self.var_roomtype.set(row[3])
                self.var_roomavailable.set(row[4])
                self.var_meal.set(row[5])
                self.var_noofromm.set(row[6])
# =========================================update===========================================
    def update(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error!..","Please enter mobile number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update room set check_in=%s,check_out=%s,room_type=%s,room_available=%s,meal=%s,no_of_days=%s where Contact=%s",(
                                                                                                                                                        self.var_check_in.get(),
                                                                                                                                                        self.var_check_out.get(),
                                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                                        self.var_meal.get(),
                                                                                                                                                        self.var_noofromm.get(),
                                                                                                                                                        self.var_contact.get()
                                                                                                                                                         ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Room Details Updated successfully",parent=self.root)
# ========================================DELETE ===============================================
    def delete(self):
           delete=messagebox.askyesno("Permission","Do You want to delete this customer room?",parent=self.root)
           if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                  my_cursor=conn.cursor()
                  query="delete from room where Contact=%s"
                  value=(self.var_contact.get(),)

                  my_cursor.execute(query,value)
                  room_no=self.var_roomavailable.get()
                  my_cursor.execute(f"update details set status='available' where RoomNo LIKE '%{room_no}%'")
           else:
                  if not delete:
                         return
           conn.commit()
           self.fetch_data()
           conn.close()          
# ======================================== RESET ===============================================
    def reset(self):
                self.var_contact.set("")
                self.var_check_in.set("")
                self.var_check_out.set("")
                #self.var_roomtype.set("")
                #self.var_roomavailable.set("")
                #self.var_meal.set("")
                self.var_noofromm.set("")
                self.var_paidtax.set("")
                self.var_actualtotal.set("")
                self.var_total.set("")


# ========================================= TIME DATE AND NO OF DAYS CALCULATION ================
    def total(self):
           inDate=self.var_check_in.get()
           outDate=self.var_check_out.get()
           inDate=datetime.strptime(inDate,"%d/%m/%Y")
           outDate=datetime.strptime(outDate,"%d/%m/%Y")
           self.var_noofromm.set(abs(outDate-inDate).days)

           if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
                  q1=float(300)
                  q2=float(700)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
                  q1=float(350)
                  q2=float(700)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                  q1=float(400)
                  q2=float(700)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
                  q1=float(300)
                  q2=float(500)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                  q1=float(350)
                  q2=float(500)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                  q1=float(400)
                  q2=float(500)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
                  q1=float(300)
                  q2=float(600)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
                  q1=float(350)
                  q2=float(600)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                  q1=float(400)
                  q2=float(600)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
       
           elif(self.var_meal.get()=="No Food Required" and self.var_roomtype.get()=="Double"):
                  q2=float(600)
                  q3=float(self.var_noofromm.get())
                  q5=float(q3*q2)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="No Food Required" and self.var_roomtype.get()=="Single"):
                  q2=float(500)
                  q3=float(self.var_noofromm.get())
                  q5=float(q3*q2)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="No Food Required" and self.var_roomtype.get()=="Luxury"):
                  q2=float(700)
                  q3=float(self.var_noofromm.get())
                  q5=float(q3*q2)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="All time" and self.var_roomtype.get()=="Luxury"):
                  q1=float(1500)
                  q2=float(700)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="All time" and self.var_roomtype.get()=="Single"):
                  q1=float(1500)
                  q2=float(500)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)
           elif(self.var_meal.get()=="All time" and self.var_roomtype.get()=="Double"):
                  q1=float(1500)
                  q2=float(600)
                  q3=float(self.var_noofromm.get())
                  q4=float(q1+q2)
                  q5=float(q3*q4)
                  Tax="Rs."+str("%.2f"%((q5)*0.2))
                  ST="Rs."+str("%.2f"%((q5)))
                  TOT="Rs."+str("%.2f"%(q5+(q5)*0.2))
                  self.var_paidtax.set(Tax)
                  self.var_actualtotal.set(ST)
                  self.var_total.set(TOT)








# ======================================== ALL DATA FETCH ======================================
    def Fetch_contact(self):
        if self.var_contact.get()=="" :
            messagebox.showerror("Error!...","Please enter Contact Number",parent=self.root)
        else :
            conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
            my_cursor=conn.cursor()
            queury=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(queury,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error!..","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()


                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=455,y=55,width=300,height=200)

                lblName=Label(showDataFrame,text="Name:",font=("Times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                queury=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(queury,value)
                row=my_cursor.fetchone()


                lblGen=Label(showDataFrame,text="Gender:",font=("Times new roman",12,"bold"))
                lblGen.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)


                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                queury=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(queury,value)
                row=my_cursor.fetchone()


                lbleam=Label(showDataFrame,text="Email:",font=("Times new roman",12,"bold"))
                lbleam.place(x=0,y=60)

                lbl3=Label(showDataFrame,text=row,font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                queury=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(queury,value)
                row=my_cursor.fetchone()


                lblnat=Label(showDataFrame,text="Natinality:",font=("Times new roman",12,"bold"))
                lblnat.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                queury=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(queury,value)
                row=my_cursor.fetchone()


                lbladd=Label(showDataFrame,text="Address:",font=("Times new roman",12,"bold"))
                lbladd.place(x=0,y=120)

                lbl5=Label(showDataFrame,text=row,font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)


# ====================================================== SEARCH ======================================================
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Naga@123", database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.txt_search.get()

        if search_field == "Contact":
                query = f"SELECT * FROM room WHERE Contact LIKE '%{search_value}%'"
        elif search_field == "Room":
                query = f"SELECT * FROM room WHERE room_available LIKE '%{search_value}%'"
        else:
                messagebox.showerror("Error", "Invalid search option selected")
                return

        my_cursor.execute(query)
        rows = my_cursor.fetchall()

        if rows:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                        self.room_table.insert("", END, values=row)
                conn.commit()
        else:
                messagebox.showinfo("Info", "No records found")

        conn.close()
    def update_room_type(self, event):
        room_num = self.var_roomavailable.get()

        # Connect to the database
        conn = mysql.connector.connect(host="localhost", username="root", password="Naga@123", database="hotel_management")
        my_cursor = conn.cursor()

        # Execute the query
        my_cursor.execute(f"SELECT RoomType FROM details WHERE RoomNo LIKE '%{room_num}%'")
        id = my_cursor.fetchone()

        # Update the room type Combobox
        if id:
            room_type_value = id[0]
            self.combo_room["values"] = [room_type_value]
            self.combo_room.current(0)
        else:
            self.combo_room["values"] = ["Unknown"]
            self.combo_room.current(0)

        # Close the cursor and connection
        my_cursor.close()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
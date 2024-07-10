from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk   # for stylish entry fill we use ttk model
import random
from tkinter import StringVar
import mysql.connector
from tkinter import messagebox




class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")


# ======================== VARIABLES ================================

        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set((str(x)))

        self.var_cus_name=StringVar()
        self.var_mother_name=StringVar()
        self.var_gender=StringVar()
        self.var_cus_post=StringVar()
        self.var_cus_mobile=StringVar()       
        self.var_cus_email=StringVar()
        self.var_cus_nationality=StringVar()
        self.var_cus_address=StringVar()
        self.var_cus_idproff=StringVar()
        self.var_cus_Id_num=StringVar()

# ========================TITLE =====================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Times new Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        imag2=Image.open(r"logo2.png")
        imag2=imag2.resize((230,140),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(imag2)

        lblimg1=Label(self.root,image=self.photoimag2,bd=0,relief=RIDGE)
        lblimg1.place(x=5,y=2,width=200,height=40)


# ======================== LABEL FRAME =========================================

        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        labelFrameleft.place(x=5,y=50,width=425,height=490)

# ======================== LABELS AND ENTRYS ======================================

        # customer reference
        lbl_cust_ref=Label(labelFrameleft,text="Customer Reference   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


        entry_ref=ttk.Entry(labelFrameleft,textvariable=self.var_ref,width=26,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # customer name

        lbl_cust_name=Label(labelFrameleft,text="Customer Name         :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)


        entry_name=ttk.Entry(labelFrameleft,textvariable=self.var_cus_name,width=26,font=("times new roman",13,"bold"))
        entry_name.grid(row=1,column=1)

        # mother Name
 
        mname=Label(labelFrameleft,text="Mother Name             :",font=("times new roman",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)

        entry_mname=ttk.Entry(labelFrameleft,textvariable=self.var_mother_name,width=26,font=("times new roman",13,"bold"))
        entry_mname.grid(row=2,column=1)


        # Gender

        gen=Label(labelFrameleft,text="Gender                        :",font=("times new roman",12,"bold"),padx=2,pady=6)
        gen.grid(row=3,column=0,sticky=W)

        combo_gen=ttk.Combobox(labelFrameleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=27,state="read only") 
        #  IN TE ABOVE CODE IF WE DONT USE THE STATE THEN WE CAN EVEN CHOOSE TO WRITE AND ALSO WE CAN CHOOSE THE OPTION BY MENTIONED IN COMBO BOX
        #  IF WE USE STATE='READ ONLY' MODE THEN WE CAN ONLY HAVE THE OPTION TO CHOOSE FROM THE OPTION MENTIONED IN COMBO BOX WE CANNOT WRITE TO IT
        combo_gen["value"]=("Male","Female","Other")
        combo_gen.current(0)
        combo_gen.grid(row=3,column=1)

        # PostCode

        pos=Label(labelFrameleft,text="Post Code                   :",font=("times new roman",12,"bold"),padx=2,pady=6)
        pos.grid(row=4,column=0,sticky=W)

        entry_pos=ttk.Entry(labelFrameleft,textvariable=self.var_cus_post,width=26,font=("times new roman",13,"bold"))
        entry_pos.grid(row=4,column=1)


        # mobile number

        mob=Label(labelFrameleft,text="Mobile Number          :",font=("times new roman",12,"bold"),padx=2,pady=6)
        mob.grid(row=5,column=0,sticky=W)

        entry_mob=ttk.Entry(labelFrameleft,textvariable=self.var_cus_mobile,width=26,font=("times new roman",13,"bold"))
        entry_mob.grid(row=5,column=1)


        # Email

        eam=Label(labelFrameleft,text="Email                           :",font=("times new roman",12,"bold"),padx=2,pady=6)
        eam.grid(row=6,column=0,sticky=W)

        entry_eam=ttk.Entry(labelFrameleft,textvariable=self.var_cus_email,width=26,font=("times new roman",13,"bold"))
        entry_eam.grid(row=6,column=1)


        # Nationality

        nat=Label(labelFrameleft,text="Nationality                  :",font=("times new roman",12,"bold"),padx=2,pady=6)
        nat.grid(row=7,column=0,sticky=W)

        combo_nat=ttk.Combobox(labelFrameleft,textvariable=self.var_cus_nationality,font=("times new roman",12,"bold"),width=27,state="read only") 
        combo_nat["value"]=("India","Sri Lanka","USA","Russia","Japan","South Africa")
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)

        #ID proof type Combobox

        id=Label(labelFrameleft,text="ID Proof Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        id.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelFrameleft,textvariable=self.var_cus_idproff,font=("times new roman",12,"bold"),width=27,state="read only") 
        combo_id["value"]=("Aadhar","PAN","Voter ID","PassPort")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # ID Number

        Id_num=Label(labelFrameleft,text="ID Number                 :",font=("times new roman",12,"bold"),padx=2,pady=6)
        Id_num.grid(row=9,column=0,sticky=W)

        entry_num=ttk.Entry(labelFrameleft,textvariable=self.var_cus_Id_num,width=26,font=("times new roman",13,"bold"))
        entry_num.grid(row=9,column=1)

        # Address

        add=Label(labelFrameleft,text="Addresss                     :",font=("times new roman",12,"bold"),padx=2,pady=6)
        add.grid(row=10,column=0,sticky=W)

        entry_add=ttk.Entry(labelFrameleft,textvariable=self.var_cus_address,width=26,font=("times new roman",13,"bold"))
        entry_add.grid(row=10,column=1)

# ======================== BUTTON =================================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        
        btnAdd=Button(btn_frame,relief=RAISED,command=self.add_data,text="Add",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpd=Button(btn_frame,relief=RAISED,command=self.update,text="Update",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnUpd.grid(row=0,column=1,padx=1)

        btnDet=Button(btn_frame,relief=RAISED,command=self.delete,text="Delete",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnDet.grid(row=0,column=2,padx=1)

        btnRes=Button(btn_frame,relief=RAISED,command=self.reset,text="Re-Set",font=("Times new roman",12,"bold"),bg='black',fg='gold',width=10)
        btnRes.grid(row=0,column=3,padx=1)


# ================================= TABLE FRAME AND SEARCH =============================================
 
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=850,height=490)

        labsearchby=Label(table_frame,text="Search by ",font=("times new roman",12,"bold"),bg='red',fg='white')
        labsearchby.grid(row=0,column=0,sticky=W,padx=3)

        self.search_var=StringVar()

        combo_sea=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=20,state="readonly") 
        combo_sea["value"]=("Mobile Number","Reference ID")
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
        details_table.place(x=0,y=50,width=850,height=350)

        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("Ref","Name","Mother","Gender","Post","Mobile","Email","Nationality","IDNumber","Address"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)

        # pack 

        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)

        Scrollbar_x.config(command=self.Cust_Details_Table.xview)
        Scrollbar_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text="Refer No")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("Mother",text="Mother Name")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Post",text="Post Code")
        self.Cust_Details_Table.heading("Mobile",text="Mobile Number")
        self.Cust_Details_Table.heading("Email",text="Email")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("IDNumber",text="ID Number")
        self.Cust_Details_Table.heading("Address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Mother",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Post",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("Email",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("IDNumber",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cus_mobile.get()=="" or self.var_mother_name.get() =="":
                messagebox.showerror("Error!...","All fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                   self.var_cus_name.get(),
                                                                                                   self.var_mother_name.get(),
                                                                                                   self.var_gender.get(),
                                                                                                   self.var_cus_post.get(),
                                                                                                   self.var_cus_mobile.get(),
                                                                                                   self.var_cus_email.get(),
                                                                                                   self.var_cus_nationality.get(),
                                                                                                   self.var_cus_idproff.get(),
                                                                                                   self.var_cus_Id_num.get(),
                                                                                                   self.var_cus_address.get()
                                                                                                  ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Customer has been added",parent=self.root)
                except Exception as err:
                      messagebox.showwarning("Warning!...",f"Some Thing went wrong:{str(err)}",parent=self.root)
    
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from customer")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                      self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                      for i in rows:
                            self.Cust_Details_Table.insert("",END,values=i)
                      conn.commit()
                conn.close()

    def get_cursor(self,event=""):
                cursor_row=self.Cust_Details_Table.focus()
                content=self.Cust_Details_Table.item(cursor_row)
                row=content["values"]
                self.var_ref.set(row[0])
                self.var_cus_name.set(row[1])
                self.var_mother_name.set(row[2])
                self.var_gender.set(row[3])
                self.var_cus_post.set(row[4])
                self.var_cus_mobile.set(row[5])
                self.var_cus_email.set(row[6])
                self.var_cus_nationality.set(row[7])
                self.var_cus_idproff.set(row[8])
                self.var_cus_Id_num.set(row[9])
                self.var_cus_address.set(row[10])
    
    
    
    def update(self):
                if self.var_cus_mobile.get()=="":
                        messagebox.showerror("Error!..","Please enter mobile number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IDProof=%s,IDNumber=%s,Address=%s where Reference=%s",(
                                                                                                                                                                                                 self.var_cus_name.get(),
                                                                                                                                                                                                 self.var_mother_name.get(),
                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                 self.var_cus_post.get(),
                                                                                                                                                                                                 self.var_cus_mobile.get(),
                                                                                                                                                                                                 self.var_cus_email.get(),
                                                                                                                                                                                                 self.var_cus_nationality.get(),
                                                                                                                                                                                                 self.var_cus_idproff.get(),
                                                                                                                                                                                                 self.var_cus_Id_num.get(),
                                                                                                                                                                                                 self.var_cus_address.get(),
                                                                                                                                                                                                 self.var_ref.get()
                                                                                                                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Customer Details has been Updated Successfully",parent=self.root)
                     
    def delete(self):
           delete=messagebox.askyesno("Permission","Do You want to delete this customer",parent=self.root)
           if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="Naga@123",database="hotel_management")
                  my_cursor=conn.cursor()
                  query="delete from customer where Reference=%s"
                  value=(self.var_ref.get(),)

                  my_cursor.execute(query,value)
           else:
                  if not delete:
                         return
           conn.commit()
           self.fetch_data()
           conn.close()
    
    def reset(self):
                #self.var_ref.set("")
                self.var_cus_name.set("")
                self.var_mother_name.set("")
                #self.var_gender.set("")
                self.var_cus_post.set("")
                self.var_cus_mobile.set("")
                self.var_cus_email.set("")
                #self.var_cus_nationality.set("")
                #self.var_cus_idproff.set("")
                self.var_cus_Id_num.set("")
                self.var_cus_address.set("")

                x=random.randint(1000,10000)
                self.var_ref.set((str(x)))
    
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Naga@123", database="hotel_management")
        my_cursor = conn.cursor()

        search_field = self.search_var.get()
        search_value = self.txt_search.get()

        if search_field == "Mobile Number":
                query = f"SELECT * FROM customer WHERE Mobile LIKE '%{search_value}%'"
        elif search_field == "Reference ID":
                query = f"SELECT * FROM customer WHERE Reference LIKE '%{search_value}%'"
        else:
                messagebox.showerror("Error", "Invalid search option selected")
                return

        my_cursor.execute(query)
        rows = my_cursor.fetchall()

        if rows:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for row in rows:
                        self.Cust_Details_Table.insert("", END, values=row)
                conn.commit()
        else:
                messagebox.showinfo("Info", "No records found")

        conn.close()
     

                                    




if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
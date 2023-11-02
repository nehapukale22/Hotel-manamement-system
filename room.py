from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1055x450+230+220")

        #================variables=================
        self.var_conatct=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1055,height=50) 
        
        #----------------Logo-----------#
        img2=Image.open(r"D:\nehapro\himages\logohotel.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #----------------Label Frame---------------#
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=5,y=50,width=360,height=380)
        #----------------Labels and Entry-----------#
        lbl_cust_contact=Label(labelFrameleft,text="Customer contact:",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelFrameleft,width=13,textvariable=self.var_conatct,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)
        #fetch data button
        btnfetchdata=Button(labelFrameleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnfetchdata.place(x=275,y=3.5)
         #Check in date
        check_in_date=Label(labelFrameleft,text="Check_In Date:",font=("arial",12,"bold"),padx=2,pady=3)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_checkin,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        #check out date
        lbl_check_out=Label(labelFrameleft,text="Check_Out Date",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txt_check_out.grid(row=2,column=1)
        #Room Type
        label_RoomType=Label(labelFrameleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=3)
        label_RoomType.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        combo_RoomType=ttk.Combobox(labelFrameleft,textvariable=self.var_roomtype,font=("arial",13,"bold"),width=20,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(labelFrameleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=3)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        # txtRoomAvailable=ttk.Entry(labelFrameleft,textvariable=self.var_roomavailable,width=22,font=("arial",13,"bold"))
        # txtRoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelFrameleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=20,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)




        #meal
        lblmeal=Label(labelFrameleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=3)
        lblmeal.grid(row=5,column=0,sticky=W)
        txtmeal=ttk.Entry(labelFrameleft,textvariable=self.var_meal,width=22,font=("arial",13,"bold"))
        txtmeal.grid(row=5,column=1)
        #No of days
        lblNoOfDays=Label(labelFrameleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=3)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelFrameleft,textvariable=self.var_noofday,width=22,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)
        #Paid tax
        labelpaidtax=Label(labelFrameleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=3)
        labelpaidtax.grid(row=7,column=0,sticky=W)
        txt_paidtax=ttk.Entry(labelFrameleft,textvariable=self.var_paidtax,width=22,font=("arial",13,"bold"))
        txt_paidtax.grid(row=7,column=1)
        #Subtotal
        lblsubtotal=Label(labelFrameleft,text="Subtotal:",font=("arial",12,"bold"),padx=2,pady=3)
        lblsubtotal.grid(row=8,column=0,sticky=W)

        txt_subtotal=ttk.Entry(labelFrameleft,textvariable=self.var_actualtotal,width=22,font=("arial",13,"bold"))
        txt_subtotal.grid(row=8,column=1)
        #total cost
        lbltotalcost=Label(labelFrameleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=2)
        lbltotalcost.grid(row=9,column=0,sticky=W)
        txttotalcost=ttk.Entry(labelFrameleft,textvariable=self.var_total,width=22,font=("arial",13,"bold"))
        txttotalcost.grid(row=9,column=1)
        #=======Bill Button==============
        btnBill=Button(labelFrameleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        #=========================btns===================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=313,width=340,height=30)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)
        
        btndel=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btndel.grid(row=0,column=2,padx=1)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)

        #===============Right side image====================
        img3=Image.open(r"D:\nehapro\himages\bed.jpg")
        img3=img3.resize((394,158),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=644,y=55,width=394,height=158)

        #===============Table Frame search system ================#
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        table_frame.place(x=365,y=200,width=680,height=230)
        
        lblSearchby=Label(table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",13,"bold"),width=15,state="readonly")
        combo_search["value"]=("contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=22)
        txtsearch.grid(row=0,column=2,padx=1)
        
        btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnshowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnshowall.grid(row=0,column=4,padx=1)

        #==============Show data table========
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=665,height=170)
        
        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
         
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")

        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=======Add data============#
    def add_data(self):
        if self.var_conatct.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_conatct.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofday.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    #==============fetch data===============#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #----------get cursor--------------
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_conatct.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofday.set(row[6]) 

    #----------Update Data-----------
    def update(self):
        if self.var_conatct.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
        


            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                   
                                                                                              
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noofday.get(),
                                                                                                self.var_conatct.get()
                                                                                              ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)  
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_conatct.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
    def reset(self):
        self.var_conatct.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofday.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    
    #============All Data Fetch===================
    def Fetch_contact(self):
      if self.var_conatct.get()=="":
        messagebox.showerror("Error","Please enter contact Number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_conatct.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        #check for the valid user
        if row==None:
          messagebox.showerror("Error","This number Not Found",parent=self.root)
        else:
          conn.commit()
          conn.close()

          showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataframe.place(x=365,y=55,width=300,height=145)
          lblName=Label(showDataframe,text="Name: ",font=("arial",11,"bold"))
          lblName.place(x=0,y=0)

          lbl=Label(showDataframe,text=row,font=("arial",11,"bold"))
          lbl.place(x=85,y=0)
          #================Gender==============
          conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
          my_cursor=conn.cursor()
          query=("select Gender from customer where Mobile=%s")
          value=(self.var_conatct.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblName=Label(showDataframe,text="Gender: ",font=("arial",11,"bold"))
          lblName.place(x=0,y=25)

          lbl2=Label(showDataframe,text=row,font=("arial",11,"bold"))
          lbl2.place(x=85,y=25)
          #================email==============
          conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
          my_cursor=conn.cursor()
          query=("select Email from customer where Mobile=%s")
          value=(self.var_conatct.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblemail=Label(showDataframe,text="Email: ",font=("arial",11,"bold"))
          lblemail.place(x=0,y=50)

          lbl3=Label(showDataframe,text=row,font=("arial",11,"bold"))
          lbl3.place(x=85,y=50)
          #Nationality
          conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
          my_cursor=conn.cursor()
          query=("select Nationality from customer where Mobile=%s")
          value=(self.var_conatct.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblNationality=Label(showDataframe,text="Nationality: ",font=("arial",11,"bold"))
          lblNationality.place(x=0,y=75)

          lbl4=Label(showDataframe,text=row,font=("arial",11,"bold"))
          lbl4.place(x=85,y=75)
          #===Address===
          conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
          my_cursor=conn.cursor()
          query=("select Address from customer where Mobile=%s")
          value=(self.var_conatct.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lbladdress=Label(showDataframe,text="Address: ",font=("arial",11,"bold"))
          lbladdress.place(x=0,y=100)

          lbl5=Label(showDataframe,text=row,font=("arial",11,"bold"))
          lbl5.place(x=85,y=100)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall() 
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #calculating no of days from checkin and checkout date
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofday.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




        
        




           

           
      


        
if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
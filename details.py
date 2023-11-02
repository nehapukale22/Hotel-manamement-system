from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1290x560+230+220")

        #----------------Label---------#
        lbl_title=Label(self.root,text="ENROLL STUDENT",font=("times new roman",18,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50) 
        
        #----------------Logo-----------#
        img2=Image.open(r"D:\nehapro\himages\logohotel.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #----------------Label Frame---------------#
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=5,y=50,width=440,height=500)
     
        #------Floor-------
        lbl_floor=Label(labelFrameleft,text="PRN No",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelFrameleft,textvariable=self.var_floor,width=15,font=("arial",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)
        #------Room No-----
        check_in_date=Label(labelFrameleft,text="Department",font=("arial",12,"bold"),padx=2,pady=3)
        check_in_date.grid(row=1,column=0,sticky=W)
        self.var_RoomNo=StringVar()
        txtcheck_in_date=ttk.Entry(labelFrameleft,textvariable=self.var_RoomNo,width=15,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1,sticky=W)
        #------Room Type-----
        lbl_check_out=Label(labelFrameleft,text="Admisssion Type",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        self.var_RoomType=StringVar()
        txt_check_out=ttk.Entry(labelFrameleft,textvariable=self.var_RoomType,width=15,font=("arial",13,"bold"))
        txt_check_out.grid(row=2,column=1,sticky=W)
        #-------btns-------------
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=340,height=30)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)
        
        btndel=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btndel.grid(row=0,column=2,padx=1)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)
        #------------table search---------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"))
        table_frame.place(x=450,y=50,width=700,height=500)
        #---------scrollbar for table-----------
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
         
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        #---------floor table----------
        self.room_table.heading("floor",text="PRN No")
        self.room_table.heading("roomno",text="Department")
        self.room_table.heading("roomType",text="Admission Type")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                                self.var_floor.get(),
                                                                                                self.var_RoomNo.get(),
                                                                                                self.var_RoomType.get(),
                                                                                                
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    #==============fetch data===============#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #----------get cursor--------------
    #when you click on data row it should be visible in entry field
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])
        #for getcursor we need to bind it 
    #----------Update Data-----------
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
        


            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update  details set Floor=%s,RoomType=%s where RoomNo=%s",(self.var_floor.get(),
                                                                                         self.var_RoomType.get(),
                                                                                         self.var_RoomNo.get()
                                                                                              ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset_data(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")

        

if __name__=="__main__":
    root=Tk()
    obj=DetailRoom(root)
    root.mainloop()
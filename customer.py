from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Campus Management System")
        self.root.geometry("1290x560+230+220")
        #================variables==========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()



        #=============Title============#
        lbl_title=Label(self.root,text="ADD STUDENT DETAILS",font=("times new roman",18,"bold"),bg="black",fg="silver",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50) 
        
        #----------------Logo-----------#
        img2=Image.open(r"E:\nehapro\himages\logo.jpg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #----------------Label Frame---------------#
        labelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",padx=2,font=("times new roman",12,"bold"))
        labelFrameleft.place(x=5,y=50,width=380,height=500)
        #---------------Labels and Entries--------------#
        lbl_cust_ref=Label(labelFrameleft,text="Roll No:",font=("arial",12,"bold"),padx=2,pady=3)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_ref,font=("arial",13,"bold"))
        
        enty_ref.grid(row=0,column=1)
        #Cust Name
        cname=Label(labelFrameleft,text="Student Name:",font=("arial",12,"bold"),padx=2,pady=3)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_cust_name,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        #mother Name
        lblmname=Label(labelFrameleft,text="Department",font=("arial",12,"bold"),padx=2,pady=3)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        #gender combobox
        label_gender=Label(labelFrameleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=3)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelFrameleft,textvariable=self.var_gender,font=("arial",13,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        #postcode
        lblPostCode=Label(labelFrameleft,text="Semester:",font=("arial",12,"bold"),padx=2,pady=3)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_post,font=("arial",13,"bold"))
        txtpostcode.grid(row=4,column=1)
        #mobilenumber
        lblmobile=Label(labelFrameleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=3)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_mobile,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)
        #email
        lblmobile1=Label(labelFrameleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=3)
        lblmobile1.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelFrameleft,width=22,textvariable=self.var_email,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)
        #nationality
        labelnationality=Label(labelFrameleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=3)
        labelnationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(labelFrameleft,font=("arial",13,"bold"),width=20,textvariable=self.var_nationality,state="readonly")
        combo_nationality["value"]=("Indian","American","British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        #idproof type combobox
        lblidproof=Label(labelFrameleft,text="Year of graduation:",font=("times new roman",12,"bold"),padx=2,pady=3)
        lblidproof.grid(row=8,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelFrameleft,textvariable=self.var_id_proof,font=("arial",13,"bold"),width=20,state="readonly")
        combo_id["value"]=("2023","2024","2025")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        #id number
        lblidnum=Label(labelFrameleft,text="Adhar Number:",font=("arial",12,"bold"),padx=2,pady=2)
        lblidnum.grid(row=9,column=0,sticky=W)
        txtidnum=ttk.Entry(labelFrameleft,textvariable=self.var_id_number,width=22,font=("arial",13,"bold"))
        txtidnum.grid(row=9,column=1)
        #address
        lbladd=Label(labelFrameleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=2)
        lbladd.grid(row=10,column=0,sticky=W)
        txtadd=ttk.Entry(labelFrameleft,textvariable=self.var_address,width=22,font=("arial",13,"bold"))
        txtadd.grid(row=10,column=1)
        
        #=========================btns===================
        btn_frame=Frame(labelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=340,height=30)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)
        
        btndel=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btndel.grid(row=0,column=2,padx=1)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)
        #===============Table Frame search system ================#
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        table_frame.place(x=390,y=50,width=889,height=500)
        
        lblSearchby=Label(table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",13,"bold"),width=15,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=1)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=22)
        txtsearch.grid(row=0,column=2,padx=1)
        
        btnSearch=Button(table_frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnshowall=Button(table_frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnshowall.grid(row=0,column=4,padx=1)
        
        #==============Show data table========
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=48,width=889,height=400)
        
        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_det_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
         
        scroll_x.config(command=self.Cust_det_table.xview)
        scroll_y.config(command=self.Cust_det_table.yview)
        
        self.Cust_det_table.heading("ref",text="PRN No")
        self.Cust_det_table.heading("name",text="Student Name")
        self.Cust_det_table.heading("mother",text="Department")
        self.Cust_det_table.heading("gender",text="Gender")
        self.Cust_det_table.heading("post",text="Semester")
        self.Cust_det_table.heading("mobile",text="Mobile")
        self.Cust_det_table.heading("email",text="Email")
        self.Cust_det_table.heading("nationality",text="Nationality")
        self.Cust_det_table.heading("idproof",text="Year OF Graduation")
        self.Cust_det_table.heading("idnumber",text="Adhar Number")
        self.Cust_det_table.heading("address",text="Address")
        
        self.Cust_det_table["show"]="headings"
        
        self.Cust_det_table.column("ref",width=100)
        self.Cust_det_table.column("name",width=100)
        self.Cust_det_table.column("mother",width=100)
        self.Cust_det_table.column("gender",width=100)
        self.Cust_det_table.column("post",width=100)
        self.Cust_det_table.column("mobile",width=100)
        self.Cust_det_table.column("email",width=100)
        self.Cust_det_table.column("nationality",width=100)
        self.Cust_det_table.column("idproof",width=100)
        self.Cust_det_table.column("idnumber",width=100)
        self.Cust_det_table.column("address",width=100)
        self.Cust_det_table.pack(fill=BOTH,expand=1)
        self.Cust_det_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                   self.var_cust_name.get(),
                                                                                                   self.var_mother.get(),
                                                                                                   self.var_gender.get(),
                                                                                                   self.var_post.get(),
                                                                                                   self.var_mobile.get(),
                                                                                                   self.var_email.get(),
                                                                                                   self.var_nationality.get(),
                                                                                                   self.var_id_proof.get(),
                                                                                                   self.var_id_number.get(),
                                                                                                   self.var_address.get()
                                                                           ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_det_table.delete(*self.Cust_det_table.get_children())
            for i in rows:
                self.Cust_det_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Cust_det_table.focus()
        content=self.Cust_det_table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
        


            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                   
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_ref.get()
                                                                                              ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="welcomE@2021",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall() 
        if len (rows)!=0:
            self.Cust_det_table.delete(*self.Cust_det_table.get_children())
            for i in rows:
                self.Cust_det_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        


            







        
    
    
        
    
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
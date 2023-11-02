from tkinter import*
from PIL import Image,ImageTk
from customer import cust_win
from room import Roombooking
from details import DetailRoom

class hotelmgmtsys:
    def __init__(self,root):
        self.root=root
        self.root.title("Campus Management System")
        self.root.geometry("1550x800+0+0")
        #----------------First Image -----------#
        img1=Image.open(r"E:\nehapro\himages\RSCOE.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        
        #----Title---#
        lbl_title=Label(self.root,text="CAMPUS  MANAGEMENT  SYSTEM",font=("times new roman",40,"bold"),bg="WHITE",fg="NAVY BLUE",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #-----Main Frame----#
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #=============menu==============
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="SKY BLUE",fg="WHITE",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        #-----btn Frame----#
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=335)
        
        cust_btn=Button(btn_frame,text="ADMIN",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="BLACK",fg="grey",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="REGISTER",command=self.roombookinh,width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="STUDENT",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="FACULTY",width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="ADMISSION CELL",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        log=Button(btn_frame,text="PLACEMENT CELL",width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        log.grid(row=5,column=0,pady=1)
        l=Button(btn_frame,text="ENQUIRY/QUERY",width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        l.grid(row=6,column=0,pady=1)
        logout_bt=Button(btn_frame,text="SETTINGS",width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        logout_bt.grid(row=7,column=0,pady=1)
        LAST_bt=Button(btn_frame,text="LOG OUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand1")
        LAST_bt.grid(row=8,column=0,pady=1)
        
        
        #----------Right side---------#
        img3=Image.open(r"E:\nehapro\himages\jspm.png")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=600)
        
        ###################DOWN Images###################
        
        frame=Frame(self.root,bd=4,relief=RIDGE)
        frame.place(x=0,y=560,width=230,height=230)
       # Pack the label into the window
        contact_label = Label(frame, text="Contact Us", font=("Helvetica", 15, "bold"), fg="orange")
        contact_label.pack(pady=1)

       # Create a bold horizontal line as the second line
        line_label = Label(frame,text="---------------------------", font=("Helvetica", 12, "bold"))
        line_label.pack(pady=1)

       # Create the third line with college information
        inst_lab= Label(frame, text="Institute", font=("Helvetica",13, "bold"), fg="dark orange")
        inst_lab.pack(pady=1)
        college_label = Label(frame,text=" JSPM'S Rajarshi", font=("Helvetica", 11))
        college_label.pack(pady=1)
        college_labe2 = Label(frame,text="Shahu College Of Engineering", font=("Helvetica", 11))
        college_labe2.pack(pady=1)

       # Create the fourth line with the address
        add_label = Label(frame, text="Address :", font=("Helvetica", 13), fg="dark orange")
        add_label.pack(pady=1)
        addre_label = Label(frame,text="Ashok Nagar, Tathawade", font=("Helvetica", 11))
        addre_label.pack(pady=1)
        address_label = Label(frame,text="Pimpri-Chinchwad, 411033", font=("Helvetica", 11))
        address_label.pack(pady=1)
        #open customer window

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def roombookinh(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailRoom(self.new_window)
    def logout(self):
        self.root.destroy()
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=hotelmgmtsys(root)
    root.mainloop()
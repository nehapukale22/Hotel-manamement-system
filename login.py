from tkinter import*
from tkinter import ttk
#for image import module
from PIL import Image,ImageTk  #pip install pillow
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        #geometry (width x height + x start point + y start point)
        self.root.geometry("1550x800+0+0")
        #----------------First Image -----------#
        img1=Image.open(r"E:\nehapro\himages\RSCOE.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    #close the window with root
    root.mainloop()

from binascii import b2a_base64
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import tkinter
from PIL import Image, ImageTk
import os

from employee import Employee
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img = Image.open("app_images/im1.jfif")
        img=img.resize((500, 110), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=110)


        #second image
        img1 = Image.open("app_images/im2.jfif")
        img1=img1.resize((500, 110), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=500, y=0, width=500, height=110)

        #third image
        img2 = Image.open("app_images/im3.jfif")
        img2=img2.resize((500, 110), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1000, y=0, width=500, height=110)


        #bg image
        imgbg = Image.open("app_images/bg.jpg")
        imgbg=imgbg.resize((1530, 710), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root, image=self.photoimgbg)
        bg_img.place(x=0, y=110, width=1530, height=710)

        #big title
        title_lb1 = Label(bg_img, text="SMART ATTENDANCE SYSTEM SOFTWARE", font=("time new roman", 35, 'bold'), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=40)


        #employee button
        img4 = Image.open("app_images/employees.jpg")
        img4=img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.employee_details, cursor="hand2")
        b1.place(x=200, y=100, width=200, height=200)
        lb1 = Button(bg_img, text="Employee Details", command=self.employee_details, cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=200, y=270, width=200, height=40)

        #detection button
        img5 = Image.open("app_images/fr_3.jpg")
        img5=img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=450, y=100, width=200, height=200)
        lb1 = Button(bg_img, text="Face Detection", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=450, y=270, width=200, height=40)

        #Attendance button
        img6 = Image.open("app_images/att.jfif")
        img6=img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, command=self.attendance, image=self.photoimg6, cursor="hand2")
        b3.place(x=700, y=100, width=200, height=200)
        lb1 = Button(bg_img, text="Attendance", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=700, y=270, width=200, height=40)

        #Help button
        img7 = Image.open("app_images/help.jpg")
        img7=img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=950, y=100, width=200, height=200)
        lb1 = Button(bg_img, text="Help", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=950, y=270, width=200, height=40)

        #Train button
        img8 = Image.open("app_images/train.jpg")
        img8=img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, command=self.train, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=350, width=200, height=200)
        lb1 = Button(bg_img, text="Train Face", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=200, y=520, width=200, height=40)

        #photos button
        img9 = Image.open("app_images/photos.jfif")
        img9=img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, command= self.open_photos, image=self.photoimg9, cursor="hand2")
        b6.place(x=450, y=350, width=200, height=200)
        lb1 = Button(bg_img, text="Photos", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=450, y=520, width=200, height=40)

        #about button
        img10 = Image.open("app_images/dev.jpg")
        img10=img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=700, y=350, width=200, height=200)
        lb1 = Button(bg_img, text="About Dev", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=700, y=520, width=200, height=40)

        #exit button
        img11 = Image.open("app_images/exit.jpg")
        img11=img11.resize((200, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, command=self.iExit, image=self.photoimg11, cursor="hand2")
        b8.place(x=950, y=350, width=200, height=200)
        lb1 = Button(bg_img, text="Exit", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=950, y=520, width=200, height=40)


    def open_photos(self):
        os.startfile("data")


    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Employee(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def iExit(self):
        self.iExit = messagebox.askyesno("Face Recognition", "Do you want to exit this app")
        if(self.iExit>0):
            self.root.destroy()
        else:
            return False





if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
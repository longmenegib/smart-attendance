from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

import imutils
import requests
import csv
import os
from tkinter import filedialog

url = "http://192.168.43.167:8080"

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #declaration of variable
        self.var_title = StringVar()
        self.var_time = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_status = StringVar()
        self.var_date = StringVar()

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
        title_lb1 = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("time new roman", 35, 'bold'), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=40)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        #left label frame
        left_frame=LabelFrame(main_frame, bd=2,relief=RIDGE,text="Attendance Details",  font=("time new roman", 12, 'bold'))
        left_frame.place(x=10, y=10,width=670, height=580)
        

        #small image
        img_left = Image.open("app_images/im3.jfif")
        img_left=img_left.resize((700, 110), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(left_frame, image=self.photoimg_left)
        f_lb1.place(x=5, y=0, width=700, height=110)

        #current position
        current_position_frame  = Frame(left_frame, bd=2, bg='white', relief=RIDGE)
        current_position_frame.place(x=5, y=120, width=700, height=600)

        
        #employee id
        employeeid_label= Label(current_position_frame, text="EmployeeID", bg='white', font=("time new roman", 13, 'bold'))
        employeeid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        employeeid_entry = ttk.Entry(current_position_frame, state= DISABLED, textvariable= self.var_id, width=12, font=("times new roman", 13, 'bold'))
        employeeid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

            #employee name
        employeename_label= Label(current_position_frame, text="Name:", bg='white', font=("time new roman", 13, 'bold'))
        employeename_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        employeename_entry = ttk.Entry(current_position_frame, textvariable= self.var_name, width=20, font=("times new roman", 13, 'bold'))
        employeename_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        #title
        dep_label= Label(current_position_frame, text="Title", bg='white', font=("time new roman", 13, 'bold'))
        dep_label.grid(row=1, column=0, padx=10, sticky=W)

        dep_combo= ttk.Entry(current_position_frame, textvariable= self.var_title, width=20, font=("times new roman", 13, 'bold'))
        dep_combo.grid(row=1, column=1,padx=10, pady=10, sticky=W)

            #employee time
        employeename_label= Label(current_position_frame, text="Time:", bg='white', font=("time new roman", 13, 'bold'))
        employeename_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        employeename_entry = ttk.Entry(current_position_frame, textvariable= self.var_time, width=20, font=("times new roman", 13, 'bold'))
        employeename_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

            #employee date
        employeeemail_label= Label(current_position_frame, text="Date:", bg='white', font=("time new roman", 13, 'bold'))
        employeeemail_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        employeeemail_entry = ttk.Entry(current_position_frame, textvariable= self.var_date, width=20, font=("times new roman", 13, 'bold'))
        employeeemail_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

            #employee status
        employeephone_label= Label(current_position_frame, text="Status:", bg='white', font=("time new roman", 13, 'bold'))
        employeephone_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        employeephone_entry=ttk.Combobox(current_position_frame, textvariable= self.var_status, font=("times new roman", 13, 'bold'), state='readonly', width=20)
        employeephone_entry["values"]=("Select", "Present", "Absent")
        employeephone_entry.current(0)
        employeephone_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        #buttons frame
        btn_frame  = Frame(current_position_frame, bd=2, bg='white', relief=RIDGE)
        btn_frame.place(x=0, y=300, width=715, height=70)

            #save btn
        save_btn= Button(btn_frame, command=self.exportCsv, width=16, text="Export csv", bg='gold', font=("time new roman", 13, 'bold'))
        save_btn.grid(row=0, column=0)

            #update btn
        update_btn= Button(btn_frame, command=self.importCsv, width=16, text="Import csv", bg='gold', font=("time new roman", 13, 'bold'))
        update_btn.grid(row=0, column=1)

            #Delete btn
        delete_btn= Button(btn_frame, width=16, text="Update", bg='gold', font=("time new roman", 13, 'bold'))
        delete_btn.grid(row=0, column=2)

            #Reset btn
        reset_btn= Button(btn_frame, width=16, text="Reset", bg='gold', font=("time new roman", 13, 'bold'))
        reset_btn.grid(row=0, column=3)
        





        #right label frame
        right_frame=LabelFrame(main_frame, bd=2,relief=RIDGE,text="Employee Attendance List",  font=("time new roman", 12, 'bold'))
        right_frame.place(x=700, y=10,width=660, height=580)

        # table frame ===================================
        table_frame  = Frame(right_frame, bd=2, bg='white', relief=RIDGE)
        table_frame.place(x=5, y=5, width=650, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame, column=('id', 'name','title', 'time', 'date', 'status'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('id', text='EmployeeID')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('title', text='Title')
        self.employee_table.heading('time', text='Time')
        self.employee_table.heading('date', text='Date')
        self.employee_table.heading('status', text='Status')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('title', width=100)
        self.employee_table.column('time', width=100)
        self.employee_table.column('id', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('date', width=100)
        self.employee_table.column('status', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        

    def fetchData(self, rows):
        self.employee_table.delete(*self.employee_table.get_children())
        for i in rows:
          self.employee_table.insert("", END, values=i) 


    def importCsv(self):
        global mydata
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV file", "*csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data", "Cannot export empty data")
                return False
            fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV file", "*csv"),("All File","*.*")),parent=self.root)
            with open(fin, mode="w", newline="") as myfile:
                exp = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp.append(i)
                messagebox.showinfo("Export", "Your attendance has been exported to "+ os.path.basename(fin)+"successfully")

        except Exception as err:
            messagebox.showerror("Error exporting", f"Due to :{str(err)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()
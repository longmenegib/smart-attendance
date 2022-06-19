from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector


class Employee:
  def __init__(self, root):
      self.root = root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")


      #declaration of variable
      self.var_title = StringVar()
      self.var_year = StringVar()
      self.var_id = StringVar()
      self.var_name = StringVar()
      self.var_phone = StringVar()
      self.var_email = StringVar()
      self.var_dob = StringVar()
      self.var_address = StringVar()
      self.var_status = StringVar()
      self.var_gender = StringVar()






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
      title_lb1 = Label(bg_img, text="EMPLOYEE MANAGEMENT SYSTEM", font=("time new roman", 35, 'bold'), bg="white", fg="red")
      title_lb1.place(x=0, y=0, width=1530, height=40)

      main_frame = Frame(bg_img, bd=2)
      main_frame.place(x=20, y=50, width=1480, height=600)

      #left label frame
      left_frame=LabelFrame(main_frame, bd=2,relief=RIDGE,text="Employee Details",  font=("time new roman", 12, 'bold'))
      left_frame.place(x=10, y=10,width=730, height=580)

        #small image
      img_left = Image.open("app_images/im3.jfif")
      img_left=img_left.resize((720, 110), Image.ANTIALIAS)
      self.photoimg_left = ImageTk.PhotoImage(img_left)

      f_lb1 = Label(left_frame, image=self.photoimg_left)
      f_lb1.place(x=5, y=0, width=720, height=110)

      #current position
      current_position_frame  = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Current position informations")
      current_position_frame.place(x=5, y=120, width=720, height=70)

      #title
      dep_label= Label(current_position_frame, text="Job Title", bg='white', font=("time new roman", 13, 'bold'))
      dep_label.grid(row=0, column=0, padx=10, sticky=W)

      dep_combo= ttk.Entry(current_position_frame, textvariable= self.var_title, width=20, font=("times new roman", 13, 'bold'))
      dep_combo.grid(row=0, column=1,padx=10, pady=10, sticky=W)

        #year
      year_label= Label(current_position_frame, text="Entry Year", bg='white', font=("time new roman", 13, 'bold'))
      year_label.grid(row=0, column=2, padx=10, sticky=W)

      year_combo= ttk.Entry(current_position_frame, textvariable= self.var_year, width=20, font=("times new roman", 13, 'bold'))
      year_combo.grid(row=0, column=3,padx=10, sticky=W)

      #emplyee details
      employee_infos  = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Current Employee informations")
      employee_infos.place(x=5, y=200, width=720, height=500)

        #employee id
      employeeid_label= Label(employee_infos, text="EmployeeID", bg='white', font=("time new roman", 13, 'bold'))
      employeeid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

      employeeid_entry = ttk.Entry(employee_infos, textvariable= self.var_id, width=20, font=("times new roman", 13, 'bold'))
      employeeid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #employee name
      employeename_label= Label(employee_infos, text="Full name:", bg='white', font=("time new roman", 13, 'bold'))
      employeename_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

      employeename_entry = ttk.Entry(employee_infos, textvariable= self.var_name, width=20, font=("times new roman", 13, 'bold'))
      employeename_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #employee email
      employeeemail_label= Label(employee_infos, text="Email address:", bg='white', font=("time new roman", 13, 'bold'))
      employeeemail_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

      employeeemail_entry = ttk.Entry(employee_infos, textvariable= self.var_email, width=20, font=("times new roman", 13, 'bold'))
      employeeemail_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #employee phone
      employeephone_label= Label(employee_infos, text="Phone number:", bg='white', font=("time new roman", 13, 'bold'))
      employeephone_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

      employeephone_entry = ttk.Entry(employee_infos, textvariable= self.var_phone, width=20, font=("times new roman", 13, 'bold'))
      employeephone_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #employee birthdate
      employeedob_label= Label(employee_infos, text="Date of Birth:", bg='white', font=("time new roman", 13, 'bold'))
      employeedob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

      employeedob_entry = ttk.Entry(employee_infos, textvariable= self.var_dob, width=20, font=("times new roman", 13, 'bold'))
      employeedob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #employee address
      employeeadd_label= Label(employee_infos, text="Address:", bg='white', font=("time new roman", 13, 'bold'))
      employeeadd_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

      employeeadd_entry = ttk.Entry(employee_infos, textvariable= self.var_address, width=20, font=("times new roman", 13, 'bold'))
      employeeadd_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #employee gender
      employeegender_label= Label(employee_infos, text="Gender:", bg='white', font=("time new roman", 13, 'bold'))
      employeegender_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

      empl_gender_combo=ttk.Combobox(employee_infos, textvariable= self.var_gender, font=("times new roman", 13, 'bold'), state='readonly', width=20)
      empl_gender_combo["values"]=("Select", "Male", "Female")
      empl_gender_combo.current(0)
      empl_gender_combo.grid(row=3, column=1,padx=5, pady=5, sticky=W)

        #employee status
      employeestatus_label= Label(employee_infos, text="Marital status:", bg='white', font=("time new roman", 13, 'bold'))
      employeestatus_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

      empl_status_combo=ttk.Combobox(employee_infos,  textvariable= self.var_status, font=("times new roman", 13, 'bold'), state='readonly', width=20)
      empl_status_combo["values"]=("Select", "Single", "Married", "Divorced")
      empl_status_combo.current(0)
      empl_status_combo.grid(row=3, column=3,padx=5, pady=5, sticky=W)


      #radio buttons
      self.var_radio1 = StringVar()
      radiobtn1 = ttk.Radiobutton(employee_infos, variable= self.var_radio1, text="Take Photo Sample", value="Yes")
      radiobtn1.grid(row=4, column=0,padx=5, pady=5, sticky=W)
      radiobtn2 = ttk.Radiobutton(employee_infos, variable= self.var_radio1, text="No Photo Sample", value="No")
      radiobtn2.grid(row=4, column=1,padx=5, pady=5, sticky=W)


      #buttons frame
      btn_frame  = Frame(employee_infos, bd=2, bg='white', relief=RIDGE)
      btn_frame.place(x=0, y=180, width=715, height=70)

        #save btn
      save_btn= Button(btn_frame, command=self.add_data, width=17, text="Save", bg='gold', font=("time new roman", 13, 'bold'))
      save_btn.grid(row=0, column=0)

        #update btn
      update_btn= Button(btn_frame, command=self.update_data, width=17, text="Update", bg='gold', font=("time new roman", 13, 'bold'))
      update_btn.grid(row=0, column=1)

        #Delete btn
      delete_btn= Button(btn_frame, command=self.delete_data, width=17, text="Delete", bg='gold', font=("time new roman", 13, 'bold'))
      delete_btn.grid(row=0, column=2)

        #Reset btn
      reset_btn= Button(btn_frame, command=self.reset_data, width=17, text="Reset", bg='gold', font=("time new roman", 13, 'bold'))
      reset_btn.grid(row=0, column=3)
      

        #buttons phtots frame
      btn_frame1  = Frame(employee_infos, bd=2, bg='white', relief=RIDGE)
      btn_frame1.place(x=0, y=230, width=715, height=35)


        #Delete btn
      take_pic_btn= Button(btn_frame1, command=self.generate_dataset, width=35, text="Take Photo", bg='gold', font=("time new roman", 13, 'bold'))
      take_pic_btn.grid(row=0, column=0)

        #Reset btn
      update_pic_btn= Button(btn_frame1, width=35, text="Update Photo", bg='gold', font=("time new roman", 13, 'bold'))
      update_pic_btn.grid(row=0, column=1)


      
      #right label frame
      right_frame=LabelFrame(main_frame, bd=2,relief=RIDGE,text="Employee Details",  font=("time new roman", 12, 'bold'))
      right_frame.place(x=750, y=10,width=660, height=580)

        #small image
      img_right = Image.open("app_images/im3.jfif")
      img_right=img_right.resize((580, 110), Image.ANTIALIAS)
      self.photoimg_right = ImageTk.PhotoImage(img_right)

      f_lb1 = Label(right_frame, image=self.photoimg_right)
      f_lb1.place(x=5, y=0, width=580, height=110)

        #search frame
      search_frame  = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE, text="Current position informations")
      search_frame.place(x=5, y=120, width=580, height=70)

        #search label
      search_label= Label(search_frame, text="Search By:", bg='red', fg='white', font=("time new roman", 12, 'bold'))
      search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

      #search combo box
      search_combo=ttk.Combobox(search_frame, width=10, font=("times new roman", 13, 'bold'), state='readonly')
      search_combo["values"]=("Select", "Phone", "title", "Gender")
      search_combo.current(0)
      search_combo.grid(row=0, column=1,padx=5, pady=5, sticky=W)

      #ssearch entry
      search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, 'bold'))
      search_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #search btn
      search_btn= Button(search_frame, text="Search", bg='gold', font=("time new roman", 13, 'bold'))
      search_btn.grid(row=0, column=4, padx=4)

        #search btn
      search_all_btn= Button(search_frame, text="Show all", bg='gold', font=("time new roman", 13, 'bold'))
      search_all_btn.grid(row=0, column=5, padx=4)

      # table frame ===================================
      table_frame  = Frame(right_frame, bd=2, bg='white', relief=RIDGE)
      table_frame.place(x=5, y=200, width=580, height=250)

      scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

      self.employee_table=ttk.Treeview(table_frame, column=('id', 'name','title', 'year', 'status', 'address', 'email', 'phone', 'dob', 'gender', 'photoSample'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.employee_table.xview)
      scroll_y.config(command=self.employee_table.yview)

      self.employee_table.heading('id', text='EmployeeID')
      self.employee_table.heading('name', text='Name')
      self.employee_table.heading('title', text='Title')
      self.employee_table.heading('year', text='Year')
      self.employee_table.heading('status', text='Status')
      self.employee_table.heading('address', text='Address')
      self.employee_table.heading('email', text='Email')
      self.employee_table.heading('phone', text='Phone')
      self.employee_table.heading('dob', text='DOB')
      self.employee_table.heading('gender', text='Gender')
      self.employee_table.heading('photoSample', text='PhotoSampleStatus')
      self.employee_table['show'] = 'headings'

     
      self.employee_table.column('title', width=100)
      self.employee_table.column('year', width=100)
      self.employee_table.column('id', width=100)
      self.employee_table.column('name', width=200)
      self.employee_table.column('email', width=200)
      self.employee_table.column('phone', width=100)
      self.employee_table.column('dob', width=100)
      self.employee_table.column('status', width=70)
      self.employee_table.column('address', width=200)
      self.employee_table.column('photoSample', width=200)
      self.employee_table.column('gender', width=100)


      self.employee_table.pack(fill=BOTH, expand=1)
      self.employee_table.bind("<ButtonRelease>", self.get_cursor)
      self.get_data()



  #function declaration to add employee information
  def add_data(self):
      if self.var_gender.get()=="Select" or self.var_status.get()=="Select" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_title.get()=="" or self.var_year.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_id.get()=="":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.var_id.get(),
            self.var_name.get(),
            self.var_title.get(),
            self.var_year.get(),
            self.var_status.get(),
            self.var_address.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.var_dob.get(),
            self.var_gender.get(),
            self.var_radio1.get(),
            
          ))

          conn.commit()
          self.get_data()
          conn.close()
          messagebox.showinfo("Success", "Employee details has been registered")
        except Exception as er:
          messagebox.showerror("Error", f"Due to : {str(er)}", parent=self.root)

  def get_data(self):
      conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from employee")
      data = my_cursor.fetchall()

      if (len(data) != 0):
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
          self.employee_table.insert("", END, values=i)

        conn.commit()
      conn.close()

  def get_cursor(self, event=""):
    cursor_focus=self.employee_table.focus()
    content=self.employee_table.item(cursor_focus)
    data=content["values"]

    print(data)

    self.var_id.set(data[0])
    self.var_name.set(data[1])
    self.var_title.set(data[2])
    self.var_year.set(data[3])
    self.var_status.set(data[4])
    self.var_address.set(data[5])
    self.var_email.set(data[6])
    self.var_phone.set(data[7])
    self.var_dob.set(data[8])
    self.var_gender.set(data[9])
    self.var_radio1.set(data[10])


  def update_data(self):
    if self.var_gender.get()=="Select" or self.var_status.get()=="Select" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_title.get()=="" or self.var_year.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_id.get()=="":
      messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
      try:
        update =  messagebox.askyesno("Update", "Do you want to update this data?")
        if update > 0:

          conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("update employee set name=%s, title=%s, year=%s, status=%s, address=%s, email=%s, phone=%s, dob=%s, gender=%s, photoSample=%s where id=%s", (
           
            self.var_name.get(),
            self.var_title.get(),
            self.var_year.get(),
            self.var_status.get(),
            self.var_address.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.var_dob.get(),
            self.var_gender.get(),
            self.var_radio1.get(),  
            self.var_id.get(),
          ))
          messagebox.showinfo("Success", "Employee details has been updated")
          conn.commit()
          self.get_data()
          conn.close()
          
      except Exception as er:
        messagebox.showerror("Error", f"Due to : {str(er)}", parent=self.root)

  def reset_data(self):
    self.var_id.set("")
    self.var_name.set("")
    self.var_title.set("")
    self.var_year.set("")
    self.var_status.set("Select")
    self.var_address.set("")
    self.var_email.set("")
    self.var_phone.set("")
    self.var_dob.set("")
    self.var_gender.set("Select")
    self.var_radio1.set("")

  def delete_data(self):
    if self.var_id.get()=="":
      messagebox.showerror("Error", "Employee id must be required", parent=self.root)
    else:
      try: 
        delete=messagebox.askyesno("Employee delete detail", "Do you wish to delete this employee detail?")

        if delete>0:
          conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
          my_cursor=conn.cursor()
          sql = "delete from employee where id=%s"
          val= (self.var_id.get(),)
          my_cursor.execute(sql, val)
        else:
          return

        conn.commit()
        self.get_data()
        self.reset_data()
        conn.close()
        messagebox.showinfo("Success", "Employee details deleted")
      except Exception as er:
        messagebox.showerror("Error", f"Due to : {er}", parent=self.root)


  # =======================generate data set or take a phto samles===
  def generate_dataset(self):
    if self.var_gender.get()=="Select" or self.var_status.get()=="Select" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_title.get()=="" or self.var_year.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_id.get()=="":
      messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
      try:
        conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        myresult=my_cursor.fetchall()
        id=0
        for x in myresult:
          id+=1
        my_cursor.execute("update employee set name=%s, title=%s, year=%s, status=%s, address=%s, email=%s, phone=%s, dob=%s, gender=%s, photoSample=%s where id=%s", (
        
          self.var_name.get(),
          self.var_title.get(),
          self.var_year.get(),
          self.var_status.get(),
          self.var_address.get(),
          self.var_email.get(),
          self.var_phone.get(),
          self.var_dob.get(),
          self.var_gender.get(),
          self.var_radio1.get(),  
          self.var_id.get()==id+1,
        ))
        conn.commit()
        self.get_data()
        self.reset_data()
        conn.close()

        ####load predifined data on face frontals from opencv

        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
          gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          faces=face_classifier.detectMultiScale(gray,1.3 ,5)
          #scalling factor=1.3
          #Minimum Neighbor=5

          for (x, y, w, h) in faces:
            face_cropped=img[y:y+h, x:x+w]
            return face_cropped

        cap=cv2.VideoCapture(0)
        img_id=0
        while True:
          ret, my_frame=cap.read()
          if face_cropped(my_frame) is not None:
            img_id+=1
            face=cv2.resize(face_cropped(my_frame), (450,450))
            face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"

            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
            cv2.imshow("Crooped Face", face)

          if cv2.waitKey(1)==13 or int(img_id)==20:
            break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Generation completed")

      except Exception as er:
        messagebox.showerror("Error", f"Due to : {str(er)}", parent=self.root)

    
if __name__ == "__main__":
    root=Tk()
    obj = Employee(root)
    root.mainloop()
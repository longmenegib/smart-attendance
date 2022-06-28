from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

         #big title
        title_lb1 = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 35, 'bold'), bg="white", fg="red")
        title_lb1.place(x=-20, y=0, width=1500, height=40)

        img_top=Image.open("app_images/employees.jpg")
        img_top=img_top.resize((1500, 320), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f1_img = Label(self.root, image=self.photoimg_top)
        f1_img.place(x=0, y=50, width=1500, height=320)


        lb1 = Button(self.root, command= self.train_classifier, text="CLICK HERE", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=-30, y=370, width=1500, height=60)


        img_down=Image.open("app_images/employees.jpg")
        img_down=img_down.resize((1500, 320), Image.ANTIALIAS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f1_img = Label(self.root, image=self.photoimg_down)
        f1_img.place(x=0, y=420, width=1500, height=320)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            print(image)
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #trrain the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        
        print(ids)


if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()
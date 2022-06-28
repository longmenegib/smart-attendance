from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np

from time import strftime
from datetime import datetime

import imutils
import requests

url = "http://192.168.43.246:8080"


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

         #big title
        title_lb1 = Label(self.root, text="FACE DETECTION", font=("time new roman", 35, 'bold'), bg="white", fg="red")
        title_lb1.place(x=-20, y=0, width=1500, height=40)

        img_top=Image.open("app_images/employees.jpg")
        img_top=img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f1_img = Label(self.root, image=self.photoimg_top)
        f1_img.place(x=0, y=50, width=650, height=700)

        img_down=Image.open("app_images/employees.jpg")
        img_down=img_down.resize((950, 700), Image.ANTIALIAS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f1_img = Label(self.root, image=self.photoimg_down)
        f1_img.place(x=650, y=50, width=950, height=700)

        lb1 = Button(f1_img, command=self.face_recog, text="Face Detector", cursor="hand2", font=("time new roman", 15, 'bold'), bg="gold", fg="red")
        lb1.place(x=300, y=500, width=200, height=40)


    #=================atendance================
    def mark_attendance(self, id, n, d):
        with open("attendance.csv", "r+", newline="\n") as f :
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                print(entry)
                name_list.append(entry[0])

            # print(name_list)
            if((id not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{n},{d},{dtString},{d1},Preset")
    
    #=========face dection recognition=======================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            # print(features)
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

               

                conn=mysql.connector.connect(host="localhost", username="root", password="680gib@#L", database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select name from employee where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                # my_cursor.execute("select id from employee where id="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(str(r))

                my_cursor.execute("select title from employee where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence>77:
                    cv2.putText(img,f"ID:{id}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Title:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(str(id), n, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,"unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # video_cap=cv2.VideoCapture(url+'/video')
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome To face Recognition",img)

            # img_resp = requests.get(url+'/shot.jpg')
            # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            # img = cv2.imdecode(img_arr, -1)
            # img = imutils.resize(img, width=1000, height=1800)
            # img=recognize(img,clf,faceCascade)
            # cv2.imshow("Android_cam", img)

            if cv2.waitKey(1)==27:
                break
        # video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition(root)
    root.mainloop()
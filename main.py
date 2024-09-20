from tkinter import Tk, Label, Button, Toplevel
from PIL import Image, ImageTk
from student import Student



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st image
        img1 = Image.open(r"C:\Users\amanv\Downloads\pexels-omaralnahi-18495.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=500, height=130)

        # 2nd image
        img2 = Image.open(r"C:\Users\amanv\Downloads\pexels-jplenio-1146708.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        second_label = Label(self.root, image=self.photoimg2)
        second_label.place(x=500, y=0, width=500, height=130)

        # 3rd image
        img3 = Image.open(r"C:\Users\amanv\Downloads\pexels-vladalex94-1402787.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        third_label = Label(self.root, image=self.photoimg3)
        third_label.place(x=1000, y=0, width=500, height=130)

        # Background image
        img4 = Image.open(r"C:\Users\amanv\Downloads\Background.jpeg")
        img4 = img4.resize((1370, 580), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1370, height=580)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1370, height=45)

        # Student button
        img5 = Image.open(r"C:\Users\amanv\Downloads\Person3.jpeg")
        img5 = img5.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=150, y=80, width=180, height=180)

        b_1 = Button(bg_img, text="Students Details",command=self.student_details, cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=150, y=255, width=180, height=40)

        # Detect Face
        img6 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img6 = img6.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=450, y=80, width=180, height=180)

        b_1 = Button(bg_img, text="Face Detector", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=450, y=255, width=180, height=40)


        # Attendance face button
        img7 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img7 = img7.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=750, y=80, width=180, height=180)

        b_1 = Button(bg_img, text="Attendance", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=750, y=255, width=180, height=40)


         # Help face button
        img8 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img8 = img8.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=1050, y=80, width=180, height=180)

        b_1 = Button(bg_img, text="Help", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=1050, y=255, width=180, height=40)


         # Train face button
        img9 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img9 = img9.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=150, y=330, width=180, height=180)

        b_1 = Button(bg_img, text="Train Data", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=150, y=505, width=180, height=40)


         # Photos face button
        img10 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img10 = img10.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=450, y=330, width=180, height=180)

        b_1 = Button(bg_img, text="Photos", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=450, y=505, width=180, height=40)


         # Developers face button
        img11 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img11 = img11.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=750, y=330, width=180, height=180)

        b_1 = Button(bg_img, text="Developer", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=750, y=505, width=180, height=40)


         # Exit face button
        img12 = Image.open(r"C:\Users\amanv\Downloads\Person.jpeg")
        img12 = img12.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=1050, y=330, width=180, height=180)

        b_1 = Button(bg_img, text="Exit", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b_1.place(x=1050, y=505, width=180, height=40)

        # ===============================Function Buttons====================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

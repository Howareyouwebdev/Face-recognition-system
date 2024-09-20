from tkinter import Tk, ttk, Label, Frame, LabelFrame, RIDGE, W,Radiobutton,StringVar,Button,BOTH,messagebox
from PIL import Image, ImageTk
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")  # Adjusted size to fit the screen
        self.root.title("Face Recognition System")

        # ============variables==========================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        # 1st image
        img1 = Image.open(r"C:\Users\amanv\Downloads\pexels-omaralnahi-18495.jpg")
        img1 = img1.resize((450, 120), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=450, height=120)

        # 2nd image
        img2 = Image.open(r"C:\Users\amanv\Downloads\pexels-jplenio-1146708.jpg")
        img2 = img2.resize((450, 120), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg2 = ImageTk.PhotoImage(img2)

        second_label = Label(self.root, image=self.photoimg2)
        second_label.place(x=450, y=0, width=450, height=120)

        # 3rd image
        img3 = Image.open(r"C:\Users\amanv\Downloads\pexels-vladalex94-1402787.jpg")
        img3 = img3.resize((450, 120), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg3 = ImageTk.PhotoImage(img3)

        third_label = Label(self.root, image=self.photoimg3)
        third_label.place(x=900, y=0, width=450, height=120)

        # Background image
        img4 = Image.open(r"C:\Users\amanv\Downloads\Background.jpeg")
        img4 = img4.resize((1366, 620), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1366, height=620)

        # Title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 24, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1366, height=30)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=35, width=1355, height=600)  # Adjusted size and position

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 10, "bold"))
        Left_frame.place(x=5, y=5, width=660, height=585)  # Adjusted size

        img_left = Image.open(r"C:\Users\amanv\Downloads\pexels-vladalex94-1402787.jpg")
        img_left = img_left.resize((650, 120), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        third_label = Label(Left_frame, image=self.photoimg_left)
        third_label.place(x=5, y=0, width=650, height=120)

        # Current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 10, "bold"))
        current_course_frame.place(x=5, y=130, width=650, height=100)  # Adjusted size

        # Department
        dep_label = Label(current_course_frame,text="Department:", font=("times new roman", 10, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman", 10, "bold"), state="readonly", width=15)
        dep_combo["values"] = ("Select Department", "Computer", "Humanities", "Commerce", "Civil", "Engineering", "Business")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course:", font=("times new roman", 10, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course ,font=("times new roman", 10, "bold"), state="readonly", width=15)
        course_combo["values"] = ("Select Course", "BCA", "B.A", "B.com", "Bsc", "BE", "Cse" ,"Civil")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year:", font=("times new roman", 10, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year ,font=("times new roman", 10, "bold"), state="readonly", width=15)
        year_combo["values"] = ("Select Year", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester:", font=("times new roman", 10, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester ,font=("times new roman", 10, "bold"), state="readonly", width=15)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 10, "bold"))
        class_Student_frame.place(x=5, y=235, width=650, height=280)  # Adjusted size

        # Student Id
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 10, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=3, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        studentID_entry.grid(row=0, column=1, padx=5, pady=3, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 10, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=3, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        studentName_entry.grid(row=0, column=3, padx=5, pady=3, sticky=W)

        # class division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 10, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=5, pady=3, sticky=W)

        class_div_entry = ttk.Entry(class_Student_frame, textvariable=self.var_div ,width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        class_div_entry.grid(row=1, column=1, padx=5, pady=3, sticky=W)

        # Roll No
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 10, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=3, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        roll_no_entry.grid(row=1, column=3, padx=5, pady=3, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 10, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=3, sticky=W)

        gender_entry = ttk.Entry(class_Student_frame,textvariable=self.var_gender , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        gender_entry.grid(row=2, column=1, padx=5, pady=3, sticky=W)

        # Date Of Birth
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=3, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        dob_entry.grid(row=2, column=3, padx=5, pady=3, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 10, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=3, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email ,width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        email_entry.grid(row=3, column=1, padx=5, pady=3, sticky=W)

        # Phone No
        phone_label = Label(class_Student_frame, text="Phone NO:", font=("times new roman", 10, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=3, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        phone_entry.grid(row=3, column=3, padx=5, pady=3, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 10, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=3, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        address_entry.grid(row=4, column=1, padx=5, pady=3, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 10, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=3, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher , width=18, font=("times new roman", 11, "bold"))  # Adjusted width and font size
        teacher_entry.grid(row=4, column=3, padx=5, pady=3, sticky=W)

        # Radio button
        self.var_radio1=StringVar
        radionbtn1 = Radiobutton(class_Student_frame, textvariable=self.var_radio1,text="Take Photo Sample", value="Yes", font=("times new roman", 10, "bold"), bg="white")
        radionbtn1.grid(row=6, column=0, padx=5, pady=3, sticky=W)

        self.var_radio2=StringVar
        radionbtn2 = Radiobutton(class_Student_frame, textvariable=self.var_radio2,text="No Photo Sample", value="No", font=("times new roman", 10, "bold"), bg="white")
        radionbtn2.grid(row=6, column=1, padx=10, pady=3, sticky=W)

        # Buttons frame 
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=647, height=35)  # Adjusted size and position

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=16, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        reset_btn.grid(row=0, column=3)

        # New btn frame
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=215, width=645, height=40)  # Adjusted size and position

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=35, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        update_photo_btn.grid(row=0, column=1)





        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 10, "bold"))
        Right_frame.place(x=670, y=5, width=680, height=585)  # Adjusted size

        img_right = Image.open(r"C:\Users\amanv\Downloads\pexels-vladalex94-1402787.jpg")
        img_right = img_right.resize((670, 120), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_label = Label(Right_frame, image=self.photoimg_right)
        right_label.place(x=5, y=0, width=670, height=120)



        # Searching system
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 10, "bold"))
        Search_frame.place(x=5, y=125, width=670, height=70)  # Adjusted size

        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 14, "bold"), bg="red",fg="white")
        Search_label.grid(row=0, column=0, padx=5, pady=3, sticky=W)

        Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 14, "bold"), state="readonly", width=15)
        Search_combo["values"] = ("Select", "Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_frame, width=14, font=("times new roman", 14, "bold"))  # Adjusted width and font size
        Search_entry.grid(row=0, column=2, padx=5, pady=3, sticky=W)

        Search_btn = Button(Search_frame, text="Search", width=17, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        Search_btn.grid(row=0, column=2,padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=17, font=("times new roman", 11, "bold"), bg="blue", fg="white")  # Adjusted width and font size
        showAll_btn.grid(row=0, column=3,padx=4)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=195, width=670, height=320)  # Adjusted size


        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table=ttk.Treeview (table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
 
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)


# ====================Function declaration=======================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            pass

        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

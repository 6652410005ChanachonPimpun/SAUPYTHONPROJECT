# OOP
class DtiSau :
    # data/property member ค่าข้อมูล
    stu_name = ''
    score = 0
    gpa = 0

    # methon member ค่าการทำงาน
    def histudent(self) :
        print(f'สวัสดี {self.stu_name}')

    def showscoreAndGPA(self) :
        print(f'คะแนน {self.score} ได้ GPA {self.gpa}')

# สร้าง object
obj01 = DtiSau() # ชื่อคลาสที่มี () เราเรียกว่าเป็นการสั่งให้ canstructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.histudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = 3.99



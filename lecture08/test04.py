# self เปรียบเสมือนสิ่งที่ใช้แทนคลาสตัวเอง เพื่อสามารถเรียกใช้ member ในคลาสตัวเองได้ 
class Test04 :
    # data/property member
    data1 = 10

    # constructor
    def __init__(self, data2, data3):
        print('Hi...')
        self.data2 = data2
        self.data3 = data3

    # methon member
    def showSumData(self):
        print(self.data1 + self.data2 + self.data3)
        self.showWow()

    def showWow(self):
        print('wow...wow...wow')

objA = Test04(20, 30)
objB = Test04(10, 20)
objC = Test04(20, 100)
objD = Test04(20, 30)

class DTItest03 :
    # data
    infoA = 10

    # constractor จะเป็นตัวทำให้ object ที่สร้างจากคลาสเดียวกันไม่จำเป็นต้องเหมือนกัน
    # constractor จะทำงานทุกครั้งที่มีการสร้าง object
    def __init__(self, infoB, infoC):
        self.infoB = infoB
        self.infoC =- infoC
        print('wow wow wow...')

    # method
    def showMixandinfo(self, mix) :
        print(self.infoA + self.infoB + self.infoC + mix)

# สร้าง object
sau1 = DTItest03(20, 30)
sau2 = DTItest03(10, 100)
sau3 = DTItest03(20, 30)
class DTItest01 :
    pass

class DTItest02 :
    # data/attribute/property/fleld คือ ตัวแปรประเภทนึง
    infoA = ' '
    infoB = 20

    # method คือ ฟังก์ชันประเภทนึง
    def showHi(self) :
        print('Hi...')

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)

# สร้าง object
objA = DTItest02
objB = DTItest02
sombat = DTItest02

objA.infoA = 'xxxx'
objB.infoB = 100

print(objA.infoB + objB.infoB)

sombat.showInfoAandB

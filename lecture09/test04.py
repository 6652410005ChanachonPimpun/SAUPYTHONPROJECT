# คุณสมบัติ Encapsulation (ห่อหุ่ม data/attribute/field/property)
class DTItest05 :
    # data
    infoA = 10      #ไม่ได้ Encap
    __infoB = 20    # Encap ดูจาก __???? -> เป็นการกำหนด access_modifier เป็น private

    def __init__(self, infoC, infoD) :
        self.infoC = infoC      # ไม่ได้ Encap
        self.__infoD = infoD    # Encap ดูจาก __???? -> เป็นการกำหนด access_modifier เป็น private
    # เมื่อใดก็ตาม Encap จะต้องมีเมธอด 2 ตัวนี้เสมอ คือ get, set ของ data ตัวนั้น
    def setinfoB(self, infoB) :
        self.__infoB = infoB

    def getinfoB(self) :
        return self.__infoB
    
    def setinfoB(self, infoD) :
        self.__infoD = infoD
    
    def getinfoD(self) :
        return self.__infoD
    
    def showinfo(self) :
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print('..................................')

ob1 = DTItest05(30, 40)
ob2 = DTItest05(30, 100)
ob1.showinfo() # 10 20 30 40
ob1.__infoB = 555
ob1.setinfoB(999)
ob1.showinfo()
print(ob1.getinfoB() + ob1.getinfoD())
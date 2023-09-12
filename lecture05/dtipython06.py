# คำสั่ง return ทีไมม่มีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกว่างานนั้นๆ เสร้จแล้ว
def ex() :
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return
#default paramiter
def dtitest(x = 40, y = 30, z = 20, a = 10) : #ถ้ามีต้องไล่จากตัวหลังมาตัวหน้า
    print(f'{x} + {y} + {z} + {a} = {x+y+z+a}')

dtitest(5, 100)

dtitest(4, 5, 6)
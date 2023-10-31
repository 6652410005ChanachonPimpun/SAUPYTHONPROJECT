# คุณสมบัติ Inheritance สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง *** (re-use)
# สืบทอด มีแม่ (super class) มีลูก (sub class)
# แม่มีอะไร ลูกมีด้วย เมื่อมีการสือทอด (Iheritance)

# คุณสมบัติเด่น     Ploymorphise (พ้องรูป:พฤติกรรมเดียวแต่คนละวิธี) คือการที่คลาสลูกเอาเมธอดแม่มาเขียนใหม่

class Sau01 :
    infoA = 10

    def showHi() :
        print('Hi...')

class Sau02(Sau01) : # Inheritance
    infoB = 20

    def showHey() :
        print('Hey...')

    # overiding meshod : Polymorphise
    def showHi() :
        print('Hi Hi Hi...')

ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()

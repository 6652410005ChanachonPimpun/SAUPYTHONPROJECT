# Desturctor

class DTOtest04 :
    data1 = 10

    def __init__(self, data2) :
        self.data2 = data2
        print('Hi...')

    def dotask1(self) :
        print('^_^')

    def dotask2(self, value) :
        print(value)

    # destructor
    def __del__(self) :
        print('Bye bye...')

#...................................
sauA = DTOtest04(20)
sauB = DTOtest04(30)
sauC = DTOtest04(20)

sauC.dotask2('T_T')
sauC.dotask1()
print(sauA.data1 + sauB.data1)

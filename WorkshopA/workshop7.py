def inputN() :
    number = float(input('ป้อนตัวเลข :'))
    return number

def cal(number) :
    if number == 25 :
        print('Correct, You are the winner')
    else :
        print('Not Correct !!!.')

def show(SW) :
    return SW

print('.............................')
number = inputN()
SW = cal(number)
show(SW)
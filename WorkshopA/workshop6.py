def inputN() :
    name = input('ชื่อผู้กู้ :')
    return name

def inputM() :
    money = float(input('ป้อนจำนวนเงินกู้ :'))
    return money

def cal(money) :
    if money > 1000 :
        more = money * (2.5/100)
        print(f'ดอกเบี้ยเมื่อกู้เงินมากกว่า 1000 = {more}')
    else :
        less = money * (5.5/100)
        print(f'ดอกเบี้ยเมื่อกู้เงินน้อยกว่า 1000 = {less}')

print('..............................')
name = inputN()
money = inputM()
cal(money)

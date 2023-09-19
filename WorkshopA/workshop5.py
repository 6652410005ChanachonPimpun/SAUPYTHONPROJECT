def inputN() :
    pas = input('ป้อนรหัสพนักงาน :')
    name = input('ป้อนชื่อพนักงาน :')
    return pas, name

def inputM() :
    money = float(input('เงินเดือนปกติ :'))
    return money

def caltotal(money) :
    total = money - (money * 7/100)- 500
    print(f'เงินเดือนสุทธิของพนักงาน เมื่อหักภาษีและค่าประกันสังคมแล้ว = {total}')

print('...........................')
pas, name = inputN()
money = inputM()
caltotal(money)
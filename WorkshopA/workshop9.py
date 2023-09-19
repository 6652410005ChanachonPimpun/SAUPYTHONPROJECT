def inputname() :
    pas = input('ป้อนรหัสพนักงาน :')
    name = input('ป้อนชื่อพนักงาน :')
    return pas, name

def inputmon() :
    money = float(input('ป้อนยอดขายพนักงาน :'))
    return money

def cal(money) :
    if money < 1000 :
        print('ได้ค่าคอมมิชชั่น 0 บาท')
    elif money > 1001 and money < 2000 :
        one = money * 1/100
        print(f'ได้ค่าคอมมิชชั่น {one} บาท')
    elif money > 2001 and money < 3000 :
        two = money * 3/100 
        print(f'ได้ค่าคอมมิชชั่น {two} บาท')
    elif money > 3001 :
        tree = money * 5/100
        print(f'ได้ค่าคอมมิชชั่น {tree} บาท')

print('..........................')
pas, name = inputname()
money = inputmon()
cal(money)
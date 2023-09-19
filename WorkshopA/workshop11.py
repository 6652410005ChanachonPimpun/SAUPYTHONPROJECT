def inputname() :
    name = input('ป้อนชื่อผู้ใช้ :')
    num = input('ป้อนเบอร์โทรศัพท์ :')
    return name, num

def inputmin() :
    mini = float(input('ป้อนจำนวนนาทีที่ใช้ :'))
    return mini

def cal(mini) :
    if mini >= 1 and mini <= 15 :
        one = mini * 5
        print(f'ค่าโทรศัพท์ = {one} บาท')
    elif mini >= 16 and mini <= 30 :
        two = mini * 3
        print(f'ค่าโทรศัพท์ = {two} บาท')
    elif mini > 31 :
        tree = mini * 1.5
        print(f'ค่าโทรศัพท์ = {tree}')

print('........................')
name, num = inputname()
mini = inputmin()
cal(mini)
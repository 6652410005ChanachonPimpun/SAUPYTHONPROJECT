def inputname() :
    name = input('ป้อนชื่อหัวหน้ากรุ๊ปทัวร์ :')
    pho = input('ป้อนเบอร์ติดต่อหัวหน้ากรุ๊ปทัวร์ :')
    return name, pho

def inputnum() :
    num = float(input('ป้อนจำนวนคนที่จะไปทัวร์ :'))
    return num

def cal(num) :
    if num <= 2 :
        one = num * 300
        print(f'ราคาแพ็กเกจทั้งหมด {one} บาท')
    elif num >= 3 and num <= 5 :
        two = num * 250
        print(f'ราคาแพ็กเกจทั้งหมด {two} บาท')
    elif num >= 6 and num <= 10 :
        tree = num * 210
        print(f'ราคาแพ็กเกจทั้งหมด {tree} บาท')
    elif num >= 11 :
        four = num * 150
        print(f'ราคาแพ็กเกจทั้งหมด {four} บาท')

print('.........................')
name, pho = inputname()
num = inputnum()
cal(num)
def inputname():
    id = input('รหัสนักเรียน :')
    name = input('ชื่อนักเรียน :')
    num = float(input('เกรดเฉลี่ยนักเรียน :'))
    return id, name, num

def cal(id, name, num):
    if num > 2.00:
        print(f'นักเรียนรหัส {id} ชื่อ {name} ได้เกรดเฉลี่ย {num} สอบผ่าน')
    else:
        print(f'นักเรียนรหัส {id} ชื่อ {name} ได้เกรดเฉลี่ย {num} สอบไม่ผ่าน')

def show():
    students = int(input("ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: "))

    for i in range(students):
        id, name, num = inputname()
        result = cal(id, name, num)
        print(result)

show()
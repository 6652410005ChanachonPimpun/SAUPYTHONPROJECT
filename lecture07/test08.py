var2 = (10, 20, 'Hello', True, (111, 'wow'), 'สมชาย')

# การเปลี่ยนแปลงค่า เพิ่ม ลบ ข้อมูล ใน Tuple
# List(), Tuple()
vartemp = list(var2)
vartemp[2] = 'Hi'
var2 = tuple(vartemp)
print(var2)
# เขียนข้อมูลลงไฟล์
f_dti = open('myfile02.txt', 'x', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti.write('wasd...')
f_dti.write('ooo...\n')
f_dti.write('ครับ...\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')
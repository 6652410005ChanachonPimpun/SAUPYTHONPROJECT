# เขียนข้อมูลลงไฟล์
f_dti = open('myfile03.txt', 'a', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('kk...')
f_dti.write('pp...\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว')
def inputname() :
    pas = input('ป้อนรหัสนักเรียน :')
    name = input ('ป้อนชื่อนักเรียน :')
    return pas, name

def inputS1() :
    S1 = float(input('ป้อนคะแนนสอบครั้งที่ 1 :'))
    S2 = float(input('ป้อนคะแนนสอบครั้งที่ 2 :'))
    S3 = float(input('ป้อนคะแนนสอบครั้งที่ 3 :'))
    return S1, S2, S3

def Cal(S1, S2, S3) :
    n = [S1, S2, S3]
    total = sum(n)/len(n)
    print(f'นักเรียนรหัส {pas} ชื่อ {name} สอบครั้งที่ 1 ได้ {S1} สอบครั้งที่ 2 ได้ {S2} สอบครั้งที่ 3 ได้ {S3}')
    print(f'ค่าเฉลี่ยคะแนนของนักเรียนคนนีคือ {total}')

print('..........................')
pas, name = inputname()
S1, S2, S3 = inputS1()
Cal(S1, S2, S3)

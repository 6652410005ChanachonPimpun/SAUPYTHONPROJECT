def inputN() :
    name = input('ชื่อจังหวัด :')
    return name

def inputNM() :
    number = float(input('ป้อนค่า PH :'))
    return number

def cal(number) :
    if number >= 7 and number < 8 :
        print('Result is Normal')
    elif number > 8 :
        print('Result is Acid')
    elif number < 7 :
        print('Result is Alkali')

print('............................')
name = inputN()
number = inputNM()
cal(number)
def XXX() :
    x = float(input('ค่า x :'))
    return x

def cal() :
    y = 2*(x)**2 + 2*(x) + 1
    return y

def show(y, x) :
    print(f'แก้สมการเมื่อx = {x} จะได้ {y}')

print('..............................')
x = XXX()
y = cal()
show(y, x)
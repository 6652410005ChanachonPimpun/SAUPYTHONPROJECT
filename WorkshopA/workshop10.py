def inputY() :
    year = int(input('ป้อนชั้นปี :'))
    return year

def cal(year) :
    if year == 1 :
        print('Welcome Freshman')
    elif year == 2 :
        print('Welcome Sophomore')
    elif year == 3 :
        print('Welcome Junior')
    elif year == 4 :
        print('Welcome Senior')

def show(TT) :
    return TT

print('..........................')
year = inputY()
TT = cal(year)
show(TT)
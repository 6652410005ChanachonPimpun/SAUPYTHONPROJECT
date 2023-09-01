pas = input('รหัสพนักงาน = ')
name = input('ชื่อพนักงาน = ')
mon = float(input('เงินเดือนปกติ = '))
total = mon - (mon * 7/100) - 500
print('รหัสพนักงาน',pas,'ชื่อพนักงาน',name,'เงินเดือนปกติ',mon)
print('เงินเดือนสุทธิของพนักงาน',total)
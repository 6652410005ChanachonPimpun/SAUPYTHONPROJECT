#โปรแกรมพื้นทีวงกลม เส้นรอบวง และปริมาตรทรงกลม  จากรัสมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ทำ 5 ฟังชั่น
#inputRadius
import math
def inputRadius() :
    r = input('ป้อนรัศมี :')
    return r

#calareacircle
def calareacircle( r ) :
    return math.pi * math.pow(r, 2)

#calroundcircle 2 * pi * r
def calroundcircle( r ) :
    return 2 * math.pi * r

#calcubecircle 4/3 * pi * r * r * r
def calcubecircle( r ) :
    return 4/3 * math.pi * r * r * r

#show
def show() :
    a = calareacircle
    print(f'พื้นที่วงกลม {calareacircle(a)} เส้นรอบวง ')
#โปรแกรมคำนวนหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์ และแสดงผลพื้นที่สามเหลี่ยมที่คำนวนได้ทางหน้าจอ

#มองหา feature การทำงานว่ามีอะไรบ้าน
#1. รับค่า ฐาน สูง
#2. คำนวนพื้นที่ และแสดงผล   

def inputBaseHigh() :
    base = float(input('ป้อนฐาน :'))
    high = float(input('ป้อนสูง :'))
    return base, high

def calAndShowTriangleArea(base, high) :
    area = base * high / 2
    print(f'สามเหลี่ยมฐาน {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}')

print('............................')
print('Calaulate Triangle Area')
print('............................')
base, high = inputBaseHigh()
print('............................')
calAndShowTriangleArea(base, high)
print('............................')
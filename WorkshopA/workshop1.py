def inputname() : 
    name = input('ป้อนชื่อสินค้า :')
    return name

def inputprice() :
    price = float(input('ป้อนราคาต้นทุน :'))
    return price

def caltotal(name, price) :
    total = price + (price * 10/100)
    print(f'ราคาขายของ {name} ตือ {total} บาท')

print('.....................')
name = inputname()
price = inputprice()
caltotal(name, price)
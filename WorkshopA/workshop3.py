def inputname() :
    name = input('ป้อนชื่อสินค้า :')
    return name

def inputprice() :
    price = float(input('ป้อนราคาสินค้า :'))
    return price

def cal(price) :
    total = price * (7/100)
    print(f'สินค้า {name} มีราคา {price} บาท จะมีภาษี {total:.2f} บาท')

print('............................')
name = inputname()
price = inputprice()
cal(price)
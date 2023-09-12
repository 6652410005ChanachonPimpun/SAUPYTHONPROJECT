#cast/conversion คำดอาไว้แปลข้อมูล
def mp() :
    m = float(input('ป้อนเงิน :'))
    p = int(input('ป้อนคน :'))
    return m, p

def cal(m, p) :
    num = format(float(m),'.2f')
    print(f'จำนวนเงิน {m:.2f} บาท คน {p} คน แชร์คนละ {round(m/p,)} บาท')
    print('จำนวนเงิน', num, 'บาท', 'คน', p, 'คน', 'แชร์คนละ', round(m/p), 'บาท')
    print('จำนวนเงิน ' + str(num) + ' บาท ' + 'คน ' + str(p) + ' คน ' +'แชร์คนละ ' + str(round(m/p)) +' บาท ')
    print('จำนวนเงิน {:.2f} บาท คน {} คน แชร์คนละ {} บาท'.format(m, p, round(m/p)))
    print('จำนวนเงิน %.2f บาท คน %d คน แชร์คนละ %s บาท'%(m, p, round(m/p)))

m, p = mp()
cal(m, p)
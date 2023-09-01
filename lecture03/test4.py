p = int(input("จำนวนคน : "))
m = float(input("จำนวนเงิน : "))

h = float(m / p)
x = format(float(h), ".2f")
print(f"จำนวนคน {p} หารคนละ {x} บาท ")
print("จำนวนคน", p, "หารคนละ", x, "บาท")
print("จำนวนคน" + " " + str(p) + " " + "หารคนละ" + " " + str(x) + " " + "บาท")
print("จำนวนคน {} หารคนละ {:.2f} บาท".format(p, h))
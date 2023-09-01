cc = float(input("อุณหภูมิ C: "))
ff = 9 / 5 * cc + 32

c = format(float(cc), ".2f")
f = format(float(ff), ".2f")

print(f"อุณหภูมิ {cc:.2f} C แปลงเป็นฟาเรนไฮด์ได้ {ff:.2f} F ")
print("อุณหถูมิ", c, "C", "แปลงเป็นฟาเรนไฮด์ได้", f, "F")
print("อุณหถูมิ" + " " + c + " C " + "แปลงเป็นฟาเรนไฮด์ได้" + " " + str(f) + " " + "F")
print("อุณหถูมิ {:.2f} C แปลงเป็นฟาเรนไฮด์ได้ {:.2f} F".format(cc, ff))
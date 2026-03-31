# รับค่าตัวเลขจากผู้ใช้
num1 = float(input("ใส่ตัวเลขแรก: "))
op = input("เลือกเครื่องหมาย (+, -, *, /): ")
num2 = float(input("ใส่ตัวเลขที่สอง: "))

# ส่วนการคำนวณ
if op == "+":
    print(f"คำตอบ: {num1 + num2}")
elif op == "-":
    print(f"คำตอบ: {num1 - num2}")
elif op == "*":
    print(f"คำตอบ: {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"คำตอบ: {num1 / num2}")
    else:
        print("Error: ไม่สามารถหารด้วยศูนย์ได้!")
else:
    print("เครื่องหมายไม่ถูกต้อง")
# Nhập vào từ bàn phím hai số thực number1, number2. Hãy in ra tổng, hiệu, tích, thương, chia nguyên, chia lấy dư, lũy thừa của hai số đó
number1 = float(input("Nhập vào số thực đầu tiên: "))
number2 = float(input("Nhập vào số thực thứ hai: "))

sum = number1 + number2
hieu = number1 - number2
multi = number1 * number2
divide = number1 / number2
chia_nguyen = number1 // number2
so_du = number1 % number2
luy_thua = number1 ** number2
print("Tổng 2 số là:", sum)
print("Hiệu 2 số là:", hieu)
print("chia nguyên:", chia_nguyen)
print("chia lấy dư:", so_du)
print("lũy thừa:", luy_thua)

"""
Dự đoán kết quả của các biểu thức so sánh sau:
'a' > 'b' False
3.0 > 3 False
'' <= ' ' True
.5 > 1 False
"""

"""
0 and 1 : 0
'' or None : None
3 and 4 or 0 : 4
'a' or '1' : a
not None : True
not 0 : True
""" 
print('' or None)

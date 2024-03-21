# 03/3/2023
# Cài tự động định dạng lại file: autopep8, Back,
# https://code.visualstudio.com/docs/python/formatting#_choose-a-formatter

# Toán tử số học
"""
Các toán tử
+ - * / // ** %
/ => kết quả trả về số thực
// => kết quả trả về int, lấy phần nguyên
"""
number1 = 11
number2 = 4
print(number1 / number2)
print(number1 // number2)

# hàm round
# Nếu ko có số lượng số sau dấu phẩy thì sẽ làm tròn
print(round(number1 / number2))
# Có số lượng chữ số sau dấu phẩy
print(round(number1 / number2, 2))
# round của số chẵn thì làm tròn xuống, số lẻ thì làm tròn lên
# search: python round half even

# mũ  **
print(0**0)
print((-0.125) ** 0)

# Thứ tự ưu tiên trong python: python  precedence order

# % chia lấy phần dư
print(number1 % number2)

# lấy ra số cuối cùng của 1 số
number = 1234
print(number % 10)

# Toán tử so sánh <, <, >=,<=, ==, != => trả về giá trị bool

print("a" > "b")  # từ so sánh chữ đổi thành so sánh mã ASCII
print(ord("a"))

# toán tử logic: not > and > or
print(1 > 2 and 4 > 5)  # False and False = F
print(2 > 1 or 1 > 2)  # True or False = True
print(not True)  # False

# các trường hợp đặc biệt
# and sẽ trả về giá trị đầu tiên nếu nó là False ngược lại trả về giá trị thứ 2
# falsy: 0, 0.0 0j, None (). [], set(),'' (các chuỗi trống)
print(0 and 2)

# or
# or sẽ trả về giá trị đầu tiên nếu nó là True ngược lại trả về giá trị thứ 2

print(0 or 2)

print("" or None)  # None

# not luôn trả về True False
print(''<= ' ')

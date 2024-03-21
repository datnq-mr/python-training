"""
01/3/2023
+ Kiểu dữ liệu
+ Biến
+ hàm input
"""
# type - Xác định kiểu dữ liệu của giá trị truyền vào nó
# value: -1, 3, "Hai", "Thinh", True, False, 1j (j^2 = -1)
print(type(3))
print(type(-1.5))
print(type(True))
print(type(1j)) # a + bj với a phần thực, b phần ảo, j^2 =-1
print(type(''))

# Biến- Một tên đại diện cho 1 đối tượng, Theo C là một vùng nhớ đc đặt tên
"""# Quy tắc đặt tên biến:
- Không bắt đầu bằng số
- Không bao gồm ký tự đặc biệt
- Biến phải có ý nghĩa
- Nên đặt theo tiếng Anh
"""
age = 100
birth_year = 2012 # đặt tên biến kiển snake case
_ = 4.5 # _ cũng có thể là tên biến
print(_)

# input dùng để lấy dữ liệu từ người dùng thông qua bàn phím
# hàm input luôn trả về 1 chuỗi ký tự
# Muốn nhập vào số nguyên thì phải ép kiểu

# 1 chuỗi nháy '' trong 1 chuỗi nháy ""
# đặt dấu \ sẽ thay đổi ý nghĩa của ký tự ' hoặc ""
sentence = "I\"m Dat"

num = input("Nhap vao mot so: ")
print(num * 5)
# chưa đổi kiểu thì sẽ in thành 55555
#num_as_int = int(num)
#print(num_as_int * 5)

# lưu ý: Thực hiện tính toán xong hết mới print

# trick: để nhập cả số nguyên, số thực dùng hàm eval: đánh giá biểu thức nằm trong chuỗi thành giá trị cụ thể
#num_as_any = eval(num)
#print(num_as_any * 5)

# Muốn cộng chuỗi vs số thì phải ép về cùng kiểu chuỗi
age = int(input("age: "))
print("I'm " + str(age))

# Tài liệu chuẩn trên doc của hãng: docs.python.org
# khi có thắc mắc dùng stackoverflow
# Đọc thêm ở daynhauhoc.com, rất nhiều người trả lời chi tiết về vấn đề nào đó, do người ta tìm hiểu sâu
# Down dữ liệu từ kaggle
# các thư viện của python ở trang pypi.org

""" khác nhau giữa vscode và jupyter:
- vscode chạy cả file
- jupyter chạy từng ô
"""

# luyện tập lập trình: hackerRank

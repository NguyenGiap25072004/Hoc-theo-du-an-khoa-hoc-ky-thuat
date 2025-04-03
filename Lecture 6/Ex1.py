""" 
Lecture 7 - Python: Package Manager, List Comprehensions, Generator Compressions

7.1: Package Manager

7.1.1. Package Manager là gì?
Công cụ giúp cài đặt, quản lý và cập nhật các thư viện Python (ví dụ: pip).
Tích hợp với Python Package Index (PyPI).

7.1.2. Cài đặt và sử dụng pip
Kiểm tra phiên bản:
pip --version


Cài đặt thư viện:
pip install numpy


Cập nhật thư viện:
pip install --upgrade numpy


Xem danh sách thư viện đã cài:
pip list

7.1.3. 

7.1.3.1. Ví dụ
Cài đặt requests để gọi API:
pip install requests

import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200

7.1.3.2. Thực hành
Cài đặt thư viện pandas và kiểm tra phiên bản của nó bằng code.

7.2. List Comprehensions
7.2.1. List Comprehensions là gì?
Cách ngắn gọn để tạo danh sách từ một iterable trong Python.
Cú pháp: [expression for item in iterable if condition].

7.2.2. Ví dụ code
Tạo danh sách bình phương các số từ 0 đến 9:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


Lọc số chẵn từ 0 đến 10:
evens = [x for x in range(11) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10]

7.2.3. So sánh với vòng lặp truyền thống
Vòng lặp:
evens = []
for x in range(11):
    if x % 2 == 0:
        evens.append(x)


List Comprehension: ngắn hơn, dễ đọc hơn.

7.2.4. Bài tập
Viết List Comprehension để tạo danh sách các số lẻ từ 1 đến 20.
Tạo danh sách các chuỗi "Hello" lặp lại 5 lần.

7.3. Generator Expressions
7.3.1. Generator Expressions là gì?
Tương tự List Comprehensions nhưng tạo ra một generator thay vì danh sách.
Tiết kiệm bộ nhớ vì không lưu toàn bộ dữ liệu cùng lúc.
Cú pháp: (expression for item in iterable if condition).

7.3.2. Ví dụ
Tạo generator bình phương các số:
squares_gen = (x**2 for x in range(5))
print(squares_gen)  # Output: <generator object ...>
print(list(squares_gen))  # Output: [0, 1, 4, 9, 16]


Sử dụng với next():
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # Output: 0
print(next(squares_gen))  # Output: 1

7.3.3. So sánh với List Comprehension
List Comprehension: [x**2 for x in range(5)] → Tạo toàn bộ danh sách ngay lập tức.
Generator Expression: (x**2 for x in range(5)) → Tạo từng giá trị khi cần.

7.3.4. Bài tập
Viết Generator Expression để tạo các số chia hết cho 3 từ 0 đến 15.
Sử dụng next() để lấy 2 giá trị đầu tiên từ generator trên.

BÀI TẬP
1. Cài đặt thư viện matplotlib và vẽ một đồ thị đơn giản (tìm code mẫu trên web nếu cần).
2. Dùng List Comprehension để tạo danh sách các số từ 1 đến 100 chia hết cho cả 3 và 5.
3. Dùng Generator Expression để tạo các số nguyên tố từ 1 đến 20 và in từng số bằng next().

"""




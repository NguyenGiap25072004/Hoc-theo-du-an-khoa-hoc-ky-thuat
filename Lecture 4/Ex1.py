'''Phần 1: Recursion (Đệ quy)

    1.1. Tính giai thừa bằng đệ quy. Viết hàm đệ quy để tính giai thừa của n (n! = n * (n-1)!).

    1.2. Tìm số Fibonacci thứ n bằng đệ quy. Viết hàm đệ quy để tìm số Fibonacci thứ n (F(n) = F(n-1) + F(n-2)).

    1.3. Đảo ngược chuỗi bằng đệ quy. Viết hàm đệ quy để đảo ngược chuỗi, bằng cách hoán đổi ký tự đầu và cuối.

    1.4. Tìm tổng của một mảng bằng đệ quy. Viết hàm đệ quy để tính tổng các phần tử trong danh sách.

    1.5. Kiểm tra chuỗi đối xứng (Palindrome) bằng đệ quy. Viết hàm đệ quy để kiểm tra xem chuỗi có giống nhau khi đọc ngược không.'''
    
# 1.1. Tính giai thừa bằng đệ quy. Viết hàm đệ quy để tính
# giai thừa của n (n! = n * (n-1)!).
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 1.2. Tìm số Fibonacci thứ n bằng đệ quy. Viết hàm đệ quy để
# tìm số Fibonacci thứ n (F(n) = F(n-1) + F(n-2)).
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 1.3. Đảo ngược chuỗi bằng đệ quy. Viết hàm đệ quy để đảo
# ngược chuỗi, bằng cách hoán đổi ký tự đầu và cuối.
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

# 1.4. Tìm tổng của một mảng bằng đệ quy. Viết hàm đệ quy để
# tính tổng các phần tử trong danh sách.
def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])

# 1.5. Kiểm tra chuỗi đối xứng (Palindrome) bằng đệ quy. Viết
# hàm đệ quy để kiểm tra xem chuỗi có giống nhau khi đọc ngược không.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test các hàm

# 1.1. Tính giai thừa của n
n = 5
print(f"Giai thừa của {n} là {factorial(n)}")

# 1.2. Tìm số Fibonacci thứ n
n = 6
print(f"Số Fibonacci thứ {n} là {fibonacci(n)}")

# 1.3. Đảo ngược chuỗi
s = "hello"
print(f"Chuỗi {s} sau khi đảo ngược là {reverse_string(s)}")

# 1.4. Tính tổng các phần tử trong mảng
arr = [1, 2, 3, 4, 5]
print(f"Tổng các phần tử trong mảng {arr} là {sum_array(arr)}")

# 1.5. Kiểm tra chuỗi đối xứng
s = "abba"
print(f"Chuỗi {s} {'là' if is_palindrome(s) else 'không là'} chuỗi đối xứng")
s = "hello"
print(f"Chuỗi {s} {'là' if is_palindrome(s) else 'không là'} chuỗi đối xứng")


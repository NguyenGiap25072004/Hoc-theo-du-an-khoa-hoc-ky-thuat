'''Bài 4: Dãy Fibonacci bằng quy hoạch động
Viết chương trình nhập vào số n và tính số Fibonacci thứ bằng quy hoạch động để tối ưu hiệu suất.
Gợi ý:
● Fibonacci: . F(n)=F(n-1)+F(n-2)F(n), 𝑣ớ𝑖 F(0)=0,F(1)=1
● Dùng mảng để lưu các giá trị đã tính trước đó để tránh tính toán lại.'''

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def main():
    try:
        n = int(input("Nhập vào số n: "))
        if n < 0:
            raise ValueError("Số nhập vào phải là số nguyên không âm.")
        result = fibonacci(n)
        print(f"Số Fibonacci thứ {n} là: {result}")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

print("Chương trình tính số Fibonacci thứ n bằng quy hoạch động")
main()

'''Bài 2: Tính giai thừa của một số
Viết chương trình nhập vào một số nguyên không âm nnn và tính n! (giai thừa của nnn).
Gợi ý:
● Công thức: . n!=nx(n-1)x...x1
● Giai thừa của 0 là 1.'''

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)

def main():
    try:
        n = int(input("Nhập một số nguyên không âm: "))
        if n < 0:
            raise ValueError("Số nhập vào phải là số nguyên không âm.")
        ketqua = giaithua(n)
        print(f"Giai thừa của {n} là: {ketqua}")
    except ValueError:
        print("Số nhập vào không hợp lệ. Vui lòng nhập một số nguyên không âm.")

print("Chương trình tính giai thừa của một số nguyên không âm")
main()


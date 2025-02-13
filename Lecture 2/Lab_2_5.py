'''Viết hàm kiểm tra xem một số có phải là số nguyên tố hay không ?'''

def lasonguyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhap vao so nguyen duong n: "))
print("So n co phai la so nguyen to khong?", lasonguyento(n))


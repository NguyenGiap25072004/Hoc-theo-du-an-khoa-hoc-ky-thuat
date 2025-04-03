"""Bài 1: Viết một chương trình nhập vào một số nguyên dương n và kiểm tra xem nó có phải là số nguyên tố hay không. Gợi ý:
+ Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
+ Có thể kiểm tra từ 2 đến căn bậc hai của n"""

def songuyento(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input("Nhập vào một số nguyên dương n: "))
        if n < 0:
            print("Vui lòng nhập một số nguyên dương.")
            return
        if songuyento(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên dương.")
        

print("Chương trình kiểm tra số nguyên tố")
main()


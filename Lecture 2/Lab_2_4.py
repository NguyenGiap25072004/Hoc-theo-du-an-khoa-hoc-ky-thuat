'''Nhập vào một số nguyên từ người dùng, nếu không phải số nguyên thì in ra thông báo lỗi "Please enter a valid number'''
a = input("Nhập vào một số nguyên a: ")
try:
    a = int(a)
    print("Số a là số nguyên")
except:
    print("Please enter a valid number")
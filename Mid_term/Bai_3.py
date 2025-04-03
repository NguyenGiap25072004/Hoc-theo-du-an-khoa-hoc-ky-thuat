'''Bài 3: Sắp xếp mảng bằng thuật toán Bubble Sort
Viết chương trình nhập vào một mảng số nguyên và sắp xếp theo thứ tự tăng dần bằng thuật toán Bubble Sort.
Gợi ý:
● Bubble Sort hoạt động bằng cách liên tục hoán đổi hai phần tử liền kề nếu chúng không đúng thứ tự.
● Lặp đi lặp lại cho đến khi mảng được sắp xếp.
Lưu ý: Cần in ra dãy số ở mỗi bước sắp xếp, cho đến khi dãy số đạt trạng thái đã sắp xếp'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                swapped = True
        print(f"Bước {i+1}: {arr}")  
        if not swapped:  
            break

def main():
    try:
        arr = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))
        print(f"Mảng ban đầu: {arr}")
        bubble_sort(arr) 
        print(f"Mảng đã sắp xếp: {arr}")
    except ValueError:
        print("Vui lòng nhập vào một mảng hợp lệ.")
        

print("Chương trình sắp xếp mảng bằng thuật toán Bubble Sort")
main()  
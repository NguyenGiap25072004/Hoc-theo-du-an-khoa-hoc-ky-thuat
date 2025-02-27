'''Phần 3: Sorting Algorithms

    3.1. Cài đặt Quick Sort. Viết thuật toán Quick Sort để sắp xếp danh sách theo thứ tự tăng dần.

    3.2. So sánh thời gian chạy giữa Bubble Sort và Merge Sort. Viết chương trình đo thời gian chạy của hai thuật toán trên một danh sách lớn.'''
    
# 3.1. Cài đặt Quick Sort. Viết thuật toán Quick Sort để sắp xếp danh sách theo thứ tự tăng dần.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 3.2. So sánh thời gian chạy giữa Bubble Sort và Merge Sort. Viết chương trình đo thời gian chạy của hai thuật toán trên một danh sách lớn.
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Test các hàm
arr = random.sample(range(1, 10000), 1000)
print(f"Original array: {arr}")
start_time = time.time()
print(f"Bubble sort: {bubble_sort(arr)}")
t1 = time.time() - start_time
print(f"Time taken for Bubble Sort: {t1}")

arr = random.sample(range(1, 10000), 1000)
print(f"Original array: {arr}")
start_time = time.time()
print(f"Merge sort: {merge_sort(arr)}")
t2 = time.time() - start_time
print(f"Time taken for Merge Sort: {t2}")

if t1 < t2:
    print("Bubble Sort is faster than Merge Sort")
else:
    print("Merge Sort is faster than Bubble Sort")


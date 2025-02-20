# Array
'''
Bài 1: Đảo ngược mảng
Bài 2: Tìm số lớn thứ 2 trong mảng
Bài 3: Xóa phần tử trùng lặp trong mảng
'''

# Bài 1: Đảo ngược mảng

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10]
print("Mảng ban đầu là:", arr)
print("Mảng sau khi được đảo ngược là: ",reverse_array(arr))

# Bài 2: Tìm số lớn thứ 2 trong mảng

def find_second_largest(arr):
    Largest = second_largest = float('-inf')
    for i in arr:
        if i > Largest:
            Largest, second_largest = i, Largest
        elif Largest > i > second_largest:
            second_largest = i
    return second_largest

print("Số lớn thứ 2 trong mảng la:",find_second_largest(arr))    

# Bài 3: Xóa phần tử trùng lặp trong mảng

def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result
'''def remove_duplicates(arr):
    return list(set(arr))'''

print("Mảng sau khi xóa phần tử trùng lặp là: ", remove_duplicates(arr))
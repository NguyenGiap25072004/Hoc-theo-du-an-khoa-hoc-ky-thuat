'''
3. Heap
Bài 5: Triển khai Min-Heap bằng Python
Bài 6: Sắp xếp mảng bằng Heap Sort
'''

# Bài 5: Triển khai Min-Heap bằng Python

class MinHeap:
    def __init__(self):
        self.a = []

    """Insert a new element into the Min Heap."""
    def insert(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i > 0 and self.a[(i - 1) // 2] > self.a[i]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    """Delete a specific element from the Min Heap."""
    def delete(self, value):
        i = -1
        for j in range(len(self.a)):
            if self.a[j] == value:
                i = j
                break
        if i == -1:
            return
        self.a[i] = self.a[-1]
        self.a.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.a) and self.a[left] < self.a[smallest]:
                smallest = left
            if right < len(self.a) and self.a[right] < self.a[smallest]:
                smallest = right
            if smallest != i:
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
                i = smallest
            else:
                break

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.a:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.a[0] if self.a else None

    def printHeap(self):
        print("Min Heap:", self.a)

# Example Usage
if __name__ == "__main__":
    h = MinHeap()
    values = [10, 7, 11, 5, 4, 13]
    for value in values:
        h.insert(value)
    h.printHeap()
    
    h.delete(7)
    print("Heap after deleting 7:", h.a)
    
    print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
    print("Minimum element in heap:", h.getMin())


# Bài 6: Sắp xếp mảng bằng Heap Sort

def heapify(arr, n, i):
    largest = i
    left = 2 * 1 + 1
    right = 2 * 1 + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Nhập mảng từ người dùng
arr = list(map(int, input("Nhap mang:").split()))
print("Mảng sau khi được sắp xếp bằng Heap Sort là: ", heapSort(arr))
    
'''Phần 2: Binary Search Tree (BST)

    2.1. Chèn phần tử vào Binary Search Tree (BST). Viết lớp BST và phương thức insert() để chèn phần tử vào cây.

    2.2. Tìm kiếm một phần tử trong BST. Viết phương thức search() để kiểm tra xem một phần tử có tồn tại trong BST không.

    2.3. Duyệt cây theo thứ tự trung tố (Inorder Traversal). Viết hàm duyệt cây theo thứ tự trung tố để lấy danh sách phần tử theo thứ tự tăng dần.'''
    

# 2.1. Chèn phần tử vào Binary Search Tree (BST). Viết lớp BST và phương thức insert() để chèn phần tử vào cây.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [node.val] + self._inorder_traversal(node.right)
    
# Test các hàm

# Tạo một BST
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Inorder Traversal
print("Inorder Traversal:", bst.inorder_traversal())

# Tìm kiếm một phần tử
print("Search 4:", bst.search(4))

# Tìm kiếm một phần tử không tồn tại
print("Search 9:", bst.search(9))

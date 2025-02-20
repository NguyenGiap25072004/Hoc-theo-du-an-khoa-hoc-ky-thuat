import string
from collections import Counter



'''Viết một chương trình Python để đếm số lần xuất hiện của từng từ trong một đoạn văn bản được người dùng nhập vào từ bàn phím. Sau đó:
1. Loại bỏ dấu câu (ví dụ.,! không được tính là một phần của từ)
2. Không phân biệt chữ hoa, chữ thường ("Python" và "python" được coi là một)
3. Sắp xếp kết quả theo số lần xuất hiện giảm dần
4. Hiển thị n từ xuất hiện nhiều nhất, với n là số do người dùng nhập (Không sử dụng bất kỳ thư viện có sẵn nào)'''
def count_words(text, n):
    # Loại bỏ dấu câu và chuyển đổi tất cả các từ thành chữ thường
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    
    # Tách các từ và đếm số lần xuất hiện của từng từ
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sắp xếp kết quả theo số lần xuất hiện giảm dần
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Hiển thị n từ xuất hiện nhiều nhất
    for word, count in sorted_word_counts[:n]:
        print(f'{word}: {count}')

# Nhập đoạn văn bản và số từ cần hiển thị từ người dùng


text = input("Please text the paragraph you want to count:")
n = int(input("Pleas enter the numbers of words you want to display:"))
count_words(text, n)




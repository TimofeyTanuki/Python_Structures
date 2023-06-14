# Импортируем всё из библиотеки.
from BinaryTreeAVL import *

# Тест АВЛ-дерева дерева.
newBinaryTreeAVL = BinaryTreeAVL()

# Создаём массив вводных данных.
data = [5, 2, 3, 6, 8]

print("data:", data, end = "\n" * 2)
for value in data: newBinaryTreeAVL.insert(value) # Добавляем вводные данные в двоичное дерево.

print("arrayPreorder:", newBinaryTreeAVL.arrayPreorder(), "\nprintPreorder:") # Получение массива из двоичного дерева обходом Preorder.
newBinaryTreeAVL.printPreorder() # Вывод дерева обходом Preorder.
print("\narrayInorder:", newBinaryTreeAVL.arrayInorder(), "\nprintInorder:") # Получение массива из двоичного дерева обходом Inorder.
newBinaryTreeAVL.printInorder() # Вывод дерева обходом Inorder.
print("\narrayPostorder:", newBinaryTreeAVL.arrayPostorder(), "\nprintPostorder:") # Получение массива из двоичного дерева обходом Postorder.
newBinaryTreeAVL.printPostorder() # Вывод дерева обходом Postorder.

print("\ncontains 5:", newBinaryTreeAVL.contains(5)) # Проверяем наличие элемента с значением 5.
print("> remove 5")
newBinaryTreeAVL.remove(5) # Удаляем элемент с значением 5.
print("contains 5:", newBinaryTreeAVL.contains(5)) # Проверяем наличие элемента с значением 5.
print("contains 7:", newBinaryTreeAVL.contains(7)) # Проверяем наличие элемента с значением 7.
print("> insert 7")
newBinaryTreeAVL.insert(7) # Вставляем элемент с значением 7.
print("contains 7:", newBinaryTreeAVL.contains(7)) # Проверяем наличие элемента с значением 7.

print("\narrayPreorder:", newBinaryTreeAVL.arrayPreorder(), "\nprintPreorder:") # Получение массива из двоичного дерева обходом Preorder.
newBinaryTreeAVL.printPreorder() # Вывод дерева обходом Preorder.
print("\narrayInorder:", newBinaryTreeAVL.arrayInorder(), "\nprintInorder:") # Получение массива из двоичного дерева обходом Inorder.
newBinaryTreeAVL.printInorder() # Вывод дерева обходом Inorder.
print("\narrayPostorder:", newBinaryTreeAVL.arrayPostorder(), "\nprintPostorder:") # Получение массива из двоичного дерева обходом Postorder.
newBinaryTreeAVL.printPostorder() # Вывод дерева обходом Postorder.
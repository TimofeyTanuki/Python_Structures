# Импортируем всё из библиотеки.
from BinaryTree import *


# Тест двоичного дерева.
newBinaryTree = BinaryTree()

# Создаём массив вводных данных.
data = [5, 2, 3, 6, 8]

print("data:", data, end = "\n" * 2)
for value in data: newBinaryTree.insert(value) # Добавляем вводные данные в двоичное дерево.

print("arrayPreorder:", newBinaryTree.arrayPreorder(), "\nprintPreorder:") # Получение массива из двоичного дерева обходом Preorder.
newBinaryTree.printPreorder() # Вывод дерева обходом Preorder.
print("\narrayInorder:", newBinaryTree.arrayInorder(), "\nprintInorder:") # Получение массива из двоичного дерева обходом Inorder.
newBinaryTree.printInorder() # Вывод дерева обходом Inorder.
print("\narrayPostorder:", newBinaryTree.arrayPostorder(), "\nprintPostorder:") # Получение массива из двоичного дерева обходом Postorder.
newBinaryTree.printPostorder() # Вывод дерева обходом Postorder.

print("\ncontains 5:", newBinaryTree.contains(5)) # Проверяем наличие элемента с значением 5.
print("> remove 5")
newBinaryTree.remove(5) # Удаляем элемент с значением 5.
print("contains 5:", newBinaryTree.contains(5)) # Проверяем наличие элемента с значением 5.
print("contains 7:", newBinaryTree.contains(7)) # Проверяем наличие элемента с значением 7.
print("> insert 7")
newBinaryTree.insert(7) # Вставляем элемент с значением 7.
print("contains 7:", newBinaryTree.contains(7)) # Проверяем наличие элемента с значением 7.

print("\narrayPreorder:", newBinaryTree.arrayPreorder(), "\nprintPreorder:") # Получение массива из двоичного дерева обходом Preorder.
newBinaryTree.printPreorder() # Вывод дерева обходом Preorder.
print("\narrayInorder:", newBinaryTree.arrayInorder(), "\nprintInorder:") # Получение массива из двоичного дерева обходом Inorder.
newBinaryTree.printInorder() # Вывод дерева обходом Inorder.
print("\narrayPostorder:", newBinaryTree.arrayPostorder(), "\nprintPostorder:") # Получение массива из двоичного дерева обходом Postorder.
newBinaryTree.printPostorder() # Вывод дерева обходом Postorder.
# Импортируем всё из библиотеки.
from BinaryHeap import *


# Тест двоичной кучи, упорядоченной по убыванию.
newBinaryHeap = BinaryHeap(False)

# Создаём массив вводных данных и определяем его длину.
data = [5, 16, 14, 24, 3, 7, 10, 13, 6, 1, 2, 29]
data_length = len(data)

print("data:", data, end = "\n" * 2)
newBinaryHeap.fromArray(data, data_length) # Преобразуем исходный массив в двоичную кучу.
print("print:", newBinaryHeap)
print("> extractTop:", newBinaryHeap.extractTop()) # Извлекаем первый элемент двоичной кучи.
print("print:", newBinaryHeap)
print("> insert 27")
newBinaryHeap.insert(27) # Добавляем новый элемент.
print("print:", newBinaryHeap, "\n" * 3)


# Тест двоичной кучи, упорядоченной по возрастанию.
newBinaryHeap = BinaryHeap(True)

# Создаём массив вводных данных и определяем его длину.
data = [5, 16, 14, 24, 3, 7, 10, 13, 6, 1, 2, 29]
data_length = len(data)

print("data:", data, end = "\n" * 2)
newBinaryHeap.fromArray(data, data_length) # Преобразуем исходный массив в двоичную кучу.
print("print:", newBinaryHeap)
print("> extractTop:", newBinaryHeap.extractTop()) # Извлекаем первый элемент двоичной кучи.
print("print:", newBinaryHeap)
print("> insert 1")
newBinaryHeap.insert(1) # Добавляем новый элемент.
print("print:", newBinaryHeap, "\n" * 3)
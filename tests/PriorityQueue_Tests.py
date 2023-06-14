# Импортируем всё из библиотеки.
from PriorityQueue import *

# Тест очереди с приоритетом.
newPriorityQueue = PriorityQueue()

# Создаём массив вводных данных, содержащий элементы формата (Приоритет, Значение).
data = [(40, "A"), (25, "B"), (30, "C"), (35, "D"), (5, "E")]

print("data:", data, end = "\n" * 2)

for value in data: newPriorityQueue.insert(value) # Добавляем вводные данные в очередь с приоритетом.

print("print:", newPriorityQueue)
print("> insert (1, \"F\")") # Добавляем новый элемент.
newPriorityQueue.insert((1, "F"))
print("> insert (45, \"G\")") # Добавляем новый элемент.
newPriorityQueue.insert((45, "G"))
print("print:", newPriorityQueue)

# Извлекаем элементы, пока очередь не будет пуста.
while not newPriorityQueue.isEmpty():
    print("extract:", newPriorityQueue.extract())
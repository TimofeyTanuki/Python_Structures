"""
    Двоичная куча с упорядочиванием на выбор.
    order = True - Возрастание
    order = False - Убывание
"""

# Класс двоичной кучи.
class BinaryHeap:

    # Инициализация.
    def __init__(self, order = False):
        self.array = []
        self.length = 0
        self.order = order

    # Проверка двоичной кучи на наличие элементов в ней.
    def isEmpty(self):
        return self.length == 0
   
    # Метод сравнения элементов.
    def compare(self, a, b):
        if self.order: return a < b
        else: return a > b

    # Рекурсивный метод для перестройки двоичной кучи с целью восстановления её свойств.
    def heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        selected = index
        if left < self.length and self.compare(self.array[left], self.array[selected]): selected = left
        if right < self.length and self.compare(self.array[right], self.array[selected]): selected = right
        if selected != index:
            self.array[index], self.array[selected] = self.array[selected], self.array[index]
            self.heapify(selected)

    # Вставка элемента.
    def insert(self, item):
        self.array.append(item)
        index = self.length
        self.length += 1
        for index in range((self.length // 2) - 1, -1, -1): self.heapify(index)

    # Извлечение верхнего элемента последовательности с сохранением свойств кучи.
    def extractTop(self):
        if self.isEmpty(): return None
        buffer = self.array[0]
        removed = self.array.pop()
        self.length -= 1
        if not self.isEmpty():
            self.array[0] = removed
            self.heapify(0)
        return buffer

    # Метод для преобразования массива чисел в двоичную кучу.
    def fromArray(self, array, length):
        self.array = array
        self.length = length
        for i in range(length // 2 - 1, -1, -1): self.heapify(i)

    # Изменение строкового представления класса.
    def __str__(self):
        return str(self.array)
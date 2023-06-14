# Класс очереди с приоритетом на базе двоичной кучи.
class PriorityQueue:

    # Инициализация.
    def __init__(self):
        self.array = []
        self.length = 0

    # Рекурсивный метод для перестройки двоичной кучи с целью восстановления её свойств.
    def heapify(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        minimum = index
        if left < self.length and self.array[left][0] < self.array[minimum][0]: minimum = left
        if right < self.length and self.array[right][0] < self.array[minimum][0]: minimum = right
        if minimum != index:
            self.array[index], self.array[minimum] = self.array[minimum], self.array[index]
            self.heapify(minimum)

    # Проверка очереди на наличие элементов в ней.
    def isEmpty(self):
        return self.length == 0

    # Вставка элемента.
    def insert(self, item):
        self.array.append(item)
        self.length += 1
        for index in range((self.length // 2) - 1, -1, -1): self.heapify(index)

    # Извлечение элемента.
    def extract(self):
        if self.isEmpty(): return None
        buffer = self.array[0]
        removed = self.array.pop()
        self.length -= 1
        if not self.isEmpty():
            self.array[0] = removed
            self.heapify(0)
        return buffer

    # Изменение строкового представления класса.
    def __str__(self):
        savedArray = self.array
        savedLength = self.length
        self.array = self.array[:]
        result = []
        for i in range(savedLength):
            result.append(self.extract())
        self.array = savedArray
        self.length = savedLength
        return str(result)
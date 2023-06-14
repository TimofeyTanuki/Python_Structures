# Импортируем всё из заранее подготовленной библиотеки.
from PriorityQueue import *

# Дерево Хаффмана.
class HuffmanTree:

    # Инициализация.
    def __init__(self):
        self.reset()

    # Вставка элемента.
    def insert(self, item):
        self.priorityQueue.insert(item)
        
    # Сброс установленных данных.
    def reset(self):
        self.priorityQueue = PriorityQueue()

    # Построение дерева Хаффмана с установленными данными.
    def build(self):
        while self.priorityQueue.length > 1:
            left = self.priorityQueue.extract()
            right = self.priorityQueue.extract()
            self.priorityQueue.insert((left[0] + right[0], (left, right)))

    # Получение словаря двоичных кодов.
    def getCodesDictionary(self):
        self.build()
        return self.getCodes(self.priorityQueue.array[0][1], dict(), "")

    # Рекурсивный метод генерации двоичных кодов.
    def getCodes(self, item, dictionary, code):
        if type(item[1][1][0]) is tuple: self.getCodes(item[1][1], dictionary, code + "1")
        else: dictionary[item[1][1]] = code + "1"
        if type(item[0][1][0]) is tuple: self.getCodes(item[0][1], dictionary, code + "0")
        else: dictionary[item[0][1]] = code + "0"
        return dictionary
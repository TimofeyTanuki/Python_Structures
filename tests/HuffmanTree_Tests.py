# Импортируем всё из библиотеки.
from HuffmanTree import *

# Тест дерева Хаффмана.
newHuffmanTree = HuffmanTree()

# Создаём массив вводных данных, содержащий элементы формата (Частота, Значение).
data = [(40, "A"), (25, "B"), (30, "C"), (35, "D"), (5, "E")]

print("data:", data, end = "\n" * 2)

for item in data: newHuffmanTree.insert(item) # Добавляем вводные данные в дерево Хаффмана.

# Получаем готовый словарь двоичных кодов.
codesDictionary = newHuffmanTree.getCodesDictionary()

print("getCodesDictionary:", codesDictionary)
# Класс двоичного дерева.
class BinaryTree:
    
    # Инициализация.
    def __init__(self):
        self.root = None

    # Вставка элемента.
    def insert(self, value):
        if self.root: self.root.insert(self.Node(value))
        else:
            self.root = self.Node(value)
            return self.root

    # Удаление узла по значению.
    def remove(self, value):
        self.root = self.root.remove(self.root, value)

    # Проверка наличия в двоичном дереве элемента по значению.
    def contains(self, value):
        if self.root: return self.root.contains(value)
        return False

    # Получение двоичного дерева в виде массива обходом Preorder.
    def arrayPreorder(self):
        if self.root: return self.root.arrayPreorder()
        return []

    # Вывод двоичного дерева обходом Preorder.
    def printPreorder(self):
        if self.root: self.root.printPreorder(0)
        else: print(None)

    # Получение двоичного дерева в виде массива обходом Inorder.
    def arrayInorder(self):
        if self.root: return self.root.arrayInorder()
        return []

    # Вывод двоичного дерева обходом Inorder.
    def printInorder(self):
        if self.root: self.root.printInorder(0)
        else: print(None)

    # Получение двоичного дерева в виде массива обходом Postorder.
    def arrayPostorder(self):
        if self.root: return self.root.arrayPostorder()
        return []

    # Вывод двоичного дерева обходом Postorder.
    def printPostorder(self):
        if self.root: self.root.printPostorder(0)
        else: print(None)
        
    # Класс узла.
    class Node:
        
        # Инициализация.
        def __init__(self, value):
            self.value = value
            self.left = self.right = None

        # Вставка элемента в узел.
        def insert(self, newNode):
            if newNode.value < self.value:
                if self.left is None:
                    self.left = newNode
                else:
                    self.left.insert(newNode)
            else:
                if self.right is None:
                    self.right = newNode
                else:
                    self.right.insert(newNode)

        # Рекурсивный метод для удаление узла по значению.
        def remove(self, node, value):
            if node:
                if value < node.value:
                    node.left = self.remove(node.left, value)
                elif value > node.value:
                    node.right = self.remove(node.right, value)
                else:
                    if node.left is None and node.right is None:
                        node = None
                    elif node.left is None:
                        node = node.right
                    elif node.right is None:
                        node = node.left
                    else:
                        minimum = self.findMinimum(node.right)
                        node.value = minimum.value
                        node.right = self.remove(node.right, minimum.value)
                return node

        # Рекурсивная проверка наличия в узле или его дочерних узлах элемента по значению.
        def contains(self, value):
            if self.value == value: return True
            if self.value > value:
                if self.left: return self.left.contains(value)
            else:
                if self.right: return self.right.contains(value)
            return False

        # Поиск минимального узла, принадлежащего текущему.
        def findMinimum(self, node):
            while node.left is not None:
                node = node.left
            return node

        # Рекурсивный метод получения содержимого узла в виде массива обходом Preorder.
        def arrayPreorder(self):
            if self.left and self.right:
                return [self.value] + self.left.arrayPreorder() + self.right.arrayPreorder()
            elif self.left:
                return [self.value] + self.left.arrayPreorder()
            elif self.right:
                return [self.value] + self.right.arrayPreorder()
            else: return [self.value]
            
        # Рекурсивный вывод содержимого узла обходом Preorder.
        def printPreorder(self, level):
            print(" " * level, self.value, sep = "")
            if self.left: self.left.printPreorder(level + 4)
            if self.right: self.right.printPreorder(level + 4)

        # Рекурсивный метод получения содержимого узла в виде массива обходом Inorder.
        def arrayInorder(self):
            if self.left and self.right:
                return self.left.arrayInorder() + [self.value] + self.right.arrayInorder()
            elif self.left:
                return self.left.arrayInorder() + [self.value]
            elif self.right:
                return [self.value] + self.right.arrayInorder()
            else: return [self.value]
            
        # Рекурсивный вывод содержимого узла обходом Inorder.
        def printInorder(self, level):
            if self.left: self.left.printInorder(level + 4)
            print(" " * level, self.value, sep = "")
            if self.right: self.right.printInorder(level + 4)

        # Рекурсивный метод получения содержимого узла в виде массива обходом Postorder.
        def arrayPostorder(self):
            if self.left and self.right:
                return self.left.arrayPostorder() + self.right.arrayPostorder() + [self.value]
            elif self.left:
                return self.left.arrayPostorder() + [self.value]
            elif self.right:
                return self.right.arrayPostorder() + [self.value]
            else: return [self.value]
            
        # Рекурсивный вывод содержимого узла обходом Postorder.
        def printPostorder(self, level):
            if self.left: self.left.printPostorder(level + 4)
            if self.right: self.right.printPostorder(level + 4)
            print(" " * level, self.value, sep = "")
# Класс АВЛ-дерева.
class BinaryTreeAVL:
    
    # Инициализация.
    def __init__(self, array = None):
        self.root = None
        if array:
            for i in array:
                self.insert(i)

    # Вставка элемента.
    def insert(self, value):
        if self.root: self.notRootInsert(self.root, value)
        else: self.root = self.Node(value)
        
    # Вставка в узел дерева.
    def notRootInsert(self, node, value):
        if node is None:
            return self.Node(value)
        elif value < node.value:
            node.left = self.notRootInsert(node.left, value)
        else:
            node.right = self.notRootInsert(node.right, value)
        heightLeft = self.getHeight(node.left)
        heightRight = self.getHeight(node.right)
        if heightLeft > heightRight: node.height = 1 + heightLeft
        else: node.height = 1 + heightRight
        balance = self.getBalance(node)
        if balance > 1:
            if value < node.left.value:
                return self.rotateNode(node, True)
            if value > node.left.value:
                node.left = self.rotateNode(node.left, False)
                return self.rotateNode(node, True)
        if balance < -1:
            if value < node.right.value:
                node.right = self.rotateNode(node.right, True)
                return self.rotateNode(node, False)
            if value > node.right.value:
                return self.rotateNode(node, False)
        return node

    # Удаление элемента.
    def remove(self, value):
        self.root = self.removeRecursion(self.root, value)
        
    # Рекурсивное удаление узла из дерева.
    def removeRecursion(self, node, value):
        if not node: return node
        elif value < node.value: node.left = self.removeRecursion(node.left, value)
        elif value > node.value: node.right = self.removeRecursion(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minumum = self.findMinimum(node.right)
                node.key = minumum
                node.right = self.removeRecursion(node.right, minumum)

        heightLeft = self.getHeight(node.left)
        heightRight = self.getHeight(node.right)
        if heightLeft > heightRight: node.height = 1 + heightLeft
        else: node.height = 1 + heightRight

        balance = self.getBalance(node)
        if balance > 1:
            if value < node.left.value:
                return self.rotateNode(node, True)
            if value > node.left.value:
                node.left = self.rotateNode(node.left, False)
                return self.rotateNode(node, True)
        if balance < -1:
            if value < node.right.value:
                node.right = self.rotateNode(node.right, True)
                return self.rotateNode(node, False)
            if value > node.right.value:
                return self.rotateNode(node, False)
        return node

    # Получение значения для балансировки.
    def getBalance(self, node):
        if node: return self.getHeight(node.left) - self.getHeight(node.right)
        return 0
    
    # Проверка наличия в АВЛ-дереве элемента по значению.
    def contains(self, value):
        if self.root: return self.root.contains(value)
        return False

    # Получение высоты узла.
    def getHeight(self, node):
        if node: return node.height
        return 0

    # Получение максимальной высоты дочернего узла.
    def compareHeight(self, node):
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        if leftHeight > rightHeight:
            return leftHeight
        return rightHeight

    # Поворот узлов.
    def rotateNode(self, node, clockwise):
        if clockwise:
            root = node.left
            node.left = root.right
            root.right = node
        else:
            root = node.right
            node.right = root.left
            root.left = node
        node.height = 1 + self.compareHeight(node)
        root.height = 1 + self.compareHeight(root)
        if node == self.root:
            self.root = root
        return root

    # Получение АВЛ-дерева в виде массива обходом Preorder.
    def arrayPreorder(self):
        if self.root: return self.root.arrayPreorder()
        return []

    # Вывод АВЛ-дерева обходом Preorder.
    def printPreorder(self):
        if self.root: self.root.printPreorder(0)
        else: print(None)

    # Получение АВЛ-дерева в виде массива обходом Inorder.
    def arrayInorder(self):
        if self.root: return self.root.arrayInorder()
        return []

    # Вывод АВЛ-дерева обходом Inorder.
    def printInorder(self):
        if self.root: self.root.printInorder(0)
        else: print(None)

    # Получение АВЛ-дерева в виде массива обходом Postorder.
    def arrayPostorder(self):
        if self.root: return self.root.arrayPostorder()
        return []

    # Вывод АВЛ-дерева обходом Postorder.
    def printPostorder(self):
        if self.root: self.root.printPostorder(0)
        else: print(None)

    # Класс узла.
    class Node:

        # Инициализация.
        def __init__(self, value):
            self.value = value
            self.right = self.left = None
            self.height = 1
            
        # Рекурсивный вывод содержимого узла обходом Preorder.
        def printPreorder(self, level):
            print(" " * level, self.value, sep = "")
            if self.left: self.left.printPreorder(level + 4)
            if self.right: self.right.printPreorder(level + 4)

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
# Класс неориентированного графа на базе встроенного словаря.
class UnorientedGraph:

    # Инициализация.
    def __init__(self, path = None):
        self.nodes = self.graph = None
        if path: self.loadFromFile(path)

    # Создание графа из файла, содержащего строки формата (Точка 1, Точка 2, Путь).
    def loadFromFile(self, path):
        file = open(path, mode = "r")
        self.nodes = list()
        self.graph = dict()
        while (row := file.readline()):
            values = row.split()
            if values[0] not in self.nodes:
                self.nodes.append(values[0])
            if values[1] not in self.nodes:
                self.nodes.append(values[1])
        file.seek(0)
        for node in self.nodes:
            self.graph[node] = dict()
        while (row := file.readline()):
            values = row.split()
            value = int(values[2])
            self.graph[values[0]][values[1]] = self.graph[values[1]][values[0]] = value
        file.close()
            
    # Получение всех исходящих путей от определённой ячейки.
    def getOutgoingNodes(self, node):
        outgoingNodes = list()
        for outgoingNode in self.nodes:
            if self.graph[node].get(outgoingNode) is not None:
                outgoingNodes.append(outgoingNode)
        return outgoingNodes

    # Изменение строкового представления класса.
    def __str__(self):
        string = "___+" + "".join([node.ljust(5, "_") for node in self.nodes]) + "\n"
        for key, values in self.graph.items():
            string += key.rjust(3, " ") + "|"
            for node in self.nodes:
                string += "{0:5}".format(str(values.get(node)))
            string += "\n"
        return string
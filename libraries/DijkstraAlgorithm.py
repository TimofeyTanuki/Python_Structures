# Импортируем всё из заранее подготовленной библиотеки.
from UnorientedGraph import *

# Класс алгоритма Эдсгера Вибе Дейкстры для нахождения кратчайшего пути графа.
class DijkstraAlgorithm:
    
    # Инициализация.
    def __init__(self, graph, startNode):
        self.graph = graph
        self.startNode = startNode
        self.build()

    # Нахождение кратчайших маршрутов.
    def build(self):
        unvisitedNodes = list(self.graph.nodes)
        self.previousNodes = dict()
        self.shortestPath = dict()
        infinity = float("inf")
        for node in unvisitedNodes: self.shortestPath[node] = infinity
        self.shortestPath[self.startNode] = 0
        while unvisitedNodes:
            minimumNode = unvisitedNodes[0]
            for node in unvisitedNodes:
                if self.shortestPath[node] < self.shortestPath[minimumNode]: minimumNode = node
            outgoingNodes = self.graph.getOutgoingNodes(minimumNode)
            for outgoingNode in outgoingNodes:
                weight = self.shortestPath[minimumNode] + self.graph.graph[minimumNode][outgoingNode]
                if weight < self.shortestPath[outgoingNode]:
                    self.shortestPath[outgoingNode] = weight
                    self.previousNodes[outgoingNode] = minimumNode
            unvisitedNodes.remove(minimumNode)

    # Получение веса кратчайшего маршрута до определённой точки.
    def getWeightToNode(self, targetNode):
        return (self.shortestPath[targetNode])

    # Получение кратчайшего маршрута до определённой точки.
    def getPathToNode(self, targetNode):
        path = list()
        node = targetNode
        while node != self.startNode:
            path.append(node)
            node = self.previousNodes[node]
        return [self.startNode] + list(reversed(path))
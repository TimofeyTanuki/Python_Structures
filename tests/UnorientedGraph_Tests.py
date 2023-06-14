# Импортируем всё из библиотеки.
from UnorientedGraph import *


# Тест класса неориентированного графа.
newUnorientedGraph = UnorientedGraph("TestFiles/Graph.dat") # Загружаем граф из файла.

print("nodes:", newUnorientedGraph.nodes) # Выводим все точки графа.
print("getOutgoingNodes:", newUnorientedGraph.getOutgoingNodes("a")) # Выводим все исходящие пути от точки "a".
print(newUnorientedGraph) # Выводим граф.
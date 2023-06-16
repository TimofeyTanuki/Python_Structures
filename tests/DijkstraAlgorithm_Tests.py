# Импортируем всё из библиотеки.
from DijkstraAlgorithm import *
# Импортируем всё из заранее подготовленной библиотеки.
from UnorientedGraph import * # https://github.com/TimofeyTanuki/Python_Structures

newUnorientedGraph = UnorientedGraph("TestFiles/Graph.dat")
print(newUnorientedGraph) # Выводим граф.
newDijkstraAlgorithm = DijkstraAlgorithm(newUnorientedGraph, "a") # Строим кратчайшие маршруты от точки "a".
print("getWeightToNode:", newDijkstraAlgorithm.getWeightToNode("k")) # Получаем вес кратчайшего пути до точки "k".
print("getPathToNode:", newDijkstraAlgorithm.getPathToNode("k")) # Получаем кратчайший путь до точки "k".

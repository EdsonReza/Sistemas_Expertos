from Node import Node
from Algoritmos.BreadthFirstSearch import BreadthFirstSearch
from Jarra import Jarra

def main():
    # Estado inicial
    inicial = Node((0, 0))
    final = [Node((2, 0)), Node((2, 1)), Node((2, 2)), Node((2, 3))]
    jarra = Jarra(inicial, final)

    bfs = BreadthFirstSearch(jarra)
    solution_bfs = bfs.run()
    print(str(solution_bfs) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))


if __name__ == "__main__":
    main()

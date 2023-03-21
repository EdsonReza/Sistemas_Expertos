from Node import Node
from Algoritmos.BreadthFirstSearch import BreadthFirstSearch
from Jarra import Jarra

def main():
    # Estado inicial
    inicial = Node((0, 0))
    # Posibles estados finales
    final = [Node((2, 0)), Node((2, 1)), Node((2, 2)), Node((2, 3))]

    # Crear el problema, con el estado inicial y el final, y las capacidades de las jarras
    jarra = Jarra(inicial, final, 3, 4)

    bfs = BreadthFirstSearch(jarra)
    solution_bfs = bfs.run()
    print(str(solution_bfs) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))


if __name__ == "__main__":
    main()

from Node import Node
from Algoritmos.BreadthFirstSearch import BreadthFirstSearch
from Algoritmos.DepthFirstSearch import DepthFirstSearch
from Algoritmos.DepthFirstSearchLimited import DepthFirstSearchLimited
from Algoritmos.DepthFirstSearchIterative import DepthFirstSearchIterative
from Jarra import Jarra

def main():
    # Estado inicial
    inicial = Node((0, 0))
    # Posibles estados finales
    final = [Node((8, 0))]

    # Crear el problema, con el estado inicial y el final, y las capacidades de las jarras
    jarra = Jarra(inicial, final, 1, 10)


    print('BFS: \n')
    bfs = BreadthFirstSearch(jarra)
    solution_bfs = bfs.run()
    print(str(solution_bfs) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))

    print('\n\nDFS: \n')
    # La jarra cuenta los nodos, al reutilizar el mismo objeto se debe reiniciar
    jarra.number = 0
    dfs = DepthFirstSearch(jarra)
    solution_dfs = dfs.run()
    print(str(solution_dfs) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))

    print('\n\nDFSL: \n')
    jarra.number = 0
    dfsl = DepthFirstSearchLimited(jarra)
    solution_dfsl = dfsl.run(5)
    print(str(solution_dfsl) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))

    print('\n\nDFSI: \n')
    jarra.number = 0
    dfsi = DepthFirstSearchIterative(jarra)
    solution_dfsi = dfsi.run(2)
    print(str(solution_dfsi) + '\n')
    print('Nodos revisados: ' +  str(jarra.number))

if __name__ == "__main__":
    main()

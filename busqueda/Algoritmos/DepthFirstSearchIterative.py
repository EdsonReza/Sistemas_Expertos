from Jarra import Jarra

class DepthFirstSearchIterative:
    def __init__(self, problem: Jarra):
        self.open = []
        self.close = []
        self.children = []
        self.problem = problem

    def run(self, depth: int):
        limit = depth
        self.open.append(self.problem.initial)
        solution = []
        while self.open:
            actual = self.open.pop()
            print( "Nodo: " + str(self.problem.number) + ", " + str(actual))
            if (actual in self.problem.goal):
                while actual:
                    action = actual.action
                    actual = actual.parent
                    solution.append(action)
                solution.reverse()
                return solution
            else:
                self.close.append(actual)
                print('\n\n' + str(self.open))
                if actual.parent:
                    actual.depth = actual.parent.depth + 1
                else:
                    actual.depth = 0
                if actual.depth <= limit:
                    self.children = self.problem.expand(actual)
                    self.clean()
                    self.open = self.children + self.open
                elif self.open:
                    # No se alcanzó la solución dentro del límite actual, 
                    # pero todavía hay nodos en la lista open, así que continuamos 
                    # explorando los nodos en la lista open
                    continue
                else:
                    # No se alcanzó la solución dentro del límite actual y no quedan 
                    # nodos en la lista open, por lo que reiniciamos el proceso desde 
                    # el estado inicial con un límite incrementado
                    limit += 1
        
        if not self.open and not solution:
            solution = "No hay solución"

    def clean(self):
        for n in self.children[0:]:
            if n in self.open or n in self.close:
                self.children.remove(n)
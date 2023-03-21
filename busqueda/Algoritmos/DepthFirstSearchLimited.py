from Jarra import Jarra
class DepthFirstSearchLimited:
    def __init__(self, problem: Jarra):
        self.open = []
        self.close = []
        self.children = []
        self.problem = problem

    def run(self, depth: int):
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
                if actual.parent:
                    actual.depth = actual.parent.depth + 1
                else:
                    actual.depth = 0
                if actual.depth < depth:
                    self.children = self.problem.expand(actual)
                    self.clean()
                    self.open = self.children + self.open

        if not self.open and not solution:
            solution = "No hay solucion"
    
    def clean(self):
        for n in self.children[0:]:
            if n in self.open or n in self.close:
                self.children.remove(n)
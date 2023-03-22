from Jarra import Jarra

class DepthFirstSearchIterative:
    def __init__(self, problem: Jarra):
        self.open = []
        self.close = []
        self.children = []
        self.problem = problem

    def run(self, value=0):
        depth = value
        while True:
            print("Profundidad: " + str(depth) + "\n")
            result = self.depth_limited_search(depth)
            if result != "cutoff":
                return result
            depth += 1
            print("\n")

    def depth_limited_search(self, depth):
        self.open = [self.problem.initial]
        self.close = []
        while self.open:
            actual = self.open.pop()
            print( "Nodo: " + str(self.problem.number) + ", " + str(actual))
            if (actual in self.problem.goal):
                solution = []
                while actual:
                    action = actual.action
                    actual = actual.parent
                    solution.append(action)
                solution.reverse()
                return solution
            elif actual.depth < depth:
                self.children = self.problem.expand(actual)
                self.clean()
                self.open = self.children + self.open
            else:
                self.close.append(actual)
        return "cutoff"

    def clean(self):
        for n in self.children[0:]:
            if n in self.open or n in self.close:
                self.children.remove(n)
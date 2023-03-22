from Node import Node
class Problem(object):
  
  def __init__(self, initial:Node, goal:Node):

    self.initial = initial
    self.goal = goal
    
  def expand(self, node):
    
    raise NotImplementedError

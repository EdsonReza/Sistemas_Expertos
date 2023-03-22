from Problem import Problem
from Node import Node
class Jarra(Problem):
  def __init__(self, initial:Node, goal:Node, min:int, max:int):
      super().__init__(initial, goal) 
      self.min = min
      self.max = max
  
  number: int = 0

  # Operaciones para desarrollar el nodo
  def expand(self, node:Node):
    children = [] 
    v_la = self.la(node)
    if v_la is not None: 
      self.number += 1
      children.append(v_la)
    
    v_lb = self.lb(node)
    if v_lb is not None: 
      self.number += 1
      children.append(v_lb)

    v_va = self.va(node)
    if v_va is not None: 
      self.number += 1
      children.append(v_va)

    v_vb = self.vb(node)
    if v_vb is not None: 
      self.number += 1
      children.append(v_vb)
    
    v_ba = self.ba(node)
    if v_ba is not None: 
      self.number += 1
      children.append(v_ba)    

    v_ab = self.ab(node)
    if v_ab is not None: 
      self.number += 1
      children.append(v_ab)
    
    return children 
  
  def la(self, node: Node):
    state = node.state 
    if state[0] != 4:
      newState = (self.max, state[1])
      return Node(newState, node, 'Llenar jarra de {0}L'.format(self.max))
    return None 
  
  def lb(self, node: Node):
    state = node.state 
    if state[1] != 3: 
      newState = (state[0], self.min) 
      return Node(newState, node, 'Llenar jarra de {0}L'.format(self.min))
    return None

  def va(self, node: Node): 
    state = node.state 
    if state[0] != 0: 
      newState = (0, state[1]) 
      return Node(newState, node, 'Vaciar jarra de {0}L'.format(self.max))
    return None 
    
  def vb(self, node: Node): 
    state = node.state 
    if state[1] != 0: 
      newState = (state[0], 0) 
      return Node(newState, node, 'Vaciar jarra de {0}L'.format(self.min))
    return None 

  def ab(self, node: Node): 
    state = node.state 
    if state[0] > 0 and state[1] <= self.min: 
      add = self.min - state[1]
      newState = (0, state[1] + state[0]) if add >= state[0] else  (state[0]-add, state[1]+add)
      return Node(newState, node, 'Vaciar jarra de {0}L en jarra de {1}L'.format(self.max, self.min))
    return None 
    
  def ba(self, node: Node): 
    state = node.state 
    if state[1] > 0 and state[0] <= self.max: 
      add = self.max - state[0]
      newState = (state[0] + state[1], 0) if add >= state[1] else (state[0] + add, state[1] - add ) 
      return Node(newState, node, 'Vaciar jarra de {0}L en jarra de {1}L'.format(self.min, self.max))
    return None 

  def hamming_distance(self, state1, state2):
    return sum(1 for s1, s2 in zip(state1, state2) if s1 != s2)
  
  def heuristic(self, node):
    return self.hamming_distance(node.state, self.goal.state)
    

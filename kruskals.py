# Kruskals algorithm implementation in python


class Graph(object):
   def __init__(self, nv):
       self.V = nv
       self.graph = []
  
   def add_edge(self, u, v, w):
       self.graph.append([u, v, w])
  
   def find(self, root, i):
       if root[i] == i:
           return i
       print(i, root[i])
       return self.find(root, root[i])
  
   def union(self, root, rank, x, y):
       print(f"root: {root}, rank: {rank}")
       xroot = self.find(root, x)
       yroot = self.find(root, y)
       if rank[xroot] < rank[yroot]:
           root[xroot] = yroot
       elif rank[xroot] > rank[yroot]:
           root[yroot] = xroot
       else:
           root[yroot] = xroot
           rank[xroot] += 1
       print(f"root: {root}, rank: {rank}")
  

   def kruskals(self):
       result = []
       i, e  = 0, 0
       self.graph = sorted(self.graph, key = lambda item: item[2])
       root = []
       rank = []
       for node in range(self.V):
           root.append(node)
           rank.append(0)
 
  
       while e < self.V - 1:
           u, v, w = self.graph[i]
           i = i + 1
           x = self.find(root, u)
           y = self.find(root, v)
           print(f"x, y: {x}, {y}")
           if x != y:
               e = e + 1
               result.append([u, v, w])
               self.union(root, rank, x, y)
 
       for u, v, w in result:
           print(f'{u} - {v}: {w}')

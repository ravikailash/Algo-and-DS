import random
from make_graph import get_graph

class Graph:
  def __init__(self):
  	self.vertices = set()
  	self.edges = {}
  def add_vertex(self, vertex):
  	if isinstance(vertex, list):
  		self.vertices.update(vertex)
  	else:
  		self.vertices.add(vertex)
  def add_edge(self, u, v):
  	if u in self.edges.keys():
  		self.edges[u].append(v)
  	else:
  		self.edges[u] = [v]

def bfs(g, v=None):
  path = []
  if v is None:
  	v = random.sample(g.vertices, 1)[0]
  queue = [v]
  visited = [False] * len(g.vertices)
  
  while queue:
  	current = queue.pop(0)
  	if visited[current] is False:
  		path.append(current)
  		visited[current] = True
  	for nodes in g.edges.get(current, []):
  		if visited[nodes] is False:
  			queue.append(nodes)
  return path

def dfs_util(g, v, path, visited):
  if visited[v] is False:
  	path.append(v)
  	visited[v] = True
  	for neighbours in g.edges.get(v, []):
  		if visited[neighbours] is False:
  			dfs_util(g, neighbours, path, visited)
  return path

def dfs(g, v=None):
  if v is None:
  	v = random.sample(g.vertices, 1)[0]
  path = []
  visited = [False] * len(g.vertices)
  dfs_util(g, v, path, visited)
  return path

def main():
  g = get_graph(9)
  print('Verices: ', g.vertices)
  print("BFS: ", bfs(g, 0))
  print("DFS: ", dfs(g, 0))

if __name__ == '__main__':
  main()

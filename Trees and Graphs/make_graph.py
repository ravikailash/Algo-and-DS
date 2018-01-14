class Graph:
	"""
	Graph: Directed unweighted graph
	"""
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

class WeightedGraph:
	"""
	Graph: Directed weighted graph
	"""
	def __init__(self):
		self.vertices = set()
		self.edges = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, list):
			self.vertices.update(vertex)
		else:
			self.vertices.add(vertex)

	def add_edge(self, u, v, w):
		if u in self.edges.keys():
			self.edges[u].append([v, w])
		else:
			self.edges[u] = [[v, w]]

# A simple helper function to generate graphs
def get_graph(index=None, weighted=False):
	if index == 9 and weighted is False:
		g = Graph()
		g.add_vertex(list(range(9)))
		g.add_edge(0, 1)
		g.add_edge(0, 7)
		g.add_edge(1, 2)
		g.add_edge(1, 7)
		g.add_edge(2, 3)
		g.add_edge(2, 5)
		g.add_edge(2, 8)
		g.add_edge(3, 4)
		g.add_edge(3, 5)
		g.add_edge(5, 4)
		g.add_edge(7, 8)
		g.add_edge(7, 6)
		g.add_edge(6, 8)
		g.add_edge(6, 5)
		return g
	elif index == 9 and weighted is True:
		g = WeightedGraph()
		g.add_vertex(list(range(9)))
		g.add_edge(0, 1, 4)
		g.add_edge(0, 7, 8)
		g.add_edge(1, 2, 8)
		g.add_edge(1, 7, 11)
		g.add_edge(2, 3, 7)
		g.add_edge(2, 5, 4)
		g.add_edge(2, 8, 2)
		g.add_edge(3, 4, 9)
		g.add_edge(3, 5, 14)
		g.add_edge(5, 4, 10)
		g.add_edge(7, 8, 7)
		g.add_edge(7, 6, 1)
		g.add_edge(6, 8, 6)
		g.add_edge(6, 5, 2)
		return g
	elif index == 8 and weighted is True:
		g = WeightedGraph()
		g.add_vertex(list(range(8)))
		g.add_edge(0, 1, 3)
		g.add_edge(0, 3, 2)
		g.add_edge(0, 7, 4)
		g.add_edge(1, 6, 4)
		g.add_edge(3, 2, 6)
		g.add_edge(2, 5, 1)
		g.add_edge(2, 6, 2)
		g.add_edge(3, 4, 1)
		g.add_edge(7, 4, 8)
		return g
	elif index == 6 and weighted is True:
		g = WeightedGraph()
		g.add_vertex([0, 1, 2, 3, 4, 5])
		g.add_edge(0, 1, 2)
		g.add_edge(0, 2, 3)
		g.add_edge(1, 3, 5)
		g.add_edge(1, 4, 3)
		g.add_edge(1, 2, 6)
		g.add_edge(2, 4, 2)
		g.add_edge(3, 5, 2)
		g.add_edge(3, 4, 1)
		g.add_edge(4, 5, 4)
		return g
	else:
		if weighted is False:
			g = Graph()
			g.add_vertex([0, 1, 2, 3])
			g.add_edge(0, 1)
			g.add_edge(0, 2)
			g.add_edge(2, 0)
			g.add_edge(1, 2)
			g.add_edge(2, 3)
			g.add_edge(3, 3)
		else:
			g = WeightedGraph()
			g.add_vertex([1, 2, 3, 0])
			g.add_edge(0, 1, 10)
			g.add_edge(0, 2, 6)
			g.add_edge(0, 3, 5)
			g.add_edge(1, 3, 15)
			g.add_edge(2, 3, 4)
		return g

if __name__ == '__main__':
	g = get_graph(index, weighted= False)
	print(g.edges)

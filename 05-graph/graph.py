
class Vertex:
    def __init__(self, key, data):
        self.key = key
        self.data = data 
        self.edges = []
        self.parent = None 
        self.color = 'white'
        self.distance = float("inf")

    def add_edge(self, vertex):
        e =Edge(vertex)
        self.edges.append(e)

    def __str__(self):
        s = str(self.key) + ' D:' + str(self.distance)
        for e in self.edges:
            s += ' ' + e.__str__()
        return s
    

class Edge:
    def __init__(self, vertex):
        self.vertex = vertex
        self.weight = 1 

    def __str__(self):
        return '[' + str(self.vertex.key) + ' ' + str(self.weight) +  ']'
    

class Graph:
    def __init__(self):
        self.vertices = {} 
        self.directed = False 

    def initialize_single_source(self):
        for key in self.vertices:
            vertex = self.vertices[key]
            vertex.color = 'white'
            vertex.parent = None 
            vertex.distance = float('inf')

    def bfs(self, start):
        self.initialize_single_source()
        Q = [] 
        if start not in self.vertices: 
            return False 
        vertex = self.vertices[start]
        vertex.color = 'gray'
        vertex.distance = 0
        Q.append(vertex)
        while len(Q) > 0:
            vertex = Q.pop(0)
            for edge in vertex.edges:
                connection = edge.vertex 
                if connection.color == 'white':
                    connection.color = 'gray'
                    connection.distance = vertex.distance + 1
                    connection.parent = vertex 
                    Q.append(connection) 
            vertex.color = 'black'
        return True
    
    def print_path(self, dest):
        if dest not in self.vertices:
            return False
        vertex = self.vertices[dest] 
        if vertex.parent is None:
            print("No path to starting vertex")
        else: 
            stack = []
            stack.append(vertex)
            while vertex.parent is not None:
                vertex = vertex.parent
                stack.append(vertex)
            while len(stack) > 0:
                vertex = stack.pop(-1)
                print(vertex.key)
        return True
            


    def add(self, key, data):
        if key in self.vertices:
            return False, "Key already in graph"
        vertex = Vertex(key, data)
        self.vertices[key] = vertex 
        return True, "Done"

    def connect(self, ka, kb):
        if ka in self.vertices and kb in self.vertices: 
            va = self.vertices[ka]
            vb = self.vertices[kb]
            va.add_edge(vb)
            if not self.directed:
                vb.add_edge(va)
        else: 
            return False, "Key(s) not found"

    def display(self):
        for key in self.vertices:
            print(self.vertices[key])



if __name__ == '__main__':
    # cities = [('AT', 'Athens'), ('TI', 'Tirana'), ('SK', 'Skopje'), ('PR', 'Prague'), ('SO', 'Sofia'), ('BR', 'Brussels'),
    #             ('PA', 'Paris'), ('LO', 'London')]
    # conn = [('AT', 'TI'), ('AT', 'SK'), ('AT', 'SO'), ('TI', 'SK'), ('SK', 'SO'), ('TI', 'PR'), ('SO', 'PR'), 
    #         ('PR', 'BR'), ('PR', 'PA'), ('PA', 'BR'), ('PA', 'LO')]

    cities = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'),
              ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')]
    conn = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'F'), ('E', 'D'), ('E', 'G'),
            ('E', 'H'), ('F', 'G'), ('F', 'I'), ('G', 'H'), ('H', 'K'), ('K', 'J'), ('J', 'I'),]

    graph = Graph()
    for v in cities:
        graph.add(v[0], v[1])
    for c in conn:
        graph.connect(c[0], c[1])

    graph.bfs('A')
    graph.display()
    graph.print_path('K')


    

    
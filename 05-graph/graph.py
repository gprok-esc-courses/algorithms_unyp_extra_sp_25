
class Vertex:
    def __init__(self, key, data):
        self.key = key
        self.data = data 
        self.edges = []
        self.parent = None 
        self.color = 'white'
        self.distance = float("inf")

    def add_edge(self, vertex, weight):
        e = Edge(vertex)
        e.weight = weight
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
        self.weighted = False

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
    
    def relax(self, source, destination, weight):
        if source.distance + weight < destination.distance:
            destination.distance = source.distance + weight
            destination.parent = source
    
    def dijkstra(self, start):
        if start not in self.vertices:
            return False
        self.initialize_single_source()
        v = self.vertices[start]
        v.distance = 0
        v.color = 'grey'
        Q = list(self.vertices.values())
        while len(Q) > 0:
            Q.sort(key=lambda x : x.distance)
            current = Q.pop(0)
            for edge in current.edges:
                self.relax(current, edge.vertex, edge.weight)
            current.color = 'black'
    
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

    def connect(self, ka, kb, **kwargs):
        if ka in self.vertices and kb in self.vertices: 
            va = self.vertices[ka]
            vb = self.vertices[kb]
            weight = 1 if 'weight' not in kwargs else kwargs['weight']
            va.add_edge(vb, weight)
            if not self.directed:
                vb.add_edge(va, weight)
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
              ('H', 'H'), ('I', 'I')]
    conn = [('A', 'B', 1), ('A', 'C', 3), ('A', 'D', 4), ('B', 'F', 2), ('C', 'D', 2), ('C', 'I', 10), 
            ('D', 'E', 6), ('D', 'G', 1), ('E', 'F', 4), ('E', 'H', 3), ('F', 'H', 4), ('G', 'H', 2), 
            ('G', 'I', 1), ('H', 'I', 5) ]

    graph = Graph()
    graph.weighted = True
    for v in cities:
        graph.add(v[0], v[1])
    for c in conn:
        if graph.weighted:
            graph.connect(c[0], c[1], weight=c[2])
        else:
            graph.connect(c[0], c[1])

    graph.bfs('A')
    # graph.dijkstra('A')
    graph.display()
    graph.print_path('I')


    

    
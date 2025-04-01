
class Vertex:
    def __init__(self, key, data):
        self.key = key
        self.data = data 
        self.edges = []

    def add_edge(self, vertex):
        e =Edge(vertex)
        self.edges.append(e)

    def __str__(self):
        s = str(self.key)
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
    cities = [('AT', 'Athens'), ('TI', 'Tirana'), ('SK', 'Skopje'), ('PR', 'Prague'), ('SO', 'Sofia'), ('BR', 'Brussels'),
                ('PA', 'Paris'), ('LO', 'London')]
    conn = [('AT', 'TI'), ('AT', 'SK'), ('AT', 'SO'), ('TI', 'SK'), ('SK', 'SO'), ('TI', 'PR'), ('SO', 'PR'), 
            ('PR', 'BR'), ('PR', 'PA'), ('PA', 'BR'), ('PA', 'LO')]

    graph = Graph()
    for v in cities:
        graph.add(v[0], v[1])
    for c in conn:
        graph.connect(c[0], c[1])

    graph.display()

    

    
# Create a dictionary with graph elements

print("-------------------------------------------------------------")

print("Display graph")

print("-------------------------------------------------------------")

graph = {"a": ["b", "c"], "b": ["a", "d"], "c": ["a", "d"],
         "d": ["b", "e"], "e": ["d"]}


print(graph)


print("-------------------------------------------------------------")

print("Display graph vertices")

print("-------------------------------------------------------------")


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
# Create the dictionary with graph elements


graph_elements = {"a": ["b", "c"], "b": ["a", "d"],
                  "c": ["a", "d"], "d": ["b", "e"],
                  "e": ["d"]}

g = graph(graph_elements)

print(g.getVertices())



print("-------------------------------------------------------------")

print("Display graph edges")

print("-------------------------------------------------------------")

class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

# Find the distinct list of edges

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename


graph_elements = {"a": ["b", "c"], "b": ["a", "d"],
                  "c": ["a", "d"], "d": ["e"],
                  "e": ["d"]}

ge = graph(graph_elements)

print(ge.edges())


print("-------------------------------------------------------------")

print("Adding a vertex")

print("-------------------------------------------------------------")


class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

# Add the vertex as a key

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

# Create the dictionary with graph elements


graph_elements = {"a": ["b", "c"], "b": ["a", "d"],
                  "c": ["a", "d"], "d": ["e"],
                  "e": ["d"]}

gv = graph(graph_elements)
gv.addVertex("f")

print(gv.getVertices())


print("----------------------------------------------------------")

print("Adding an edge")

print("-----------------------------------------------------------")

class graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge name

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                edgename.append({vrtx, nxtvrtx})
        return edgename


graph_elements = {"a": ["b", "c"], "b":["a", "d"],
                  "c": ["a", "d"], "d": ["e"], "e": ["d"]}


gee = graph(graph_elements)

gee.AddEdge({"a", "e"})

gee.AddEdge({"a", "c"})

print(gee.edges())





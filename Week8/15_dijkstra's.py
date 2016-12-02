class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, frm, to, weight):
        if (frm in self.nodes) and (to in self.nodes):
            if (to not in self.nodes[frm]):
                self.nodes[frm][to] = weight
            if (frm not in self.nodes[to]):
                self.nodes[to][frm] = weight
                
    def display_graph(self):
        return self.nodes


def Dijkstras(graph, source, dest): # dest = detination
    current = source
    pre = {} #previous
    tw = {} # tentative_weight

    for node in graph:
        tw[node] = float("inf")
        pre[node] = None
        
    tw[source] = 0
    visited = []
    
    while current != dest:
        adjacent = graph[current]
        for edge in adjacent:
            if tw[current]+adjacent[edge] < tw[edge]:
                tw[edge] = tw[current]+adjacent[edge]
                pre[edge] = current
        visited.append(current)
        minimum = float("inf")
        for node in graph:
            if (node not in visited) and (tw[node] < minimum):
                current = node
                minimum = tw[node]
    visited.append(dest)
    
    path = shortestPath(pre, dest)
    return (path,tw[dest])
    
def shortestPath(pre, dest):
    result = []
    while pre[dest] != None:
        result.append(dest)#Insert elemnt at the beginning
        dest = pre[dest]
    result.append(dest)
    return result[::-1] # SLICING because append insert at end of list 

   
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")


graph.add_edge("A","B",1)
graph.add_edge("A","D",2)
graph.add_edge("B","C",3)
graph.add_edge("B","E",1)
graph.add_edge("C","G",5)
graph.add_edge("D","B",4)
graph.add_edge("E","F",2)


Graph = graph.display_graph()
print(Dijkstras(Graph, 'A', 'G'))

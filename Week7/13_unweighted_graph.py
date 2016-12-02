
class Graph:
    def __init__(self):
        self.nodes = {}
        
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
            
    def add_edge(self, frm, to):
      if (frm in self.nodes) and (to in self.nodes):
            if (to not in self.nodes[frm]):
                self.nodes[frm].append(to)
            if (frm not in self.nodes[to]):
                self.nodes[to].append(frm)


    def display_graph(self):
        return self.nodes



g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node("F")
g.add_node("G")

g.add_edge("A","B")
g.add_edge("A","D")
g.add_edge("B","C")
g.add_edge("B","E")
g.add_edge("C","G")
g.add_edge("D","B")
g.add_edge("E","F")

print(g.display_graph())

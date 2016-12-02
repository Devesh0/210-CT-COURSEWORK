
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

    def dfs(self,start):
        queue = [start]
        visited = []
        while queue != []:
            vertex = queue.pop()
            if vertex not in visited:
                visited.append(vertex)
                for e in self.nodes[vertex]:
                    queue.append(e)
        print("Depth first search: " + str(visited))
        
        f = open("dfs.txt","w")
        f.write("Depth first search: " + str(visited))
        f.close()


    def bfs(self,start):
        queue = [start]
        visited = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                #queue = queue + self.nodes[vertex]
                queue.extend(self.nodes[vertex])
    
        print("Breadth first search: " + str(visited))
        
        f = open("bfs.txt","w")
        f.write("Breadth first search: " + str(visited))
        f.close()

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


print("Graph: " + str(g.display_graph()))
g.dfs('B')
g.bfs('B')

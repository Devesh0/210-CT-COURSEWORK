CLASS Graph
     __init__(self)
         nodes <- {}

     ADD_NODE(self, node)
        IF node not in  nodes:
             nodes[node] <- []

     ADD_EDGE(self, frm, to)
      IF (frm in  nodes) AND (to in  nodes):
            IF (to not in  nodes[frm]):
                 insert(to) at the nodes[frm]
    
            IF (frm not in  nodes[to]):
                 insert(frm) at the nodes[to]

    DISPLAY_GRAPH(self):
        return  nodes



g <- Graph()
g.ADD_NODE("A")
g.ADD_NODE("B")
g.ADD_NODE("C")
g.ADD_NODE("D")
g.ADD_NODE("E")
g.ADD_NODE("F")
g.ADD_NODE("G")

g.ADD_EDGE("A","B")
g.ADD_EDGE("A","D")
g.ADD_EDGE("B","C")
g.ADD_EDGE("B","E")
g.ADD_EDGE("C","G")
g.ADD_EDGE("D","B")
g.ADD_EDGE("E","F")

OUTPUT g.DISPLAY_GRAPH()

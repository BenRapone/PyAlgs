def UCCBFS(graph): 
    """ input is a undirected graph (Nodes, Edges) in linked list form
        output is the number of connected components and a list containing them"""
    Nodes = graph[0]
    Edges = graph[1]
    numnodes = len(Nodes)
    numedges = len(Edges)
    nodeset = set(range(numnodes))
    components = []
    while len(nodeset) > 0:
        v = nodeset.pop()
        q = [v]
        touched = set([v])
        while len(q) > 0:
            vtx = q.pop(0)
            for edge in Nodes[vtx][0]:
                w = Edges[edge][1]
                if w not in touched:
                    touched.add(w)
                    q.append(w)
                    nodeset.remove(w)
        components.append(touched)

    return len(components),components 

def BFS(graph,v): 
    """ input is a directed graph (Nodes, Edges) in linked list form and a vertex you wish to start from
        output is all nodes that can be reached from v and number of levels out from v"""
    Nodes = graph[0]
    Edges = graph[1]
    numnodes = len(Nodes)
    numedges = len(Edges)
    touched = set([v])
    q = [v]
    levelcount = 0
    levelnode = v
    while len(q) > 0:
        vtx = q.pop(0)
        for edge in Nodes[vtx][0]:
            w = Edges[edge][1]
            if w not in touched:
                touched.add(w)
                q.append(w)
        if vtx == levelnode:
            levelcount += 1
            levelnode = w

    return touched, levelcount

def ShortestPath_BFS(graph,v,s): 
    """ input is a directed graph (Nodes, Edges) in linked list form and a vertex, v, you wish to start from and end at s
        output is the shortest number of levels from v to s, i.e. smallest number of edges between or -1 if not connected"""
    Nodes = graph[0]
    Edges = graph[1]
    numnodes = len(Nodes)
    numedges = len(Edges)
    touched = set([v])
    q = [v]
    levelcount = 0
    levelnode = v
    while len(q) > 0:
        vtx = q.pop(0)
        for edge in Nodes[vtx][0]:
            w = Edges[edge][1]
            if w not in touched:
                if w == s:
                    return levelcount+1
                touched.add(w)
                q.append(w)
        if vtx == levelnode:
            levelcount += 1
            levelnode = w

    return -1


 
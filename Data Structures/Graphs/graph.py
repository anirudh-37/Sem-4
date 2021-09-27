"""The code is borrowed from the book "Problem Solving with Algorithms and Data Structures"
   http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html
   
"""
from Heap import BinHeap
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.front=[]
        self.back=[]
        self.depfs=[]
        self.visited = dict()
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):  #f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        for i in self.vertList:
            self.visited[i] = 0

    def getVertices(self):
        return self.vertList.keys()

    def printdfs(self):
        print("DFS:",self.depfs)
        print("Front:",self.front)
        print("Back:",self.back)
        return
    
    def __iter__(self):
    	return iter(self.vertList.values())
    """
    Write a method to generate an adjacency matrix representation of the graph
    """
    def createAdjMatrix(self):
        c = self.numVertices 
        r = self.numVertices 
        adjm = [[0 for i in range(c)] for j in range(r)] 
        for i in range(c): 
            for j in range(r): 
                adjm[i][j] = 0 
        for i in self.getVertices(): 
            x = self.getVertex(i) 
            for w in x.getConnections(): 
                adjm[x.getId()][w.getId()] = x.getWeight(w)
        return adjm

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """
    
    def dfs(self,stnode):
        self.depfs.append(stnode.id)
        for i in self.vertList[(stnode.id)].getConnections():
            if(i.id not in self.depfs):
                self.front.append([stnode.id,i.id])
                self.dfs(i)
            else:
                self.back.append([stnode.id,i.id])
        return
    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """
    def bfs(self, stnode):
        queue=[]
        bfs=[]
        ce=[]
        bfs.append(stnode.getId())
        queue.append(stnode.getId())
        visited = {}
        visited[stnode.getId()] = True
        while (len(queue) > 0):
            temp = queue[0]
            queue.pop(0)
            bfs.append(temp)
            for i in self.vertList[temp].connectedTo:
                if i.getId() in visited:
                    ce.append([temp,i.getId()])
                else:
                    queue.append(i.getId())
                    visited[i.getId()] = True
        
        print("Bfs:",bfs)
        print("Cross edge:",ce)
        return
    
    """
    Write a method to generate the minimum spanning tree of the graph using Kruskal algorithm
    """
    def mstKruskal(self):
        return

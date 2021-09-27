
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

    def getVertices(self):
        return self.vertList.keys()

    def printdfs(self):
        print("Front edges:",self.front)
        print("Back edges:",self.back)
        print("dfs:",self.depfs)
    
    def __iter__(self):
    	return iter(self.vertList.values())
    """
    Write a method to generate an adjacency matrix representation of the graph
    """
    def createAdjMatrix(self):
        adjmat = list()
        

        for x in sorted(self.vertList):
            key = self.vertList[x]
            temp = []
            for y in sorted(self.vertList):
                anotherkey = self.vertList[y]
                if anotherkey in key.connectedTo:
                    temp.append(1)
                else:
                    temp.append(0)
            adjmat.append(temp)
        
        
        print("Adjacency matrix")
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print(adjmat[i][j], end=" ")
            print("")

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """
    def dfs(self,stnode):
        self.depfs.append(stnode.getId() )
        neighbours=list(stnode.getConnections())
        
        self.depfs = []
        visited = {}
        visited[stnode.getId()] = True
        self.time = 0
        pre = {}
        post = {}
        triedge = []
        cross = []

        def recur(x):
            self.depfs.append(x.getId())
            pre[x.getId()] = self.time
            self.time += 1
            for i in self.vertList[x.getId()].connectedTo:
                if i.getId() in visited:
                    self.back.append([x.getId(),i.getId()])
                else:
                    self.front.append([x.getId(),i.getId()])
                    visited[i.getId()] = True
                    recur(i)
            
            post[x.getId()] = self.time
            self.time += 1
                    
        recur(stnode)

        
        return 
    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """
    def bfs(self,stnode):
        queue=[]
        breadth=[]
        cross=[]
        breadth.append(stnode.getId())
        queue.append(stnode.getId())
        
        breadth = []
        visited = {}
        visited[stnode.getId()] = True
        while (len(queue) > 0):
            temp = queue[0]
            queue.pop(0)
            breadth.append(temp)
            for i in self.vertList[temp].connectedTo:
                if i.getId() in visited:
                    cross.append([temp,i.getId()])
                else:
                    queue.append(i.getId())
                    visited[i.getId()] = True
        
        print("Bfs:",breadth)
        print("Cross edge:",cross)
        return

def testGraph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
    g.addEdge(5, 1, 8)
    g.addEdge(1, 2, 19)
    g.addEdge(5, 0, 10)
    g.addEdge(4, 6, 11)
    g.addEdge(6, 10, 23)
    g.addEdge(10, 9, 33)
    g.addEdge(9, 8, 7)
    g.addEdge(6, 7, 6)
    g.addEdge(8, 7, 1)
    g.addEdge(9, 6, 9)
    g.addEdge(7, 10, 14)
    g.addEdge(0, 4, 15)
    g.addEdge(0, 3, 16)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 30)
    g.addEdge(4, 5, 18)
    g.addEdge(5, 2, 22)
    g.addEdge(3, 1, 17)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    print("Adjacent matrix:")
    AdjMat = list()
    g.createAdjMatrix()
    

    start = g.getVertex(3)


    print ("Depth first Traversal")
    g.dfs(start)
    g.printdfs()
    print ("Breadth first Traversal")
    g.bfs(start)
    


def main():
    testGraph()


if __name__ == '__main__':
    main()

    

#@start-editable@

import math
from collections import deque
			
			
#@end-editable@

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
            

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0
        

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild==None and curnode.rightchild==None):
            return (True)
        else:
            return (False)

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False   	

    def inorderTraverse(self, v):
        #@start-editable@

        if v:
            self.inorderTraverse(v.leftchild)
            print(v.element,end = ",")
            self.inorderTraverse(v.rightchild)	
			
	    #@end-editable@
        

    def preorderTraverse(self, v):
        #@start-editable@

        if v:
            print(v.element,end = ",")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)	
			
	    #@end-editable@
       

    def postorderTraverse(self, v):
        #@start-editable@

        if v:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element,end = ",")	
			
	    #@end-editable@
        

    def levelorderTraverse(self, v):
        #@start-editable@

        if v != None:
            lq = deque()
            lq.append(v)
            while(len(lq) > 0):
                v = lq.popleft()
                print(v.element,end = ",")
                if v.leftchild is not None:
                    lq.append(v.leftchild)
                if v.rightchild is not None:
                    lq.append(v.rightchild)
            
        return 0	
			
	    #@end-editable@
       

    def findDepth(self, v):
        #@start-editable@
        if self.isRoot(v):
            return 0
        else:
            x = 1 + self.findDepth(v.parent)
            return x
        
			
	    #@end-editable@
    	

    def findHeight(self, v):
        #@start-editable@
        
        if v is None:
            return -1
        else:
            ld =  1 + self.findHeight(v.leftchild)
            rd =  1 + self.findHeight(v.rightchild)

            if(ld > rd):
                return ld
            else:
                return rd
        
			

        
	    #@end-editable@
    	

    # delete leaves in the tree
    def delLeaves(self, v):
        #@start-editable@
        if v == None: 
            return None
        if v.leftchild == None and v.rightchild == None: 
            return None
        v.leftchild = self.delLeaves(v.leftchild)  
        v.rightchild = self.delLeaves(v.rightchild) 
        
        return v

        		
			
	    #@end-editable@
        
    # returns true if tree is proper
    def isProper(self, v):
        #@start-editable@
        if v == None:
            return True
        if(v.leftchild == None and v.rightchild == None):
            return True
        if(v.leftchild != None and v.rightchild != None):
            return(self.isProper(v.leftchild) and self.isProper(v.rightchild))

        return False			
			
	    #@end-editable@
        
    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        #@start-editable@
        if v != None:
            t = v
            self.mirror(v.leftchild)
            self.mirror(v.rightchild)
            t = v.leftchild
            v.leftchild = v.rightchild
            v.rightchild = t
            return v
        else:
            return None
    
    def p(self,v,s):
        
        if v is None:
            return (s == 0)
        else:
            a = 0
            ss = s - v.element
            if(v.leftchild == None and v.rightchild == None and ss == 0):
                return True
            if v.leftchild is not None:
                a = a or self.p(v.leftchild,ss)
            if v.rightchild is not None:
                a = a or self.p(v.rightchild,ss)
            if(a == 0):
                return False
            return a
    def sum(self,v,s,l,e):
        if v is not None:
            if(self.isExternal(v)):
                s = v.element + s
                l.append(s)
                e.append(v.element)
                return
            else:
                s = v.element + s
                self.sum(v.leftchild,s,l,e)
                self.sum(v.rightchild,s,l,e)
        return 


			
	    #@end-editable@
        

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz=len(nodelist)
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element,end=" ")
            else:
                print(None)


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    #determine whether there exists a root-to-leaf path whose nodes sum is equal to a specified integer
    def root2leafsum(self, k):
        #@start-editable@
        x = self.p(self.root,k)
        print(x)
        return



           




        	
			
	    #@end-editable@
        

    #determine the value of the leaf node in a given binary tree that is the terminal node of a path of least value from the root of the binary tree to any leaf. The value of a path is the sum of values of nodes along that path.
    def leastleaf(self):
        #@start-editable@
        s = 0
        suml = []
        e = []
        self.sum(self.root,s,suml,e)
        
        min = suml[0]
        t = 0
        for i in range(len(suml)):
            if suml[i] < min:
                min = suml[i]
                t = i
        print(e[t])
        return 	
			
	    #@end-editable@
        

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
         command = input()
         operation = command.split()
         if (operation[0] == "I"):
              tree.inorderTraverse(tree.root)
              print()
         elif (operation[0] == "P"):
              tree.preorderTraverse(tree.root)
              print()
         elif (operation[0] == "Post"):
              tree.postorderTraverse(tree.root)
              print()
         elif (operation[0] == "L"):
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == "D"):
              pos = int(operation[1])
              print(tree.findDepth(nlist[pos]))
         elif (operation[0] == "H"):
              pos = int(operation[1])
              print(tree.findHeight(nlist[pos]))
         elif (operation[0] == "IP"):
              print(tree.isProper(tree.root))
         elif (operation[0] == 'M'):
              tree.mirror(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'DL'):
              tree.delLeaves(tree.root)
              tree.levelorderTraverse(tree.root)
              print()
         elif (operation[0] == 'RL'):
              tree.root2leafsum(int(operation[1]))
              print()
         elif (operation[0] == 'ML'):
              tree.leastleaf()
              print()
         inputs -= 1

if __name__ == '__main__':
    main()
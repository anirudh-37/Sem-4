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
            print(v.element,end = " ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)	
			
	    #@end-editable@
       

    def postorderTraverse(self, v,li):
        #@start-editable@

        if v:
            self.postorderTraverse(v.leftchild,li)
            self.postorderTraverse(v.rightchild,li)
            li.append(v.element)
            	
			
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
    
    def palindrome(self,v):
        nl = []
        flag = 0
        self.postorderTraverse(v,nl)
        for i in range(0,len(nl)):
            print(nl[i],end = " ")
        print()
        self.mirror(v)
        self.preorderTraverse(v)
        print()
        f = []
        self.postorderTraverse(v,f)
        for i in range(0,len(f)):
            if(f[i] != nl[i]):
                flag = 1
        if(flag == 0):
            print("Is a Palindromic Tree")
        elif(flag == 1):
            print("Is Not a Palindromic Tree")


			
	    #@end-editable@
        

    def buildTree(self, eltlist):
        if eltlist[0] != -1:
            eltlist.insert(0,-1)
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

    
        

   
        

def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    tree.buildTree(arr)
    tree.palindrome(tree.root)
    

        

if __name__ == '__main__':
    main()
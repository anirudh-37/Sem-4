import math
from collections import deque

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
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def isRoot(self,curnode):
    	if (curnode.parent==None):
    		return True
    	else:
    		return False

    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print (curnode.element,end = ",")
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild)

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element,end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)
        

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print (curnode.element,end=",")
        

    def levelorderTraverse(self, v):
        q1 = deque()
        q1.append(v)
        while (len(q1)>0):
        	temp=q1.popleft()
        	print(temp.element,end=",")
        	if temp.leftchild!=None:
        		q1.append(temp.leftchild)
        	if temp.rightchild!=None:
        		q1.append(temp.rightchild)
        return



    def buildTree(self, expr):
        #@start-editable@
        li = list(expr.split())
        v = self.root
        for i in range(len(li)):
            if(li[i] == '('):
                bc = bc + 1
                if(bc > 1 and v.leftchild.element == 0):
                    v = v.leftchild
                elif(bc > 1 and v.rightchild.element == 0):
                    v = v.rightchild
                v.leftchild = self.node()
                v.leftchild.parent = v
                v.rightchild = self.node()
                v.rightchild.parent = v
            elif(li[i] == '+' or li[i] == '-' or li[i] == '*' or li[i] == '/'):
                v.element = li[i]
            elif(li[i].isdigit()):
                if v.leftchild.element == 0:
                    v.leftchild.element = li[i]
                elif v.rightchild.element == 0:
                    v.rightchild.element = li[i]   
            elif(li[i] == ')'):
                if (v.parent != None):
                    v = v.parent
        nodelist = []
        q = deque()
        q.append(self.root)
        nc = self.node()
        nc.element = -1
        nodelist.append(nc)
        h = self.fh(self.root)
        mi = pow(2,h + 1) - 1
        nodec = 0
        while(len(q) > 0 and nodec < mi):
            x = q.popleft()
            nodelist.append(x)
            if(self.isExternal(x)):
                q.append(nc)
                q.append(nc)
            else:
                if x.leftchild != None:
                    q.append(x.leftchild)
                if x.rightchild != None:
                    q.append(x.rightchild)
            nodec += 1


        
                

        



        

			
			
        #@end-editable@
        return nodelist

    # write a function to visualize the tree

    def equivalent(self, treevec1, root1, treevec2, root2):
        #@start-editable@

        return
    def fh(self,v):
            if (self.isExternal(v)):
                return 0
            else:
                h=0
                for w in self.getChildren(v):
                    h=max(h,self.fh(w))
            return 1+h

        #@end-editable@
        

    def printTree(self, nlist):
        for i in range(len(nlist)):
            print(nlist[i].element,end=" ")
        print()


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


def main():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    inputs = int(input())
    while (inputs > 0):
        exp1 = input()
        exptree1 = tree1.buildTree(exp1)
        tree1.printTree(exptree1)
        exp2 = input()
        exptree2 = tree2.buildTree(exp2)
        tree2.printTree(exptree2)
        print(tree1.equivalent(exptree1, tree1.root, exptree2, tree2.root))
        inputs -= 1
 
if __name__ == '__main__':
    main()
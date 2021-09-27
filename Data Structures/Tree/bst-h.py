import math
class BinarySearchTree:

    """
        This defines the node class. The children can be individually declared or stored
        in a list. We are adding a pos value to help with visualization
    """
    
    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: True if tree contains e or False if e not present in T
    """
                 
    def findElement(self,e,curnode):
        while(self.isExternal(curnode) == False):
            if curnode.element == e:
                return curnode
            if e > curnode.element:
                if curnode.rightchild == None:
                    break
                else:
                    curnode = curnode.rightchild
            elif e < curnode.element:
                if curnode.leftchild == None:
                    break
                else:
                    curnode = curnode.leftchild
        return curnode

        '''if self.isExternal(curnode) or curnode.element == e:
            return curnode
        if e > curnode.element:
            return self.findElement(e,curnode.rightchild)
        elif e < curnode.element:
            return self.findElement(e,curnode.leftchild)'''
    
        

    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly
        
    """
    def insertElement(self,e):
        if self.root == None:
            self.root = self.node()
            self.root.element = e
        else:
            x = self.node()
            x = self.findElement(e,self.root)
            if(e > x.element):
                x.rightchild = self.node()
                x.rightchild.parent = x
                x.rightchild.element = e
            elif(e < x.element):
                x.leftchild = self.node()
                x.leftchild.parent = x
                x.leftchild.element = e
        return
        
                
    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """
    def inorderTraverse(self,v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print(curnode.element,end=",")
        if (curnode.rightchild!=None):
            self.inorderTraverse(curnode.rightchild)
        

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal.
    """
    def returnNextInorder(self,v):
        return
        
    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteElement(self,e):
        return
        

    """
        Given a list of elements construct a balanced binary search tree
    """
    def createTree(self, items):
        self.sz=len(items)
        mid = int(math.floor(len(items)/2))
        self.insertElement(items[mid])
        del items[mid]
        if (len(items)>1):
            self.createTree(items[0:mid])
            self.createTree(items[mid:len(items)+1])
        else:
            if (len(items)==1):
                self.insertElement(items[0])
            return
        
    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
            2. printTree(self): to visualize the tree for your debugging purposes. You may print it
            using text formatting or use a turtle library given along with the file.
    """
    def isExternal(self,curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []
        #if curnode.leftchild!= None:
        children.append(curnode.leftchild)
        #if curnode.rightchild!= None:
        children.append(curnode.rightchild)
        return children
        
            
    def preorderTraverse(self,v):
        curnode = v
        print (curnode.element,end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.preorderTraverse(curnode.rightchild)
        return
        
    def postorderTraverse(self,v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.postorderTraverse(curnode.rightchild)
        print (curnode.element)
        return

    def findDepthIter(self,v):
        if v==self.root:
            return 0
        else:
            return 1+self.findDepthIter(v.parent)
    def findDepth(self,v):
        return self.findDepthIter(self.findElement(v.element,self.root))

    def findHeightIter(self,v):
        if self.isExternal(v):
            return 0
        else:
            h=0
            if(v.leftchild!=None):
                h=max(h,self.findHeightIter(v.leftchild))
            if(v.rightchild!=None):
                h=max(h,self.findHeightIter(v.rightchild))
            return 1+h
        
    def findHeight(self,v):
        return self.findHeightIter(self.findElement(v.element,self.root))

    def findRange(self,low,high):
        return
        
        
	
    def findMedian(self):
        return
        

def testbst():
    #initialize Data structure here
    ds = BinarySearchTree()
    arr = list(map(int, input().split()))
    ds.createTree(arr)
    ds.preorderTraverse(ds.root)
    print()
    inputs = int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="M"):
            ds.preorderTraverse(ds.root)
            print()
            print(ds.findMedian())
        elif(operation[0]=="R"):
            print(ds.findRange(int(operation[1]),int(operation[2])))
        elif(operation[0]=="I"):
            ds.insertElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="Pre"):
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="In"):
            ds.inorderTraverse(ds.root)
            print()
        elif(operation[0] == "F"):
            temp = ds.findElement(int(operation[1]))
            if (temp == None):
                print(False)
            else:
                print(True)
        elif(operation[0]=="D"):
            ds.deleteElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        inputs-=1



def main():
    testbst()

if __name__ == '__main__':
    main()
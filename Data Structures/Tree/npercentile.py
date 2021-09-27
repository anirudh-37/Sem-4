import math
class BinarySearchTree:

    """
        This defines the node class. The children can be individually declared or stored
        in a list. We are adding a pos value to help with visualization
    """
    class node:
        def _init_(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def _init_(self):
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
        while(not(self.isExternal(curnode))):
            if curnode.element==e:
                break
            if(e>curnode.element):
                if(curnode.rightchild==None):
                    break
                else:
                    curnode=curnode.rightchild
            elif(e<curnode.element):
                if(curnode.leftchild==None):
                    break
                else:
                    curnode=curnode.leftchild
        return curnode

    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly
        
    """


    def insertElement(self,e):
        if self.root==None:
            self.root=self.node()
            self.root.element=e
        else:
            x = self.root
            v=self.findElement(e,x)
            if(e>v.element):
                v.rightchild=self.node()
                v.rightchild.parent=v
                v.rightchild.element=e
            elif(e<v.element):
                v.leftchild=self.node()
                v.leftchild.parent=v
                v.leftchild.element=e
        return
    """py bststemplate123.py
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
        q=self.findElement(e,self.root)
        temp=q.element
        if(q.element==e):
            if(self.isExternal(q)):
                if (q.element==self.root.element):
                    self.root=None
                elif q.parent.element>q.element:
                    q.parent.leftchild=None
                elif q.parent.element<q.element:
                    q.parent.rightchild=None
            elif (q.leftchild!=None and q.rightchild==None):
                if(q.parent!=None):
                    if(q.parent.element<q.leftchild.element):
                        q.parent.rightchild=q.leftchild
                        q.leftchild.parent=q.parent
                    elif(q.parent.element>q.leftchild.element):
                        q.parent.leftchild=q.leftchild
                        q.leftchild.parent=q.parent
                else:
                    self.root=self.root.leftchild
                    self.root.parent=None
            elif (q.rightchild!=None and q.leftchild==None):
                if(q.parent!=None):
                    if(q.parent.element<q.rightchild.element):
                        q.parent.rightchild=q.rightchild
                        q.rightchild.parent=q.parent
                    elif(q.parent.element>q.rightchild.element):
                        q.parent.leftchild=q.rightchild
                        q.rightchild.parent=q.parent
                else:
                    self.root=self.root.rightchild
                    self.root.parent=None
            elif (q.rightchild!=None and q.leftchild!=None):
                flag=0
                v=q.rightchild
                while(not(self.isExternal(v))):
                    if(v.leftchild!=None):
                        flag=1
                        v=v.leftchild
                    else:
                        flag=2
                        break
                if(flag==0):
                    q.element=v.element
                    v.parent.rightchild=None
                elif(flag==1):
                    q.element=v.element
                    v.parent.leftchild=None   
                else:
                    if(v.rightchild.element>=q.rightchild.element):
                        q.element=v.element
                        q.rightchild=v.rightchild
                        v.rightchild.parent=q
                    else:
                        v.parent.leftchild=v.rightchild
                        v.rightchild.parent=v.parent
        else:
            print("Error, element not found")
            return -1
        return temp 

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
        print (curnode.element,end=" ")
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

    def findrange(self,low,high):
        r=[]
        x=[]
        self.inorder(self.root,x)
        for i in x:
            if(i>low and i<=high):
                r.append(i)
        return r
    
    def inorder(self,v,inl):
        curnode = v
        if (curnode.leftchild != None):
            self.inorder(curnode.leftchild,inl)
        inl.append(v.element)
        if (curnode.rightchild!=None):
            self.inorder(curnode.rightchild,inl)
        return inl

    def findmax(self,v):
        max=0
        if(v.rightchild!=None):
            while(v.rightchild!=None):
                v=v.rightchild
            max=v.element
        else:
            max=v.element
        return max
    
    def greater(self,v):
        q=self.findmax(self.root)
        grlis=self.findrange(v,q)
        
        return len(grlis)

    def getpercentile(self,k):
        li=[]
        c=0
        self.inorder(self.root,li)
        n=len(li)
        for i in li:
            if(i<=k):
                c=c+1
        per= (c/n)*100
        per=(math.ceil(per))
        return per
def testbst():
    #initialize Data structure here
    ds = BinarySearchTree()
    
    inputs = int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="H"):
            print(ds.findmax(ds.root))
        elif(operation[0]=="I"):
            ds.insertElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        elif(operation[0]=="G"):
            print(ds.greater(int(operation[1])))
        elif(operation[0]=="P"):
            print(ds.getpercentile(int(operation[1])))
        inputs-=1

def main():
    testbst()

if __name__ == '_main_':
    main()



class MyStack():

    class Node:
        def __init__(self,ele):
            self.element = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.sz = 0
        

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if(self.size() == 0):
            self.head = self.Node(value)
            self.sz += 1
        else:
            newnode = self.Node(value)
            newnode.next = self.head
            self.head = newnode
            self.sz += 1
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if self.isEmpty():
            print("Stack Empty Exception")
            return
        else:
            curnode = self.head
            self.head = self.head.next
            curnode.next = None
            self.sz -= 1


        
        return curnode.element
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if self.size == 0:
            print("Stack Empty Exception")
            return
        else:
            return self.head.element

        
        return

    # returns True if stack is empty   
    def isEmpty(self):
        return(self.size() == 0) 

    # returns the number of elements currently in stack 
    def size(self):
        return self.sz




    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            curnode = self.head
            while(curnode != None):
                print(curnode.element ,end = " ")
                curnode = curnode.next
            print('\n')
        return

# Driver code.---------------------------------------------

def teststack():
    stacksize=int(input())
    st1 = MyStack()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(st1.size())
        elif(operation[0]=="I"):
            print(st1.isEmpty())
        elif(operation[0]=="P"):
            st1.push(int(operation[1]))
            st1.printStack()
        elif(operation[0]=="O"):
            print(st1.pop())
            st1.printStack()
        elif(operation[0]=="T"):
            print(st1.top())
            st1.printStack()
        inputs-=1

def main():
    teststack()

if __name__ == '__main__':
    main()



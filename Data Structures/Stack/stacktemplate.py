class MyStack():
    def __init__(self,size):
        self.stack = []
        # this is the stack container called 'stack'
        self.max_stack_size = size
        for i in range(self.max_stack_size):
            self.stack.append(None)
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        #print(self.stack)

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if(self.t > self.max_stack_size):
            print("Stack Full Exception")
        else:
            self.t += 1
            self.stack[self.t] = value

        
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if(self.t <= -1):
            print("Stack Empty Exception")
        else:
            p = self.stack[self.t]
            self.stack[self.t] = None
            self.t -= 1
            return p
        
        return
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        
        
        return self.stack

    # returns True if stack is empty   
    def isEmpty(self):
        return (self.t <= -1)

    # returns the number of elements currently in stack 
    def size(self):
        return self.t + 1




    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i]!=None:
                    print(self.stack[i],end=" ")
            print()
        return

# Driver code.---------------------------------------------

def teststack():
    stacksize=int(input())
    st1 = MyStack(stacksize)
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



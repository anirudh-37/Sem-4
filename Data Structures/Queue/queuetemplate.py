class MyQueue():
    
    def __init__(self,size):
        # this is the queue container called 'queue'
        self.queue = []
        # front and back indexes
        self.f = 0
        self.r = 0
        # define the queue size 'max_queue_size' and initialize it
        self.max_queue_size = size
        for i in range(0,self.max_queue_size):
            self.queue.append(None)
        self.sz=0

    # define the enqueue operation which inserts the value into the queue, must throw a queue full exception
    # call print queue after enqueue (not when there is an exception)
    def enqueue(self,value):
        if(self.sz == self.max_queue_size):
            print("Queue Full Exception")
            return
        
        else:
            self.queue[self.r] = value
            self.r=(self.r+1) % self.max_queue_size
            self.sz+=1
            self.printQueue()
        
                
    # returns first elt of the queue if not empty, else throws queue empty
    # exception
    
    def dequeue(self):
        if(self.sz == 0):
            print("Queue Empty Exception")
            return None
        else:
            x = self.queue[self.f]
            self.queue[self.f] = None
            self.sz -= 1
            self.f = (self.f+1)%self.max_queue_size
            return x
        

        
       
    
    # returns front element without removing it if the queue is not empty, else throws exception   
    def front(self):
        if(self.sz == 0):
            print("Queue Empty Exception")
            return
        else:
            return self.queue[self.f]

        
     
    # returns True if queue is empty
    def isEmpty(self):
        return (self.sz==0)

    # returns the number of elements currently in queue
        
    def size(self):
        return (self.sz)

    def delK(self,k):
        if (self.sz == 0):
            return
        elif self.front()==k:
            self.dequeue()
            self.printQueue()
        else:
            i=0
            while(i<=self.sz):
                if i==(k-1):
                    self.dequeue()
                else:
                    self.enqueue(self.dequeue())
                i+=1
        return 
        
    
    def printQueue(self):
        if (self.isEmpty()):
            print ("Queue Empty")
        else:
            for i in range(self.max_queue_size):
                if self.queue[i]!=None:
                    print(self.queue[i],end=" ")
            print(" ")


# Driver code.---------------------------------------------

def testqueue():
    qsize=int(input())
    q1 = MyQueue(qsize)
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(q1.size())
        elif(operation[0]=="I"):
            print(q1.isEmpty())
        elif(operation[0]=="E"):
            q1.enqueue(int(operation[1]))
        elif(operation[0]=="D"):
            print(q1.dequeue())
            q1.printQueue()
        elif(operation[0]=="F"):
            print(q1.front())
        elif(operation[0]=="DK"):
            q1.delK(int(operation[1]))
        inputs-=1

def main():
    testqueue()

if __name__ == '__main__':
    main()
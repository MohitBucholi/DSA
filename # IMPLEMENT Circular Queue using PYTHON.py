# IMPLEMENT Circular Queue using PYTHON
# First In First Out

# create a class 
class circular_queue:
    def __init__(self,k):
        self.q = [None]*k     # give the length(k)
        self.k =  k
        self.front = self.rear = -1     # set front and rear as -1
    
# creat a function to check queue is empty
    def isempty(self):
        if self.rear == -1:
            return True
        else:
            return False

# creat a function to check queue is full
    def isfull(self):
        if (self.rear+1)%self.k == self.front:
            return True
        else:
            return False
        
# create a function to insert item in queue
    def enqueue(self,item):
        if self.isfull() == True:
            print("queue is already full")
        elif self.rear == -1:
            self.front = self.rear =0
            self.q[self.rear] = item
        else:
            self.rear = (self.rear+1)%self.k
            self.q[self.rear] = item

# create a function to remove the item from queue
    def dequeue(self):
        if self.isempty() == True:
            print("queue is already empty")
        elif self.rear ==0 and self.front == 0:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.k

# function to print the queue
    def show(self):
        if self.rear >= self.front:
            for i in range(self.k):
                if i>=self.front and i<=self.rear:
                    print(self.q[i],end=" ")
            print()
        else:
            for i in self.q[self.front:]:
                print(i,end=" ")
            for i in self.q[:self.rear+1]:
                print(i,end=" ")
            

l = circular_queue(5)
l.enqueue(5)
l.enqueue(6)
l.enqueue(9)
l.enqueue(0)
l.enqueue(3)
l.show()
l.dequeue()
l.dequeue()
l.dequeue()
l.enqueue(10)
l.enqueue(11)
l.show()


# Application's of Circular Queue
# 1. CPU Scheduling
# 2. Memory Management
# 3. Traffic Management
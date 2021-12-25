# IMPLEMENT Simple QUEUE Using PYTHON 
# First In First Out

#Creat a class Queue
class queue:
    def __init__(self):
        self.q =[]

# create a function to check Queue is empty or not
    def isempty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

# create a function to insert the items in Queue 
    def enqueue(self,item):
        self.q.append(item)

# Create a function to remove the item from Queue
    def dequeue(self):
        if self.isempty() == False:
            self.q.pop(0)
        else:
            print("Queue is empty")
# function for print the Queue
    def show(self):
        print(self.q)

l = queue()
l.isempty()
l.enqueue(1)
l.enqueue(5)
l.enqueue(6)
l.enqueue(3)
l.show()
l.dequeue()
l.dequeue()
l.show()
l.isempty()

# Queue Time Complexity
# For the array-based implementation of a Queue, the enqueue and dequeue operations take constant time, i.e. O(1).
# and In PYTHON Code Time Complexity is o(n)

# Applications where Queue is in use
# 1. CPU Scheduling, Disk Scheduling
# 2. In Call Center Phone System use Queue to hold people calling them in order

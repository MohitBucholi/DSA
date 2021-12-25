# IMPLEMENT Dequeue using PYTHON
# It Doesn't Follow the First In First Out

# It allow insertion and deletion from both side front and rear

# create a class 
class dequeue:
    def __init__(self):
        self.q =[]

# creat a function to check queue is empty
    def empty(self):
        if len(self.q)==0:
            return True
        else:
            return False

# function to insertion at front
    def add_front(self,item):
        self.q.insert(0,item)

# function to insertion at rear
    def add_rear(self,item):
        self.q.append(item)

# function to deletion at rear
    def del_rear(self):
        if self.empty() == False:
            self.q.pop()
        else:
            print("queue is empty")

# function to deletion at front
    def del_front(self):
        if self.empty()== False:
            self.q.pop(0)

        else:
            print("queue is empty")

# function to print dequeue    
    def show(self):
        print(self.q)

l = dequeue()
l.add_rear(3)
l.add_rear(9)
l.add_front(8)
l.add_front(5)
l.show()
l.del_rear()
l.del_front()
l.show()

# Application's of Dequeue
# 1. In undo operation on software
# 2. To store the history in browser
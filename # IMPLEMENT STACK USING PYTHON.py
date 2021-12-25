# IMPLEMENT STACK USING PYTHON 
# Last In First Out

#Creat a class stack
class stack:
    def __init__(self):
        self.s =[]

# create a function to check stack is empty or not
    def empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

# create a function to insert the items in stack
    def push(self,item):
        self.s.append(item)

# Create a function to remove the item from stack
    def pop(self):
        if self.empty() == False:
            self.s.pop()
        else:
            print("stack is empty")
# function for print the stack
    def show(self):
        print(self.s)

l = stack()
l.push(4)
l.push(6)
l.push(1)
l.push(9)
l.push(0)
l.show()
l.pop()
l.pop()
l.pop()
l.show()

# Stack Time Complexity
#For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).

# Applications where stack is in use
# 1. To reverse a word
# 2. In compilers
# 3. The back button in a browser
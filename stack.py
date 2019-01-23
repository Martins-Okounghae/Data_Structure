print("--------------------------------------------")
print("PUSH into a Stack")
print("---------------------------------------------")
class Stack:
    def __init__(self):
        self.stack =[]

    def add(self, dataval):
        #Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[0]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())


print("--------------------------------------------")
print("POP from a Stack")
print("---------------------------------------------")

class PopStack:
    def __init__(self):
        self.popstack = []

    def add(self, dataval):
        if dataval not in self.popstack:
            self.popstack.append(dataval)
            return  True
        else:
            return False


    #Use list pop method to remove element from the stack

    def remove(self):
        if len(self.popstack) <= 0:
            return "No element in the Stack"
        else:
            return self.popstack.pop()


    def top_index(self):
        return self.popstack[0]



PopAStack = PopStack()

PopAStack.add("Mon")
PopAStack.add("Tue")
#Num1Index = PopAStack.top_index()
#print(Num1Index)
print(PopAStack.remove())
PopAStack.add("Wed")
PopAStack.add("Thu")
PopAStack.add("Fri")
print(PopAStack.remove())

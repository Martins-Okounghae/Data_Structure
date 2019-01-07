# Creation of Linked List

print("Creating a linked list")
print("--------------------------------------------------")

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None

list1 = SlinkedList()

list1.headval = Node("Mon")
e2 = Node("Tue")

e3 = Node("Wed")


# Link Second Node to Third Node
print("Link Second Node to Third Node")

e2.nextval = e3

print()


print("Traversing a linked List")
print("-----------------------------------------------------------")


class Node:
    def __init__(self, dataval=Node):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()

list.headval = Node("Mon")

e2 = Node("Tue")

e3 = Node("Wed")


# Link first Node to second node
print("Link first Node to second Node")
list.headval.nextval = e2

e2.nextval = e3

list.listprint()

print()
print("Insertion in a linked list")
print("---------------------------------------------------------------")

class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    #Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
    #Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")
list.listprint()

print()
print("--------------------------------------------------")
print("Inserting at the end of the Linked list")

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    #Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2

e2.nextval = e3
list.AtEnd("Thu")
list.listprint()


print()
print("Inserting in between two data nodes")
print("-----------------------------------------------------------")


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Function to add node
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headval.nextval = e2

e2.nextval = e3
list.Inbetween(list.headval.nextval, "Fri")
list.listprint()



print()
print("Removing an item from a liked list")
print("---------------------------------------------------------")


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

#Function to remove node

    def RemovNode(self, Removekey):
        Headval = self.head

        if (Headval is not None):
            if(Headval.data == Removekey):
                self.head = Headval.next
                Headval = None
                return

        while (Headval is not None):
            if Headval.data == Removekey:
                break
            prev = Headval
            Headval = Headval.next

        if (Headval == None):
            return

        prev.next = Headval.next

        Headval = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data)
            printval = printval.next



llist = SLinkedList()

llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemovNode("Tue")
llist.LListprint()





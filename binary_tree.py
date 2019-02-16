#Create Root

class Node:

    def  __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)


root = Node(10)

root.PrintTree()


# Inserting into a Tree

print("-----------------------------------------------------")
print("Inserting into a Tree")
print("-----------------------------------------------------")


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()

        print(self.data)

root = Node(12)

root.insert(6)

root.insert(14)

root.insert(3)

root.PrintTree()

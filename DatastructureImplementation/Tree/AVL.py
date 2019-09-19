class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)
        print("New root: {}".format(self.root.data))

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insertNode(data, node.left)
        else:
            node.right = self.insertNode(data, node.right)
        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1

        return self.settleViolation(data, node)

    def settleViolation(self, data, node):
        balance = self.calcBalance(node)
        # Case1: left left heavy situation
        if balance > 1 and data < node.left.data:
            print("Left left heavy situation")
            return self.rotateRight(node)
        elif balance < -1 and data > node.right.data:
            print("Right right heavy situation")
            return self.rotateLeft(node)
        if balance > 1 and data > node.left.data:
            print("Left right heavy situation")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        if balance < -1 and data < node.right.data:
            print("Right left heavy situation")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        """
        >1 then left heavy -> right rotation
        """
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)

    def rotateRight(self, node):
        print("Rotating {} to right".format(node.data))
        tempLeft = node.left
        t = tempLeft.right
        tempLeft.right = node
        node.left = t
        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempLeft.height = max(self.calcHeight(tempLeft.left), self.calcHeight(tempLeft.right)) + 1
        return tempLeft

    def rotateLeft(self, node):
        print("Rotating {} to left".format(node.data))
        tempRight = node.right
        t = tempRight.left
        tempRight.left = node
        node.right = t
        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempRight.height = max(self.calcHeight(tempRight.left), self.calcHeight(tempRight.right)) + 1
        return tempRight

    def traverse(self):
        if self.root:
            print("Root: {}".format(self.root.data))
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print("{}".format(node.data))
        if node.right:
            self.traverseInOrder(node.right)


avl = AVL()
l = [50, 100, 90, 80, 70, 10, 20, 30]
for i in l:
    print("Inserting {}".format(i))
    avl.insert(i)
avl.traverse()

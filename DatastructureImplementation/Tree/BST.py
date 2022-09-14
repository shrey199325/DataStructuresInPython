class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key


# Function to insert node in tree recursively
def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)


# Function to print inorder traversal recursively
def inOrderTraversal(root, li):
    if root:
        inOrderTraversal(root.left, li)
        li.append(root.data)
        inOrderTraversal(root.right, li)


# Creating a new BST with root as 50
r = TreeNode(55)
insertNode(r, TreeNode(35))
insertNode(r, TreeNode(25))
insertNode(r, TreeNode(45))
insertNode(r, TreeNode(75))
insertNode(r, TreeNode(65))
insertNode(r, TreeNode(85))

# Print inoder traversal of the BST
ll = []
inOrderTraversal(r, ll)
print(ll)

"""
Heap is a binary tree
Each node can have a left child and right child
min heap: Root node is minimum
max heap: Root node is maximum
Abstract Datatype: Priority Queue
Heap memory is different from this heap and that memory doesn't use this concept.
Root->left(l1)->right(r1)->left of l1(l1-l2)->right of l1(l1-r2)-> left of r1(r1-l3)->right of r1(r1-r3)
Min and max element can be accessed respectively from min and max heaps in O(1) time complexity
If,
    Parent node = i
    left child = 2i+1
    right child = 2i+2
O(N) to construct the tree.
    Reconstruction takes O(logN).
    => O(N) + O(logN) = O(N)
O(logN) time to remove the root node
O(N) time to remove a node
"""

O = object

#
# class Node(O):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# class Heap(O):
#     def __init__(self, node):
#         self.root = node
#
#     def insert(self, node):
#         if not self.root:
#             self.root = node
#             return self.root



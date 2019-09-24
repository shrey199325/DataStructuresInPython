# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        return self.checkVal(A)

    def checkVal(self, a):
        res = 1
        if a is not None and a != -1:
            if a.left > a.val:
                return 0
            else:
                res = self.checkVal(a.left)
            if a.right < a.val:
                return 0
            else:
                res = self.checkVal(a.right)
        return res


